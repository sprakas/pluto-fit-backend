from fastapi import APIRouter, Depends
from modules.users.user_schema import UserCreateSchema, UserResponseSchema, PaginatedUsersResponse, UserUpdateSchema
from modules.users.user_service import UserService
from fastapi import Query
from typing import Optional
from core.jwt import verify_jwt_token
from fastapi import Body

router = APIRouter(dependencies=[Depends(verify_jwt_token)])
service = UserService()

@router.post("", response_model=UserResponseSchema)
def create_user(user: UserCreateSchema):
    return service.create_user(user)

@router.get("/email/{email}", response_model=UserResponseSchema)
def get_user_by_email(email: str):
    return service.get_user_by_email(email)

@router.get("/list", response_model=PaginatedUsersResponse)
def get_all_users(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Number of records per page"),
    search: Optional[str] = Query(None, description="Search term for user fields"),
    sort_by: Optional[str] = Query(None, description="Field to sort by"),
    sort_order: Optional[str] = Query("asc", regex="^(asc|desc)$", description="Sort order: asc or desc"),
    filters: Optional[str] = Query(None, description="Comma-separated field:value pairs for filtering"),
):
    return service.get_all(
        page=page,
        page_size=page_size,
        search=search,
        sort_by=sort_by,
        sort_order=sort_order,
        filters=filters,
    )

@router.get("/{id}", response_model=UserResponseSchema)
def get_user(id: str):
    return service.get_user(id)



@router.put("/{id}", response_model=UserResponseSchema)
def update_user(id: str, updates: UserUpdateSchema = Body(...)):
    updated_user = service.update_user(id, updates.model_dump(exclude_unset=True))
    return updated_user

@router.delete("/{id}")
def delete_user(id: str):
    return service.delete_user(id)
