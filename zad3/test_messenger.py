import unittest
from unittest import mock
from assertpy import assert_that
from unittest.mock import *
from messenger import Messenger

class testMessenger(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Messenger()

    @patch.object(Messenger, 'send')
    def test_send1(self, mock_send):
        mock_send.return_value = True
        assert_that(self.tmp.send('text', 'sub')).is_true()
    
    @patch.object(Messenger, 'send')
    def test_send2(self, mock_send):
        mock_send.side_effect = ValueError
        assert_that(self.tmp.send).raises(ValueError).when_called_with(None, None)
    
    @patch.object(Messenger, 'send')
    def test_send3(self, mock_send):
        mock_send.side_effect = ValueError
        assert_that(self.tmp.send).raises(ValueError).when_called_with('text', ['odbiorca'])
    
    @patch.object(Messenger, 'send')
    def test_send4(self, mock_send):
        mock_send.side_effect = ValueError
        assert_that(self.tmp.send).raises(ValueError).when_called_with(None, 'nice')
    
    @patch.object(Messenger, 'receive')
    def test_receive(self, mock_rec):
        mock_rec.return_value = True 
        assert_that(self.tmp.receive('nadawca')).is_true()

    @patch.object(Messenger, 'receive')
    def test_receive2(self, mock_rec):
        mock_rec.side_effect = ValueError
        assert_that(self.tmp.receive).raises(ValueError).when_called_with(None)

    @patch.object(Messenger, 'receive') 
    def test_receive3(self, mock_rec):
        mock_rec.side_effect = ValueError
        assert_that(self.tmp.receive).raises(ValueError).when_called_with([])
    
    @patch.object(Messenger, 'receive') 
    def test_receive4(self, mock_rec):
        mock_rec.side_effect = ValueError
        assert_that(self.tmp.receive).raises(ValueError).when_called_with({})
      