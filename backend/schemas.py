from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    xp: int
    current_world: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserOut


class LessonOut(BaseModel):
    id: int
    world_id: int
    order: int
    title: str
    description: str
    theory: str
    starter_code: str
    expected_output: str
    hint: str
    xp_reward: int
    is_final_project: bool

    class Config:
        from_attributes = True


class WorldOut(BaseModel):
    id: int
    number: int
    title: str
    description: str
    icon: str
    color: str
    lessons: List[LessonOut] = []

    class Config:
        from_attributes = True


class UserProgressOut(BaseModel):
    id: int
    user_id: int
    lesson_id: int
    completed: bool
    attempts: int
    completed_at: Optional[datetime]

    class Config:
        from_attributes = True


class CodeRunRequest(BaseModel):
    code: str
    lesson_id: int


class CodeRunResult(BaseModel):
    output: str
    error: str
    success: bool
    passed: bool
    execution_time_ms: int


class AIHintRequest(BaseModel):
    lesson_id: int
    code: str
    error_message: Optional[str] = None


class AIHintResponse(BaseModel):
    hint: str


class AIErrorRequest(BaseModel):
    error_message: str
    code: str


class AIErrorResponse(BaseModel):
    explanation: str


class AIExerciseRequest(BaseModel):
    world_number: int
    topic: str


class AIExerciseResponse(BaseModel):
    title: str
    description: str
    starter_code: str
    expected_output: str
    hint: str


class BadgeOut(BaseModel):
    badge_id: str
    earned_at: datetime

    class Config:
        from_attributes = True


class ProgressSummary(BaseModel):
    total_lessons: int
    completed_lessons: int
    xp: int
    badges: List[BadgeOut]
    worlds_progress: List[dict]
