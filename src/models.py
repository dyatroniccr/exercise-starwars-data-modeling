import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
"""
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
"""
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(25), nullable=False)
    rotation_period = Column(String(25), nullable=False)
    orbital_period = Column(String(25), nullable=False)
    gravity = Column(String(25), nullable=False)
    population = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    pass

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(50), nullable=False)
    starship_class = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    length = Column(String(10), nullable=False)
    crew = Column(String(10), nullable=False)
    passengers = Column(String(10), nullable=False)
    max_atmosphering_speed = Column(String(10), nullable=False)
    hyperdrive_rating = Column(String(10), nullable=False)
    mglt = Column(String(10), nullable=False)
    capacity = Column(String(10), nullable=False)
    consumables = Column(String(25), nullable=False)
    pilots = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    pass

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(10), nullable=False)
    mass = Column(String(10), nullable=False)
    hair_color = Column(String(10), nullable=False)
    skin_color = Column(String(10), nullable=False)
    gender = Column(String(10), nullable=False)
    eye_color = Column(String(10), nullable=False)
    birth_year = Column(String(15), nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    pass

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    people = relationship(People)
    planet = relationship(Planet)
    vehicle = relationship(Vehicle)
    pass

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Login = Column(String(15), nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    favorite = relationship(Favorite)


def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')