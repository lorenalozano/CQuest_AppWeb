from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from models import Lesson
from schemas import AIHintRequest, AIHintResponse, AIErrorRequest, AIErrorResponse, AIExerciseRequest, AIExerciseResponse
from routers.auth import get_current_user
from services.ai_service import generate_hint, explain_error, generate_exercise

router = APIRouter(prefix="/ai", tags=["ai"])

WORLD_TOPICS = {
    1: "Hello World and printf",
    2: "Variables and data types",
    3: "If/else conditions",
    4: "For and while loops",
    5: "Functions",
    6: "Complete C programs",
}


def auth_user(authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = authorization.split(" ")[1]
    return get_current_user(token, db)


@router.post("/hint", response_model=AIHintResponse)
async def get_hint(req: AIHintRequest, user=Depends(auth_user), db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == req.lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    hint = await generate_hint(lesson.title, lesson.theory, req.code, req.error_message)
    return AIHintResponse(hint=hint)


@router.post("/explain-error", response_model=AIErrorResponse)
async def explain_error_endpoint(req: AIErrorRequest, user=Depends(auth_user)):
    explanation = await explain_error(req.error_message, req.code)
    return AIErrorResponse(explanation=explanation)


@router.post("/generate-exercise", response_model=AIExerciseResponse)
async def gen_exercise(req: AIExerciseRequest, user=Depends(auth_user)):
    topic = WORLD_TOPICS.get(req.world_number, req.topic)
    data = await generate_exercise(req.world_number, topic)
    return AIExerciseResponse(**data)
