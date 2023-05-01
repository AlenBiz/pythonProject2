from playwright.sync_api import Page
import config



class SigninPage:

    def open_signin_page(self, page: Page) -> None:
        page.goto(config.urlSignIn)


