def user_entity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "name": user["name"],
        "picture": user.get("picture"),
        "fitness_goal": user.get("fitness_goal"),
        "experience_level": user.get("experience_level"),
        "workout_preference": user.get("workout_preference"),
        "gender": user.get("gender"),
        "dob": user.get("dob"),
        "height": user.get("height"),
        "weight": user.get("weight"),
        "created_at": user["created_at"],
    }
