from fastapi import APIRouter
from database.saleservice import *
from datetime import datetime


sale_router = APIRouter(tags=["Control of sales"], prefix="/sale")


# done
@sale_router.post("/add-sale/")
async def add_sale(model: str, year: int, description: str, price: float, car_id: int):
    add = create_sale_db(model=model, year=year, description=description, price=price, car_id=car_id)
    return add


# done
@sale_router.get('/get-exact-sale/')
async def get_exact_sale(id: int):
    exact_sale = get_sale_db(id=id)
    return exact_sale


# not done
@sale_router.put("/change_sale/")
async def change_sale(id: int, change_info, new_info: str):
    data = update_sale_db(id=id, change_info=change_info, new_info=new_info)
    return data


# done
@sale_router.delete("/delete_sale/")
async def delete_sale(id: int):
    data = delete_sale_db(id=id)
    return data


# done
@sale_router.get("/all-sales/")
async def get_all_sales():
    all = get_all_sales_db()
    return all


@sale_router.post("/return-car-back/")
def return_car(sale_id: int):
    return return_car_db(sale_id=sale_id)
