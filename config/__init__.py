from config.url import Url
from config.expectations import Expectations
from config.playwright import Playwright
from pages.signin_page import SigninPage

url = Url()
urlSignIn = url.DOMAIN + "/signin"
urlStudentsSchedule = url.DOMAIN + "/students-schedule"

playwright = Playwright()
expectations = Expectations()


singnin_page = SigninPage()



