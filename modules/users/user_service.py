from fastapi import HTTPException
from modules.users.user_repo import UserRepository
from modules.users.user_schema import UserCreateSchema
import time

repo = UserRepository()

class UserService:

    def create_user(self, data: UserCreateSchema):
        existing = repo.find_by_email(data.email)
        if existing:
            raise HTTPException(400, "USER_ALREADY_EXISTS")

        user_dict = data.dict()
        user_dict["created_at"] = time.time()

        return repo.create(user_dict)

    def get_user(self, id: str):
        user = repo.find_by_id(id)
        if not user:
            raise HTTPException(404, "USER_NOT_FOUND")
        return user

    def get_user_by_email(self, email: str):
        user = repo.find_by_email(email)
        if not user:
            raise HTTPException(404, "USER_NOT_FOUND")
        return user

    def get_all(
        self,
        page: int = 1,
        page_size: int = 20,
        search: str = None,
        sort_by: str = None,
        sort_order: str = "asc",
        filters: dict = None,
    ):
        query = {}

        if search:
            query["$or"] = [
                {"name": {"$regex": search, "$options": "i"}},
                {"email": {"$regex": search, "$options": "i"}},
            ]

        if filters:
            for key, value in filters.items():
                query[key] = value

        sort = None
        if sort_by:
            sort = [(sort_by, 1 if sort_order == "asc" else -1)]

        skip = (page - 1) * page_size
        limit = page_size

        results, total = repo.find_all(
            query=query,
            skip=skip,
            limit=limit,
            sort=sort,
        )
        return {
            "results": results,
            "total": total,
            "page": page,
            "page_size": page_size,
        }

    def update_user(self, id: str, updates: dict):
        user = repo.find_by_id(id)
        if not user:
            raise HTTPException(404, "USER_NOT_FOUND")

        return repo.update(id, updates)

    def delete_user(self, id: str):
        if not repo.delete(id):
            raise HTTPException(404, "USER_NOT_FOUND")
        return {"message": "SUCCESS"}
