def user_entity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "name": user["name"],
        "picture": user.get("picture"),
        "primary_goal": user.get("primary_goal"),
        "experience_level": user.get("experience_level"),
        "workout_preference": user.get("workout_preference"),
        "created_at": user["created_at"]
    }
