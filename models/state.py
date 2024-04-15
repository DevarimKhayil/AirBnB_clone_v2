#!/usr/bin/python3
#""" State Module for HBNB project """
#from models.base_model import BaseModel
#
#
#class State(BaseModel):
#    """ State class """
#    name = ""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Relationship or property is defined based on the storage type
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals to the current State.id"""
            from models import storage
            from models.city import City
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]


