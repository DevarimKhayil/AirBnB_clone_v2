#!/usr/bin/python3
"""
Defines the DBStorage engine.
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """Represents a database storage engine.
    Attributes:
        __engine: The SQLAlchemy engine.
        __session: The SQLAlchemy session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        if cls is None:
            objs = self.__session.query(State).all() + \
                   self.__session.query(City).all() + \
                   self.__session.query(User).all() + \
                   self.__session.query(Place).all() + \
                   self.__session.query(Review).all() + \
                   self.__session.query(Amenity).all()
        else:
            objs = self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs}

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database."""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute."""
        self.__session.remove()

