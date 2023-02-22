#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
     id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        if kwargs:
            if "id" not in kwargs:
                kwargs["id"] = str(uuid.uuid4())

            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now().isoformat()
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now().isoformat()

            for key, value in kwargs.items():
                if key == "created_at":
                    kwargs[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    kwargs[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                    # hasattr(self, key) and

    def __str__(self):
        """Returns a string representation of the instance"""
        # cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(type(self).__name__, self.id,
                                     self.__dict__)
        # copy = self.__dict__.copy()
        # copy.pop("_sa_instance_state", None)
        # return "[{}] ({}) {}".format(type(self).__name__, self.id, copy)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""

        my_dict = dict(self.__dict__)
        for key in self.__dict__.keys():
            if key == "_sa_instance_state":
                del (my_dict[key])

        # my_dict["__class__"] = str(type(self).__name__)
        my_dict.update({'__class__': self.__class__.__name__})
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()

        return my_dict

    def delete(self):
        """
        delete the current instance from the storage (models.storage)
        by calling the method delete
        """
        models.storage.delete(self)
