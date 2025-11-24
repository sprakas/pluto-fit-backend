from enum import Enum

class FitnessGoalEnum(str, Enum):
    BUILD_MUSCLE = "BUILD_MUSCLE"
    LOSE_WEIGHT = "LOSE_WEIGHT"
    MAINTAIN_FITNESS = "MAINTAIN_FITNESS"
    IMPROVE_ENDURANCE = "IMPROVE_ENDURANCE"

class ExperienceLevelEnum(str, Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"

class WorkoutPreferenceEnum(str, Enum):
    GYM = "GYM"
    HOME = "HOME"
    OUTDOOR = "OUTDOOR"
