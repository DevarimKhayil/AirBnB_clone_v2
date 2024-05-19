#!/usr/bin/python3
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models import place_amenity

class Amenity(BaseModel, Base):
    """An amenity provided by a place"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity, viewonly=False, overlaps="amenities")

