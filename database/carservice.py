from datetime import datetime
from database import get_db
from .models import Cars


# Create a new car
def create_car_db(car_name, car_owner_id, car_description, car_color, car_price, made_in):
    db = next(get_db())
    new_car = Cars(car_name=car_name, car_owner_id=car_owner_id, car_description=car_description, car_color=car_color, car_price=car_price, made_in=made_in, car_created_at=datetime.now())
    db.add(new_car)
    db.commit()
    return "Car successfully created!"


# Get all cars
def get_all_cars_db():
    db = next(get_db())
    return db.query(Cars).all()


# Получение автомобиля по ID
def get_car_db(id: int):
    db = next(get_db())
    car = db.query(Cars).filter_by(id=id).first()
    if car:
        return car
    return "Car not found"


# Update a car
def update_car_field_db(change_info: str, new_info, car_id: int):
    db = next(get_db())
    car = db.query(Cars).filter_by(id=car_id).first()
    if car:
        if change_info == "car_owner_id":
            car.car_owner_id = new_info
        elif change_info == "car_name":
            car.car_name = new_info
        elif change_info == "car_description":
            car.car_description = new_info
        elif change_info == "car_color":
            car.car_color = new_info
        elif change_info == "car_price":
            car.car_price = new_info
        elif change_info == "made_in":
            car.made_in = new_info
        else:
            return f"No such field to change"
        db.commit()
        db.refresh(car)
        return "Successfully updated"
    return "Car not found"


# Delete a car
def delete_car_db(id: int):
    db = next(get_db())
    car = db.query(Cars).filter_by(id=id).first()
    if car:
        db.delete(car)
        db.commit()
        return "Car successfully deleted!"
    return "Car not found"
