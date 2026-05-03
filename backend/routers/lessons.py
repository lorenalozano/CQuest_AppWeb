from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from models import World, Lesson, UserProgress
from schemas import WorldOut, LessonOut
from routers.auth import get_current_user

router = APIRouter(prefix="/lessons", tags=["lessons"])


def auth_user(authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = authorization.split(" ")[1]
    return get_current_user(token, db)


@router.get("/worlds", response_model=List[WorldOut])
def get_worlds(db: Session = Depends(get_db)):
    return db.query(World).order_by(World.number).all()


@router.get("/worlds/{world_number}", response_model=WorldOut)
def get_world(world_number: int, db: Session = Depends(get_db)):
    world = db.query(World).filter(World.number == world_number).first()
    if not world:
        raise HTTPException(status_code=404, detail="World not found")
    return world


@router.get("/{lesson_id}", response_model=LessonOut)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson
