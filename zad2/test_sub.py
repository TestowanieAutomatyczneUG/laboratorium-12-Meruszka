import unittest
from unittest import mock
from assertpy import assert_that
from subscriber import Subscriber
from unittest.mock import *
class testSubscriber(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Subscriber()
    
    @patch.object(Subscriber, 'dodajOsobe')
    def test_dodajOsobe(self, mock_dodajOsobe):
        mock_dodajOsobe.return_value = True
        assert_that(self.tmp.dodajOsobe('Szymon')).is_true()
    
    @patch.object(Subscriber, 'dodajOsobe')
    def test_dodajOsobe1(self, mock_dodajOsobe):
        mock_dodajOsobe.side_effect = ValueError
        self.assertRaises(ValueError, self.tmp.dodajOsobe, 123)
    
    @patch.object(Subscriber, 'dodajOsobe')
    def test_dodajOsobe2(self, mock_dodajOsobe):
        mock_dodajOsobe.side_effect = [['Szymon'], ValueError]
        self.tmp.dodajOsobe('Szymon')
        self.assertRaises(ValueError, self.tmp.dodajOsobe, 'Szymon')
    
    @patch.object(Subscriber, 'usunOsobe')
    def test_usunOsobe(self, mock_usunOsobe):
        mock_usunOsobe.return_value = True
        self.tmp.lista = ['Maciek']
        assert_that(self.tmp.usunOsobe('Maciek')).is_true()

    @patch.object(Subscriber, 'usunOsobe')
    def test_usunOsobe2(self, mock_usunOsobe):
        mock_usunOsobe.side_effect = ValueError
        self.assertRaises(ValueError, self.tmp.usunOsobe, 'nie ma nic')
    
    @patch.object(Subscriber, 'usunOsobe')
    def test_usunOsobe3(self, mock_usunOsobe):
        mock_usunOsobe.side_effect = ValueError
        self.assertRaises(ValueError, self.tmp.usunOsobe, 123)
    
    @patch.object(Subscriber, 'wyslijWiadomosc')
    def test_wyslijWiadomosc(self, mock_wyslijWiadomosc):
        mock_wyslijWiadomosc.return_value = True
        self.tmp.lista = ['Maciek']
        assert_that(self.tmp.wyslijWiadomosc('Maciek', 'abc')).is_true()

    @patch.object(Subscriber, 'wyslijWiadomosc')
    def test_wyslijWiadomosc2(self, mock_wyslijWiadomosc):
        mock_wyslijWiadomosc.side_effect = ValueError
        self.tmp.lista = ['Maciek']
        self.assertRaises(ValueError, self.tmp.wyslijWiadomosc, 'Maciek', 123)

    @patch.object(Subscriber, 'wyslijWiadomosc')
    def test_wyslijWiadomosc3(self, mock_wyslijWiadomosc):
        mock_wyslijWiadomosc.side_effect = ValueError
        self.assertRaises(ValueError, self.tmp.wyslijWiadomosc, 'Maciek', '123')
    
    @patch.object(Subscriber, 'wyslijWiadomosc')
    def test_wyslijWiadomosc4(self, mock_wyslijWiadomosc):
        mock_wyslijWiadomosc.side_effect = ValueError
        self.tmp.lista = ['Maciek']
        self.assertRaises(ValueError, self.tmp.wyslijWiadomosc, 123, 'abc')