#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import Test_basemodel
from models.state import State


classnTestState(TestBaseModel):
    """ Test for state """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
