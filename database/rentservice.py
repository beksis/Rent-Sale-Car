from datetime import datetime
from database import get_db
from .models import Rent, Cars


def get_all_borrowings_db():
    db = next(get_db())
    rents = db.query(Rent).all()
    return rents


def get_rent_db(id):
    db = next(get_db())
    rent = db.query(Rent).filter_by(id=id).first()
    if rent:
        return rent
    return "Rent is not found"


def update_rent_db(id, change_info, new_info):
    db = next(get_db())
    rent = db.query(Rent).filter_by(id=id).first()
    if rent:
        try:
            if change_info == "car_id":
                rent.car_id = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "user_id":
                rent.user_id = new_info
                db.commit()
                return "Successfully changed"
        except:
            return "There is no value for changing"
    return False


def cancel_rent_db(id):
    db = next(get_db())
    rent = db.query(Rent).filter_by(id=id).first()
    if rent:
        db.delete(rent)
        db.commit()
        return "Rent is successfully deleted!"
    return "Rent is not found"


# Rents
def create_rent_db(user_id: int, car_id: int):
    db = next(get_db())
    car = db.query(Cars).filter(Cars.id == car_id).first()
    if not car:
        return "Car is not found."

    if car.car_status:
        new_rent = Rent(user_id=user_id, car_id=car_id, rent_date=datetime.now())
        db.add(new_rent)
        db.commit()

        mark_car_as_unavailable(car_id)

        return "Rent created successfully."
    else:
        return "Car is not available for rent."


def mark_car_as_unavailable(car_id: int):
    db = next(get_db())
    car = db.query(Cars).filter(Cars.id == car_id).first()
    if car:
        car.car_status = False
        db.commit()
        return "Car marked as unavailable."
    else:
        return "Car is not found."


def return_car_db(rent_id: int):
    db = next(get_db())

    rent = db.query(Rent).filter(Rent.id == rent_id).first()
    if not rent:
        return "Rent record is not found."

    db.commit()

    mark_car_as_available_db(rent.car_id)

    return "Car is returned successfully."


def mark_car_as_available_db(car_id: int):
    db = next(get_db())
    car = db.query(Cars).filter(Cars.id == car_id).first()
    if car:
        car.car_status = True
        db.commit()
        return "Car is marked as available."
    return "Car is not found."
