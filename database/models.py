from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from database import Base


class Cars(Base):
    __tablename__ = 'cars'
    id = Column(Integer, autoincrement=True, primary_key=True)
    car_owner_id = Column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    car_name = Column(String, nullable=False)
    car_description = Column(Text, nullable=True)
    car_color = Column(String, nullable=False)
    car_price = Column(Float, nullable=False)
    made_in = Column(String, nullable=False)
    car_created_at = Column(DateTime)
    car_status = Column(Boolean, default=True)

    # Relationship with User
    owner_fk = relationship("User", back_populates="cars", lazy="subquery")

    # One-to-many relationship with Sale
    sales = relationship("Sale", back_populates="car", lazy="subquery", cascade="all, delete", passive_deletes=True)

    # Relationships with Review
    reviews = relationship("Review", back_populates="cars", lazy="subquery", cascade="all, delete",
                           passive_deletes=True, foreign_keys="[Review.car_id]")

    # Relationships with Rent
    rents = relationship("Rent", back_populates="car", lazy="subquery", cascade="all, delete", passive_deletes=True)


class Rent(Base):
    __tablename__ = 'rents'
    id = Column(Integer, autoincrement=True, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id', ondelete='CASCADE'))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    rent_date = Column(DateTime)

    # Correct relationships
    car = relationship("Cars", back_populates="rents")
    user = relationship("User", back_populates="rents")


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    car_id = Column(ForeignKey("cars.id", ondelete='CASCADE'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    created_at = Column(DateTime)

    # Relationships with Cars and User
    cars = relationship("Cars", back_populates="reviews")
    user = relationship("User", back_populates="reviews")


class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    sale_created = Column(DateTime)
    status = Column(Boolean, default=True)
    car_id = Column(Integer, ForeignKey('cars.id', ondelete='CASCADE'), nullable=False)

    # Relationship with Cars
    car = relationship("Cars", back_populates="sales")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True)
    email = Column(String, nullable=False, unique=True)
    status = Column(Boolean, default=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    reg_date = Column(DateTime)

    # Relationships with Cars
    cars = relationship("Cars", back_populates="owner_fk", cascade="all, delete", passive_deletes=True, lazy="subquery")

    # One-to-many relationship with Reviews
    reviews = relationship("Review", back_populates="user", cascade="all, delete", passive_deletes=True,
                           lazy="subquery")

    # One-to-many relationship with Rents
    rents = relationship("Rent", back_populates="user", cascade="all, delete", passive_deletes=True, lazy="subquery")