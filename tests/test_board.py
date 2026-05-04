"""
Data-driven Playwright test suite for the Demo Project Management App.

All test scenarios are defined in data/test_cases.json.
Adding a new test case requires only a new JSON entry — no code changes needed.
"""

import json
import os
import pytest
from playwright.sync_api import Page
from tests.pages.dashboard_page import DashboardPage

# ── Load test data ─────────────────────────────────────────────────────────────
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "test_cases.json")

with open(DATA_FILE) as f:
    TEST_CASES = json.load(f)


def pytest_id(test_case: dict) -> str:
    """Human-readable test ID shown in pytest output."""
    return f"{test_case['id']} | {test_case['project']} | {test_case['task']}"


# ── Data-driven test ───────────────────────────────────────────────────────────
@pytest.mark.regression
@pytest.mark.parametrize("test_case", TEST_CASES, ids=[pytest_id(tc) for tc in TEST_CASES])
def test_task_in_column_with_tags(dashboard: DashboardPage, test_case: dict):
    """
    For each test case:
      1. Navigate to the specified project.
      2. Verify the task exists in the correct column.
      3. Confirm all expected tags are present on the task card.
    """
    project  = test_case["project"]
    task     = test_case["task"]
    column   = test_case["column"]
    tags     = test_case["tags"]

    # Step 1: Navigate to project
    dashboard.navigate_to_project(project)

    # Step 2: Verify task is in the correct column
    dashboard.verify_task_in_column(task, column)

    # Step 3: Verify all tags on the task card
    dashboard.verify_task_tags(task, tags)
