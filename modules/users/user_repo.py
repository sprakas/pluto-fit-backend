from core.db import users
from modules.users.user_entity import user_entity
from bson import ObjectId

class UserRepository:

    def create(self, data: dict):
        result = users.insert_one(data)
        return user_entity(users.find_one({"_id": result.inserted_id}))

    def find_by_email(self, email: str):
        user = users.find_one({"email": email})
        return user_entity(user) if user else None
    
    def find_by_id(self, user_id):
        user = users.find_one({"_id": ObjectId(user_id)})
        return user_entity(user) if user else None

    def find_all(
        self,
        query: dict = None,
        skip: int = 0,
        limit: int = 10,
        sort: list = None
    ):
        query = query.copy() if query else {}
        
        cursor = users.find(query)
        total = cursor.count() if hasattr(cursor, "count") else users.count_documents(query)

        if sort:
            cursor = cursor.sort(sort)

        cursor = cursor.skip(skip).limit(limit)
        results = [user_entity(u) for u in cursor]
        return results, total

    def update(self, email: str, update_data: dict):
        users.update_one({"email": email}, {"$set": update_data})
        return self.find_by_email(email)

    def delete(self, email: str):
        result = users.delete_one({"email": email})
        return result.deleted_count > 0
