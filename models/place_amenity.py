#!/usr/bin/python3
from sqlalchemy import Table, Column, String, ForeignKey, MetaData

# Define the metadata object
metadata = MetaData()

# Define the place_amenity association table
place_amenity = Table(
    'place_amenity',
    metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

