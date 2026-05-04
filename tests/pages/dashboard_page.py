from playwright.sync_api import Page, expect
import logging

logger = logging.getLogger(__name__)

class DashboardPage:
    """Page Object for the main project board after login."""

    def __init__(self, page: Page):
        self.page = page
        # ── Sidebar ───────────────────────────────────────────────────────────
        self.sidebar_nav = page.locator("nav")

        # ── Board columns ─────────────────────────────────────────────────────
        self.column_headers = page.locator("h2")
        self.column_container = page.locator("div").filter(has=page.locator("h2"))

        # ── Task cards ────────────────────────────────────────────────────────
        self.task_card_by_name = lambda task_name: (page.get_by_role("heading", name=task_name).locator(".."))

    def navigate_to_project(self, project_name: str):
        logger.info(f"Navigating to project: '{project_name}'")
        self.sidebar_nav.get_by_role("heading", name=project_name).click()
        self.page.wait_for_load_state("networkidle")
        logger.info(f"Project '{project_name}' loaded")

    def get_column(self, column_name: str):
        logger.info(f"Locating column: '{column_name}'")
        return self.page.locator("div").filter(
            has=self.page.locator(f"h2:has-text('{column_name}')")
        ).last

    def verify_task_in_column(self, task_name: str, column_name: str):
        logger.info(f"Verifying task '{task_name}' is in column '{column_name}'")
        column = self.get_column(column_name)
        task_card = column.get_by_role("heading", name=task_name, exact=True)
        expect(task_card).to_be_visible(timeout=10_000)
        expect(task_card).to_have_text(task_name)
        assert task_card.inner_text() == task_name, \
            "Task name in UI column doesn't match with task name string from JSON file test data"
        logger.info(f"Task '{task_name}' confirmed in '{column_name}' column")


    def verify_task_tags(self, task_name: str, expected_tags: list[str]):
        logger.info(f"Verifying tags {expected_tags} on task '{task_name}'")
        task_card = self.task_card_by_name(task_name)
        for tag in expected_tags:
            logger.info(f"Checking tag: '{tag}'")
            expect(task_card.get_by_text(tag, exact=True)).to_be_visible(timeout=5_000)
            logger.info(f" Tag '{tag}' confirmed on task '{task_name}'")