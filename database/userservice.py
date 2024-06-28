from datetime import datetime
from database import get_db
from .models import User


# Users, done
def create_user_db(name, phone_number, password, email):
    db = next(get_db())
    new_user = User(name=name, phone_number=phone_number, password=password, email=email, reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return "User successfully created!"


# done
def get_all_users_db():
    db = next(get_db())
    users = db.query(User).all()
    return users


def get_user_db(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        return user
    return "User not found"


def update_user_db(id, change_info, new_info):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        try:
            if change_info == "name":
                user.name = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "email":
                user.email = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "phone_number":
                user.phone_number = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "password":
                user.password = new_info
                db.commit()
                return "Successfully changed"
        except:
            return "There is no value for changing"
    return False


def delete_user_db(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        db.delete(user)
        db.commit()
        return "User successfully deleted!"
    return "User not found"


def activate_user_db(id: int):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        user.status = True
        db.commit()
        return "User activated successfully."
    return "User not found."


def deactivate_user_db(id: int):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        user.status = False
        db.commit()
        return "User deactivated successfully."
    return "User not found."