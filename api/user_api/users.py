from fastapi import APIRouter
from database.userservice import *
from datetime import datetime


user_router = APIRouter(tags=["Control of users"], prefix="/users")


@user_router.post("/add-user/")
async def add_user(name: str, email: str, password: str, phone_number: int):
    add = create_user_db(name=name, email=email, password=password, phone_number=phone_number)
    return add


@user_router.get('/get-exact-user/')
async def get_exact_user(id: int):
    exact_user = get_user_db(id=id)
    return exact_user


@user_router.put("/change_user/")
async def change_user(id: int, change_info, new_info: str):
    data = update_user_db(id=id, change_info=change_info, new_info=new_info)
    return data


@user_router.delete("/delete_user/")
async def delete_user(id: int):
    data = delete_user_db(id=id)
    return data


@user_router.get("/all-users/")
async def get_all_users():
    all = get_all_users_db()
    return all


@user_router.post("/activate")
def activate_user(id: int):
    return activate_user_db(id)


@user_router.post("/deactivate")
def deactivate_user(id: int):
    return deactivate_user_db(id)