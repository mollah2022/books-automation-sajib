# Enterprise UI Automation Framework - Books to Scrape

A production-ready UI automation framework built with Playwright and Pytest,
targeting https://books.toscrape.com. Implements Page Object Model, OOP, SOLID,
and DRY principles with HTML and Allure reporting and full GitHub Actions CI/CD.

---

## Project Overview

This framework validates the complete functionality of the Books to Scrape website.
It covers homepage integrity, random book navigation, data consistency between pages,
broken link detection, and product image validation across paginated results.

---

## Features

- Page Object Model design pattern
- Five automated test cases covering all acceptance criteria
- Random book selection for realistic test coverage
- Screenshot capture on test failure
- Video recording of every test run
- Playwright trace files for step-by-step debugging
- Allure HTML report with steps and attachments
- pytest-html self-contained report
- GitHub Actions CI/CD pipeline triggering on push and pull request
- No hardcoded waits, all synchronisation via Playwright built-in strategies

---

## Tech Stack

| Layer              | Technology          |
|--------------------|---------------------|
| Language           | Python 3.11+        |
| Browser Automation | Playwright 1.44     |
| Test Runner        | Pytest 8.2          |
| HTML Report        | pytest-html 4.1     |
| Allure Report      | allure-pytest 2.13  |
| HTTP Validation    | requests 2.32       |
| CI/CD              | GitHub Actions      |

---

## Prerequisites

Before cloning and running this project, make sure you have the following installed:

- Python 3.10 or above
- Git
- pip (comes with Python)

To check:

```bash
python3 --version
git --version
pip --version
```

---

## Installation Guide

### Step 1 - Clone the repository

```bash
git clone https://github.com/mollah2022/books-automation-sajib.git
cd books-automation-sajib
```

### Step 2 - Create a virtual environment

```bash
python3 -m venv venv
```

### Step 3 - Activate the virtual environment

On Linux and macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

You will see (venv) at the start of your terminal line when it is active.

### Step 4 - Install Python dependencies

```bash
pip install -r requirements.txt
```

### Step 5 - Install Playwright browser

```bash
playwright install chromium
```

---

## Running Tests

### Run the full test suite

```bash
pytest -v
```

### Run a specific test file

```bash
pytest tests/test_01_homepage.py -v
pytest tests/test_02_book_navigation.py -v
pytest tests/test_03_data_consistency.py -v
pytest tests/test_04_broken_links.py -v
pytest tests/test_05_image_validation.py -v
```

### Run by marker

```bash
pytest -m smoke -v
pytest -m regression -v
pytest -m navigation -v
pytest -m images -v
```

### Run with browser visible (useful for debugging)

```bash
HEADLESS=false pytest -v
```

---

## Project Structure

```
books-automation-sajib/
├── .github/
│   └── workflows/
│       └── playwright.yml
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   └── book_detail_page.py
├── tests/
│   ├── __init__.py
│   ├── test_01_homepage.py
│   ├── test_02_book_navigation.py
│   ├── test_03_data_consistency.py
│   ├── test_04_broken_links.py
│   └── test_05_image_validation.py
├── utils/
│   ├── __init__.py
│   ├── config.py
│   └── helpers.py
├── reports/
├── allure-results/
├── screenshots/
├── videos/
├── traces/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Case Coverage

| ID    | Test Case              | Description                                        | Markers               |
|-------|------------------------|----------------------------------------------------|-----------------------|
| TC-01 | Homepage Validation    | Verify URL, title, headings, and books section     | smoke, ui             |
| TC-02 | Random Book Navigation | Click 5 random books and verify detail page title  | regression, navigation|
| TC-03 | Data Consistency       | Compare title and price on homepage vs detail page | regression, data      |
| TC-04 | Broken Link Validation | Check all hrefs return HTTP 200                    | regression, links     |
| TC-05 | Image Validation       | Verify src, alt, class attributes across 5 pages   | regression, images    |

---

## Environment Variables

All configuration is handled through environment variables with sensible defaults.
You can create a .env file in the project root to override any of these:
---

## Report Generation

### HTML Report

The HTML report is generated automatically every time you run pytest.
It is saved to reports/report.html.

To open it after a test run:

```bash
xdg-open reports/report.html
```

### Allure Report

#### Install Allure CLI on Ubuntu or Debian

```bash
sudo apt-get install -y allure
```

#### Install Allure CLI on macOS

```bash
brew install allure
```

#### Run tests and generate Allure results

```bash
pytest --alluredir=allure-results
```

#### Serve the interactive Allure report

```bash
allure serve allure-results
```

This opens the report in your default browser automatically.

#### Generate a static Allure report

```bash
allure generate allure-results --clean -o allure-report
python3 -m http.server 8080 --directory allure-report
```

Then open http://localhost:8080 in your browser.

---

### Viewing Allure Report from GitHub Actions (No Install Required)

Step 1 - Go to your repository on GitHub
Step 2 - Click the Actions tab
Step 3 - Click on the latest green workflow run
Step 4 - Scroll down to the Artifacts section
Step 5 - Download and unzip allure-report
Step 6 - Open terminal inside the unzipped folder

```bash
cd ~/Downloads/allure-report
python3 -m http.server 8080
```

Step 7 - Open browser and go to:
http://localhost:8080

Step 8 - To stop the server press Ctrl+C in terminal

Note: Python is already installed with this project so no extra install needed.

## GitHub Actions CI/CD

The workflow file is located at .github/workflows/playwright.yml.

### Triggers

- Push to main or dev branch
- Pull request targeting main or dev branch
- Manual trigger from the Actions tab using workflow_dispatch

### Pipeline Steps

1. Checkout the repository
2. Set up Python 3.11
3. Install all pip dependencies
4. Install Playwright and Chromium browser
5. Create artifact output directories
6. Run the full pytest suite
7. Generate Allure HTML report
8. Upload the following artifacts with 30 day retention:
   - html-report
   - allure-results
   - allure-report
   - screenshots
   - videos
   - traces

### Viewing Artifacts from GitHub Actions

1. Go to your repository on GitHub
2. Click the Actions tab
3. Click on the latest workflow run
4. Scroll down to the Artifacts section
5. Download and unzip the artifact you want to view
6. For allure-report: run python3 -m http.server 8080 inside the folder
7. Open http://localhost:8080 in your browser

---

## Design Decisions

| Decision                        | Reason                                                          |
|---------------------------------|-----------------------------------------------------------------|
| Page Object Model               | Separates selectors from test logic, reduces code duplication   |
| BasePage class                  | Single place for all browser interactions, easy to maintain     |
| BookCard dataclass              | Clean data transfer between page objects and tests              |
| Session-scoped browser          | One browser launch per test run, faster execution               |
| Function-scoped context         | Each test gets a fresh context for full isolation               |
| normalize_price utility         | Handles encoding issues when comparing prices across pages      |
| verify=False for link checks    | books.toscrape.com has SSL issues on some machines              |
| continue-on-error in CI         | Artifacts always upload even when tests fail                    |
| No time.sleep() anywhere        | All waits use Playwright networkidle and wait_for_selector      |

---

## Known Limitations

- Broken link test may run slowly on low-bandwidth connections
- Video recording slightly increases test execution time
- Allure CLI must be installed separately to view the report locally
- Tests run sequentially, parallel execution is not configured
- SSL verification is disabled for HTTP link checks due to certificate issues on the target site

---

## Author

Built following industry automation best practices using OOP, SOLID, DRY, and Page Object Model.
