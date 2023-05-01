import pytest
import pages
import time

class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.signin_page.open_signin_page(page)
        time.sleep(10)
