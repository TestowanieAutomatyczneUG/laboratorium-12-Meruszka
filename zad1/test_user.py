import unittest
from assertpy import assert_that
from user import User

class testUser(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = User()

    def test_data_is_good(self):
        assert_that(self.tmp.getData()).is_not_none()
    
    def test_data_is_good2(self):
        assert_that(self.tmp.getData()).is_instance_of(dict)
    
    def test_name(self):
        assert_that(self.tmp.getData().get('results')[0].get('name')).is_length(3)
    
    def test_emial(self):
        assert_that(self.tmp.getEmail()).contains('@')
    
    def test_dob(self):
        assert_that(self.tmp.getData().get('results')[0].get('dob')).is_length(2)
    
    def test_id(self):
        assert_that(self.tmp.getData().get('results')[0].get('id')).is_not_none()
    