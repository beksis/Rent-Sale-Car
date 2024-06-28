from datetime import datetime
from database import get_db
from .models import Sale, Cars


# Получение всех продаж
def get_all_sales_db():
    db = next(get_db())
    return db.query(Sale).all()


# Получение продажи по ID
def get_sale_db(id: int):
    db = next(get_db())
    sale = db.query(Sale).filter_by(id=id).first()
    if sale:
        return sale
    return "Sale not found"


def update_sale_db(id, new_info, change_info):
    db = next(get_db())
    sale = db.query(Sale).filter_by(id=id).first()
    if sale:
        try:
            if change_info == "cars_id":
                sale.cars_id = new_info
                db.commit()
                return "Successfully changed cars_id"
            elif change_info == "model":
                sale.model = new_info
                db.commit()
                return "Successfully changed model"
            elif change_info == "year":
                sale.year = new_info
                db.commit()
                return "Successfully changed year"
            elif change_info == "description":
                sale.description = new_info
                db.commit()
                return "Successfully changed description"
            elif change_info == "price":
                sale.price = new_info
                db.commit()
                return "Successfully changed price"
        except:
            return "There is no value for changing"
    return "Sale not found"


# Удаление записи о продаже
def delete_sale_db(id: int):
    db = next(get_db())
    sale = db.query(Sale).filter_by(id=id).first()
    if sale:
        db.delete(sale)
        db.commit()
        return "Sale successfully deleted!"
    return "Sale not found"


def create_sale_db(model, year, description, price, car_id):
    db = next(get_db())
    car = db.query(Cars).filter(Cars.id == car_id).first()
    if not car:
        return "Car not found."

    if car.car_status:
        new_sale = Sale(model=model, year=year, description=description, price=price, car_id=car_id, sale_created=datetime.now())
        db.add(new_sale)
        db.commit()

        mark_car_as_unavailable(car_id)

        return "Sale created successfully."
    else:
        return "Car is not available for sale."


def mark_car_as_unavailable(car_id: int):
    db = next(get_db())
    car = db.query(Cars).filter(Cars.id == car_id).first()
    if car:
        car.car_status = False
        db.commit()
        return "Car marked as unavailable."
    else:
        return "Car not found."


def return_car_db(sale_id: int):
    db = next(get_db())

    sale = db.query(Sale).filter(Sale.id == sale_id).first()
    if not sale:
        return "Sale record not found."

    db.commit()

    mark_car_as_available_db(Sale.car_id)

    return "Car returned successfully."


def mark_car_as_available_db(car_id: int):
    db = next(get_db())
    car = db.query(Cars).filter(Cars.id == car_id).first()
    if car:
        car.car_status = True
        db.commit()
        return "Car marked as available."
    return "Car not found."
