import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

# Fill in your details here to be posted to the login form.

LOGIN_URL = 'https://emas.ui.ac.id/login/index.php'

class GoldenRetriever():
    def __enter__(self):
        return self

    def __init__(self, username, password, verbose=False):
        self.__verboseprint = print if verbose else lambda *a, **k: None
        self.session = requests.Session()
        self.username = username
        self.password = password
        self.courses = CaseInsensitiveDict()

    def login(self):
        if self.username and self.password:
            payload = {'username': self.username, 'password': self.password}
            login_result = self.session.post(LOGIN_URL, payload)
            return login_result
        else:
            return None
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.__verboseprint("Closing session...")
        self.session.close()