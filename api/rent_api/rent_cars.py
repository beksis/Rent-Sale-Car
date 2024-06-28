from fastapi import APIRouter
from database.rentservice import *
from datetime import datetime


rent_router = APIRouter(tags=["Control of rents"], prefix="/rent")


@rent_router.post("/do-rent")
def create_rent(user_id: int, car_id: int):
    add = create_rent_db(user_id=user_id, car_id=car_id)
    return add


# done
@rent_router.get('/get-exact-rent/')
async def get_exact_rent(id: int):
    exact_rent = get_rent_db(id=id)
    return exact_rent


# done
@rent_router.put("/change_rent/")
async def change_rent(id: int, change_info, new_info: str):
    data = update_rent_db(id=id, change_info=change_info, new_info=new_info)
    return data


# done
@rent_router.delete("/cancel_rent/")
async def cancel_rent(id: int):
    data = cancel_rent_db(id=id)
    return data


# done
@rent_router.get("/all-rents/")
async def get_all_rents():
    all = get_all_rents_db()
    return all


@rent_router.post("/return-car-back/")
def return_car(rent_id: int):
    return return_car_db(rent_id=rent_id)
