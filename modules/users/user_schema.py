from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from modules.users.user_enum import FitnessGoalEnum, ExperienceLevelEnum, WorkoutPreferenceEnum

class UserBaseSchema(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = Field(default=None, min_length=2, max_length=50)
    picture: Optional[str] = None
    fitness_goal: Optional[FitnessGoalEnum] = None
    experience_level: Optional[ExperienceLevelEnum] = None
    workout_preference: Optional[WorkoutPreferenceEnum] = None
    gender: Optional[str] = None
    dob: Optional[str] = None  # Date of Birth as ISO string (usually "YYYY-MM-DD")
    height: Optional[float] = None
    weight: Optional[float] = None

class UserCreateSchema(UserBaseSchema):
    email: EmailStr
    name: str = Field(min_length=2, max_length=50)

class UserUpdateSchema(UserBaseSchema):
    pass

class UserResponseSchema(UserBaseSchema):
    id: str
    email: EmailStr
    name: str = Field(min_length=2, max_length=50)

class PaginatedUsersResponse(BaseModel):
    results: List[UserResponseSchema]
    total: int
    page: int
    page_size: int