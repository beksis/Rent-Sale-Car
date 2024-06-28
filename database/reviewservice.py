from datetime import datetime
from database import get_db
from .models import Review, User, Cars


# Reviews, done
def create_review_db(user_id, car_id, rating, comment):
    db = next(get_db())
    new_review = Review(user_id=user_id, car_id=car_id, rating=rating, comment=comment, created_at=datetime.now())
    if rating > 10:
        return "You can't give a rating greater than 10"
    if rating < 0:
        return "You can't give a negative rating"
    db.add(new_review)
    db.commit()
    return "Review successfully created!"


# Получение всех отзывов
def get_all_reviews_db():
    db = next(get_db())
    reviews = db.query(Review).all()
    return reviews


# Получение отзыва по ID
def get_review_db(id):
    db = next(get_db())
    review = db.query(Review).filter_by(id=id).first()
    if review:
        return review
    return "Review not found"


# Обновление отзыва
def update_review_db(id, change_info, new_info):
    db = next(get_db())
    review = db.query(Review).filter_by(id=id).first()
    if review:
        try:
            if change_info == "car_id":
                review.car_id = new_info
                db.commit()
                return "Successfully changed car_id"
            elif change_info == "user_id":
                review.user_id = new_info
                db.commit()
                return "Successfully changed user_id"
            elif change_info == "rating":
                if new_info > 10 or new_info < 0:
                    return "Rating must be between 0 and 10"
                review.rating = new_info
                db.commit()
                return "Successfully changed rating"
            elif change_info == "comment":
                review.comment = new_info
                db.commit()
                return "Successfully changed comment"
        except:
            return "There is no value for changing"
    return "Review not found"


# Удаление отзыва
def delete_review_db(id):
    db = next(get_db())
    review = db.query(Review).filter_by(id=id).first()
    if review:
        db.delete(review)
        db.commit()
        return "Review successfully deleted!"
    return "Review not found"
