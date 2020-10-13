import unittest, getpass
from GoldenRetriever import GoldenRetriever
from bs4 import BeautifulSoup

class test_gretriever(unittest.TestCase):

    def test_correct_login(self):
        uname = input("Insert correct username: ")
        pword = getpass.getpass("Insert correct password: ")
        with GoldenRetriever(uname, pword) as g:
            soup = BeautifulSoup(g.login().text, 'html.parser')
            err = soup.find_all(id='loginerrormessage')
            self.assertFalse(err)

    def test_false_login(self):
        uname = "aaa"
        pword = "aaa"
        with GoldenRetriever(uname, pword) as g:
            soup = BeautifulSoup(g.login().text, 'html.parser')
            err = soup.find_all(id='loginerrormessage')
            self.assertTrue(err)

    def test_empty_login(self):
        with GoldenRetriever("", "") as g:
            err = g.login()
            self.assertIsNone(err)