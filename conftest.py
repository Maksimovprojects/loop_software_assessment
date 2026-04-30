import pytest
import logging
from playwright.sync_api import Page, Browser, BrowserContext
from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage


logger = logging.getLogger(__name__)

# ── Credentials ──────────────────────────────────────────────────────────────
USERNAME = "admin"
PASSWORD = "password123"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Global browser context settings."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 800},
    }


@pytest.fixture()
def authenticated_page(page: Page) -> Page:
    login = LoginPage(page)
    login.navigate()
    login.login(USERNAME, PASSWORD)
    # logger.info("Login successful — redirected to dashboard")
    return page


@pytest.fixture()
def dashboard(authenticated_page: Page) -> DashboardPage:
    """Returns a DashboardPage bound to an authenticated page."""
    # logger.info("Initializing DashboardPage with authenticated session")
    return DashboardPage(authenticated_page)
