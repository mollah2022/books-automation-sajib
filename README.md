# Enterprise UI Automation Framework - Books to Scrape

A production-ready UI automation framework built with Playwright and Pytest,
targeting https://books.toscrape.com. Implements Page Object Model, OOP/SOLID/DRY
principles, HTML and Allure reporting, and full GitHub Actions CI/CD.

---

## Project Overview

This framework validates the complete functionality of the Books to Scrape website
including homepage integrity, book navigation, data consistency, broken links,
and image rendering across paginated results.

---

## Features

- Page Object Model (POM) design pattern
- 5 fully automated test cases covering all acceptance criteria
- Random book selection for realistic test coverage
- Screenshot capture on test failure
- Video recording of every test run
- Playwright trace files for debugging
- Allure HTML report with steps and attachments
- pytest-html report (self-contained)
- GitHub Actions CI/CD (triggers on push and pull request)
- Zero hardcoded waits — all synchronisation via Playwright built-in waiting

---

## Tech Stack

| Layer             | Technology         |
|-------------------|--------------------|
| Language          | Python 3.11        |
| Browser Automation| Playwright 1.44    |
| Test Runner       | Pytest 8.2         |
| HTML Report       | pytest-html 4.1    |
| Allure Report     | allure-pytest 2.13 |
| HTTP Validation   | requests 2.32      |
| CI/CD             | GitHub Actions     |

---

## Installation Guide

### Prerequisites

- Python 3.10 or above
- Git

### Step 1 - Clone the repository

```bash
git clone https://github.com/<your-username>/books-automation-sajib.git
cd books-automation-sajib
```

### Step 2 - Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### Step 3 - Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 - Install Playwright browsers

```bash
playwright install chromium
```

---

## Environment Setup

Create a .env file in the project root (optional - all values have defaults):
