import unittest, getpass, time
from GoldenRetriever import GoldenRetriever
from bs4 import BeautifulSoup

class test_gretriever(unittest.TestCase):
        
    def test_correct_login(self):
        self.uname = input("Username: ")
        self.pword = getpass.getpass()
        print("Username: {}\nPassword: {}".format(self.uname, self.pword))
        with GoldenRetriever() as g:
            login_result = g.login(self.uname, self.pword)
            self.assertTrue(login_result)

    def test_false_login(self):
        uname = "aaa"
        pword = "aaa"
        with GoldenRetriever() as g:
            login_result = g.login(uname, pword)
            self.assertTrue(login_result)

if __name__ == "__main__":
    unittest.main()