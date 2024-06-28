from fastapi import APIRouter
from database.reviewservice import *
from datetime import datetime


review_router = APIRouter(tags=["Control of reviews"], prefix="/review")


# done
@review_router.post("/add-review/")
async def add_review(user_id: int, car_id: int, rating: float, comment: str):
    add = create_review_db(user_id=user_id, car_id=car_id, rating=rating, comment=comment)
    return add


# done
@review_router.get('/get-exact-review/')
async def get_exact_review(id: int):
    exact_review = get_review_db(id=id)
    return exact_review


# not done
@review_router.put("/change_review/")
async def change_review(id: int, change_info, new_info: str):
    data = update_review_db(id=id, change_info=change_info, new_info=new_info)
    return data


# done
@review_router.delete("/delete_review/")
async def delete_review(id: int):
    data = delete_review_db(id=id)
    return data


# done
@review_router.get("/all-reviews/")
async def get_all_reviews():
    all = get_all_reviews_db()
    return all