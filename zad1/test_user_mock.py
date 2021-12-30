from unittest import TestCase, mock

from assertpy.assertpy import assert_that
from user import User
import json
from assertpy import assert_that


def load_mock_data():
    with open("rdata.json", "r") as f:
        return json.loads(f.read())


class TestUser(TestCase):
    def setUp(self) -> None:
        self.patcher = mock.patch('user.User.getData', return_value=load_mock_data())
        self.patcher.start()
        self.tmp = User()

    def test_get_email(self):
        assert_that(self.tmp.getEmail()).is_equal_to("frida.jorgensen@example.com")

    def test_is_mature(self):
        assert_that(self.tmp.isMature()).is_true()