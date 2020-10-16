import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

LOGIN_URL = 'https://emas.ui.ac.id/login/index.php'
DASHBOARD_URL = "https://emas.ui.ac.id/my/"
LOGINERR_CSS = "div.loginerrors > a"
COURSE_CSS = 'div[id=courses-view-in-progress] > div[id=pc-for-in-progress] > div > div.span6 > div > div > div > div.media-body > h4 > a'

class GoldenRetriever():
    def __enter__(self):
        return self

    def __init__(self, verbose=False):
        self.verboseprint = print if verbose else lambda *a, **k: None
        self.session = requests.Session()
        self.courses = CaseInsensitiveDict()

    def login(self, username, password):
        payload = {'username': username, 'password': password}
        login_result = self.session.post(LOGIN_URL, payload)
        login_result = BeautifulSoup(login_result.content, 'html.parser')
        return True if not login_result.select(LOGINERR_CSS) else False
    
    def get_course(self):
        dashboard = self.session.get(DASHBOARD_URL)
        dashboard = BeautifulSoup(dashboard.content, 'html.parser')
        courses = dashboard.select(COURSE_CSS)
        for course in courses:
            self.courses[course.text] = course['href']
        return self.courses if self.courses else None

    def stop(self):
        self.verboseprint("Closing session...")
        self.session.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

if __name__ == "__main__":
    pass