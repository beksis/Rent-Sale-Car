from fastapi import APIRouter, UploadFile, File
from database.carservice import *
from datetime import datetime, time, date

car_router = APIRouter(tags=["Control of cars"], prefix="/car")


@car_router.post("/add-car/")
async def add_car(car_name: str, car_owner_id: int, car_description: str, car_color: str, car_price: float, made_in: str):
    add = create_car_db(car_name=car_name, car_owner_id=car_owner_id, car_description=car_description, car_color=car_color, car_price=car_price, made_in=made_in)
    return add


# done
@car_router.get('/get-exact-car/')
async def get_exact_car(id: int):
    exact_car = get_car_db(id=id)
    return exact_car


# not done
@car_router.put("/change_car/")
async def change_car(id: int, change_info, new_info: str):
    data = update_car_field_db(id=id, change_info=change_info, new_info=new_info)
    return data


# done
@car_router.delete("/delete_car/")
async def delete_car(id: int):
    data = delete_car_db(id=id)
    return data


# done
@car_router.get("/all-cars/")
async def get_all_cars():
    all = get_all_cars_db()
    return all
