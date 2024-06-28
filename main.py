from fastapi import FastAPI

from api.car_api.cars import car_router
from api.rent_api.rent_cars import rent_router
from api.review_api.reviews import review_router
from api.sale_api.sale_cars import sale_router
from api.user_api.users import user_router
from database import Base, engine

# подключение к проекту базы данных и создание всех таблиц
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/")
app.include_router(user_router)
app.include_router(rent_router)
app.include_router(review_router)
app.include_router(car_router)
app.include_router(sale_router)

