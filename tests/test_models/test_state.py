#!/usr/bin/python3
#""" """
#from tests.test_models.test_base_model import test_basemodel
#from models.state import State
#
#
#class test_state(test_basemodel):
#    """ """
#
#    def __init__(self, *args, **kwargs):
#        """ """
#        super().__init__(*args, **kwargs)
#        self.name = "State"
##        self.value = State
#
#    def test_name3(self):
#        """ """
#        new = self.value()
#        self.assertEqual(type(new.name), str)i
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    Test class for the State model.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Test case to check the data type of the 'name' attribute in the State model.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

