
from playwright.sync_api import Page
from playwright.sync_api import expect
import logging

logger = logging.getLogger(__name__)

class LoginPage:
    """Page Object for the Login screen."""

    URL = "https://animated-gingersnap-8cf7f2.netlify.app/"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Sign in")

    def navigate(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_url("https://animated-gingersnap-8cf7f2.netlify.app/")
        # logger.info("Login verified — URL confirmed dashboard")
