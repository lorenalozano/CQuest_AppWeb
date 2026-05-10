from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from models import Lesson, Exercise
from schemas import CodeRunRequest, CodeRunResult
from routers.auth import get_current_user
from services.code_runner import run_c_code

router = APIRouter(prefix="/code", tags=["code"])


def auth_user(authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = authorization.split(" ")[1]
    return get_current_user(token, db)


@router.post("/run", response_model=CodeRunResult)
def run_code(req: CodeRunRequest, user=Depends(auth_user), db: Session = Depends(get_db)):
    if req.exercise_id:
        exercise = db.query(Exercise).filter(Exercise.id == req.exercise_id).first()
        if not exercise:
            raise HTTPException(status_code=404, detail="Exercise not found")
        expected = exercise.expected_output
    elif req.lesson_id:
        lesson = db.query(Lesson).filter(Lesson.id == req.lesson_id).first()
        if not lesson:
            raise HTTPException(status_code=404, detail="Lesson not found")
        expected = lesson.expected_output
    else:
        raise HTTPException(status_code=400, detail="exercise_id or lesson_id required")

    result = run_c_code(req.code, expected)
    return CodeRunResult(**result)
