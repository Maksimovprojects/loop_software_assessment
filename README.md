# loop_software_assessment

Playwright Assessment — Demo Project Management App
Data-driven Playwright test suite built with **Python + pytest** for the [Demo App](https://animated-gingersnap-8cf7f2.netlify.app/).

---

## Project Structure

```
asana-playwright-assessment/
├── data/
│   └── test_cases.json          # All test scenarios — single source of truth
├── tests/
│   ├── pages/
│   │   ├── login_page.py        # Page Object: Login screen
│   │   └── dashboard_page.py    # Page Object: Project board
│   └── test_board.py            # Data-driven parametrized test
├── .github/
│   └── workflows/
│       └── playwright.yml       # GitHub Actions CI/CD
├── conftest.py                  # Shared fixtures (login, dashboard)
├── pytest.ini                   # Pytest + Playwright config
├── requirements.txt
└── README.md
```

---

## Setup

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd asana-playwright-assessment

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
python -m playwright install chromium
```

---

## Run Tests

```bash
# Run all tests (headed with slow-motion for visibility)
pytest

# Run headless (e.g., for CI)
pytest --headless

# Run a single test case by ID
pytest -k "TC01"

# Run with HTML report
pytest --html=reports/report.html --self-contained-html
```

---

## How Data-Driven Testing Works

All test cases live in `data/test_cases.json`:

```json
{
  "id": "TC01",
  "project": "Web Application",
  "task": "Implement user authentication",
  "column": "To Do",
  "tags": ["Feature", "High Priority"]
}
```

`pytest.mark.parametrize` dynamically generates one test per entry. To add a new test case, **just add a JSON object** — no code changes required.

---

## CI/CD

GitHub Actions automatically runs the full suite on every push and pull request to `main`. The HTML report is uploaded as a downloadable artifact after each run.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Language |
| Playwright | Browser automation |
| pytest | Test runner |
| pytest-playwright | Playwright/pytest integration |
| pytest-html | HTML test reports |
| GitHub Actions | CI/CD |
