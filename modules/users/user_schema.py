from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

from modules.users.user_enum import (
    PrimaryGoalEnum,
    ExperienceLevelEnum,
    WorkoutPreferenceEnum
)

class UserCreateSchema(BaseModel):
    email: EmailStr
    name: str = Field(min_length=2, max_length=50)
    picture: Optional[str] = None

    primary_goal: Optional[PrimaryGoalEnum] = None
    experience_level: Optional[ExperienceLevelEnum] = None
    workout_preference: Optional[WorkoutPreferenceEnum] = None

class UserResponseSchema(UserCreateSchema):
    id: str
    created_at: float

class PaginatedUsersResponse(BaseModel):
    results: List[UserResponseSchema]
    total: int
    page: int
    page_size: int