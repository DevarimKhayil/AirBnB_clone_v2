#!/usr/bin/python3
#"""This module defines a base class for all models in our hbnb clone"""
#import uuid
#from datetime import datetime


#class BaseModel:
#    """A base class for all hbnb models"""
#    def __init__(self, *args, **kwargs):
#        """Instatntiates a new model"""
#        if not kwargs:
#            from models import storage
#            self.id = str(uuid.uuid4())
#            self.created_at = datetime.now()
#            self.updated_at = datetime.now()
#            storage.new(self)
#        else:
#            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
#                                                     '%Y-%m-%dT%H:%M:%S.%f')
#            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
#                                                     '%Y-%m-%dT%H:%M:%S.%f')
#            del kwargs['__class__']
#            self.__dict__.update(kwargs)
#
#    def __str__(self):
#        """Returns a string representation of the instance"""
#        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
#        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
#
#    def save(self):
#        """Updates updated_at with current time when instance is changed"""
#        from models import storage
#        self.updated_at = datetime.now()
#        storage.save()
#
#    def to_dict(self):
#        """Convert instance into dict format"""
#        dictionary = {}
#        dictionary.update(self.__dict__)
#        dictionary.update({'__class__':
#                          (str(type(self)).split('.')[-1]).split('\'')[0]})
#        dictionary['created_at'] = self.created_at.isoformat()
#        dictionary['updated_at'] = self.updated_at.isoformat()
#        return dictionary
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        for key, value in kwargs.items():
            if key != '_sa_instance_state':  # filter out SQLAlchemy state
                setattr(self, key, value)
        if not hasattr(self, 'id'):
            self.id = str(uuid.uuid4())
        self.created_at = self.created_at or datetime.utcnow()
        self.updated_at = self.updated_at or datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = self.__class__.__name__
        return f'[{cls}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        """Delete the current instance from the storage"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {key: getattr(self, key) for key in self.__dict__ if not key.startswith('_sa_')}
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat() if self.created_at else None
        dictionary['updated_at'] = self.updated_at.isoformat() if self.updated_at else None
        return dictionary

