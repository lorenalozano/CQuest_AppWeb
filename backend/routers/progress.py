from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime

from database import get_db
from models import UserProgress, UserBadge, Lesson, World, User
from schemas import ProgressSummary, UserProgressOut, BadgeOut
from routers.auth import get_current_user

router = APIRouter(prefix="/progress", tags=["progress"])

BADGES = {
    1: {"id": "world1", "name": "Hello Hero", "icon": "🌟"},
    2: {"id": "world2", "name": "Variable Voyager", "icon": "🔢"},
    3: {"id": "world3", "name": "Decision Maker", "icon": "🔀"},
    4: {"id": "world4", "name": "Loop Legend", "icon": "🔄"},
    5: {"id": "world5", "name": "Function Fighter", "icon": "⚡"},
    6: {"id": "world6", "name": "C Master", "icon": "🏆"},
}


def auth_user(authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = authorization.split(" ")[1]
    return get_current_user(token, db)


@router.get("/summary", response_model=ProgressSummary)
def get_summary(user=Depends(auth_user), db: Session = Depends(get_db)):
    all_lessons = db.query(Lesson).all()
    completed = db.query(UserProgress).filter(
        UserProgress.user_id == user.id,
        UserProgress.completed == True
    ).all()
    badges = db.query(UserBadge).filter(UserBadge.user_id == user.id).all()

    worlds = db.query(World).order_by(World.number).all()
    worlds_progress = []
    for world in worlds:
        world_lessons = [l for l in all_lessons if l.world_id == world.id]
        world_completed = [p for p in completed if any(l.id == p.lesson_id for l in world_lessons)]
        worlds_progress.append({
            "world_number": world.number,
            "world_title": world.title,
            "total": len(world_lessons),
            "completed": len(world_completed),
            "unlocked": world.number <= user.current_world,
        })

    return ProgressSummary(
        total_lessons=len(all_lessons),
        completed_lessons=len(completed),
        xp=user.xp,
        badges=[BadgeOut(badge_id=b.badge_id, earned_at=b.earned_at) for b in badges],
        worlds_progress=worlds_progress,
    )


@router.post("/complete/{lesson_id}", response_model=UserProgressOut)
def complete_lesson(lesson_id: int, user=Depends(auth_user), db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    prog = db.query(UserProgress).filter(
        UserProgress.user_id == user.id,
        UserProgress.lesson_id == lesson_id
    ).first()

    if not prog:
        prog = UserProgress(user_id=user.id, lesson_id=lesson_id)
        db.add(prog)

    if not prog.completed:
        prog.completed = True
        prog.completed_at = datetime.utcnow()
        user.xp += lesson.xp_reward
        db.flush()

        _check_world_completion(user, lesson, db)

    prog.attempts = (prog.attempts or 0) + 1
    db.commit()
    db.refresh(prog)
    return prog


def _check_world_completion(user: User, completed_lesson: Lesson, db: Session):
    world = db.query(World).filter(World.id == completed_lesson.world_id).first()
    if not world:
        return

    world_lessons = db.query(Lesson).filter(Lesson.world_id == world.id).all()
    completed_ids = {
        p.lesson_id for p in db.query(UserProgress).filter(
            UserProgress.user_id == user.id,
            UserProgress.completed == True
        ).all()
    }

    all_complete = all(l.id in completed_ids for l in world_lessons)
    if all_complete:
        badge_id = BADGES.get(world.number, {}).get("id")
        if badge_id:
            existing = db.query(UserBadge).filter(
                UserBadge.user_id == user.id,
                UserBadge.badge_id == badge_id
            ).first()
            if not existing:
                db.add(UserBadge(user_id=user.id, badge_id=badge_id))

        if user.current_world == world.number:
            user.current_world = world.number + 1
