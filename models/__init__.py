#!/usr/bin/python3
"""
Initialize the models package.
"""

from os import getenv
from sqlalchemy import Table, Column, ForeignKey
from models.base_model import Base

# Define the place_amenity association table
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

# Set the storage type
storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

