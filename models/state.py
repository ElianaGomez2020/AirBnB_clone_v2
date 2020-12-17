#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String
from models.city import City
import models


class State(BaseModel, Base):
    """This is the State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """returns the list of City instances with state_id"""
        from models import storage
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            all_cities = storage.all(City)
            cities = []
            for value in all_cities.items():
                for val in storage.all(State).items():
                    if value.state_id == State.id:
                        cities.append(value)
            return cities
