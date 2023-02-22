#!/usr/bin/python3
import unittest
import models
import os
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "if is db")
class test_DBStorage(unittest.TestCase):
    """DB Storage test"""

    def setUp(self):
        """ Set up test environment """
        self.store = models.storage

    def tearDown(self):
        """ Remove storage file at end of tests """
        del self.store

    def test_place(self):
        """test"""
        pass
        # place = Place(name='Park', number_rooms=3,
        #               number_bathrooms=1, max_guest=6, price_by_night=120)
        # place.save()
        # self.assertEqual(place.number_bathrooms, 1)
        # self.assertEqual(place.price_by_night, 120)
        # self.assertTrue(place.id in self.store.all())

    def test_state(self):
        """test"""
        pass
        # state = State(name='Lagos')
        # state.save()
        # self.assertEqual(state.name, 'Lagos')
        # self.assertTrue(state.id in self.store.all())

    def test_city(self):
        """test"""
        pass
        # city = City(name='SanDiego')
        # new_state = State()
        # # city.state_id = new_state.id
        # city.save()
        # # self.assertEqual(city.state_id, new_state.id)
        # self.assertEqual(city.name, 'SanDiego')
        # self.assertTrue(city.id in self.store.all())

    def test_user(self):
        """test"""
        pass
        # user = User(email="gui@hbtn.io", password="guipwd")
        # user.save()
        # self.assertTrue(user.id in self.store.all())
        # self.assertEqual(user.email, 'gui@hbtn.io')
