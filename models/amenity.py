#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel):
    """Amenities of a place"""
        __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship('Place', secondary="place_amenity")
