# Setting Up Python Project with Allure for Test Reporting

## Overview
This project demonstrates how to set up a Python project using Selenium, pytest, and Allure for generating detailed test reports.

## Prerequisites
- Python 3.x installed on your system
- pip package manager
- Java Runtime Environment (JRE) installed (for running Allure)

## Installation Steps

### 1. Set Up Virtual Environment (Optional but Recommended)
Create and activate a virtual environment (recommended):

python -m venv .venv
source .venv/bin/activate   
# On Windows use .\.venv\Scripts\activate


### 2. Install Dependencies
Install required Python packages:

pip install -r requirements.txt

### 3. Install Allure Command-line Tool
Install Allure command-line tool for generating reports:
- Follow instructions from [Allure Installation Guide](https://docs.qameta.io/allure/#_installing_a_commandline)

### 4. Running Tests
Run tests with pytest and generate Allure reports:

pytest --alluredir=./allure-results


### 5. Generating Allure Report
Generate Allure HTML report from the results:

allure serve ./allure-results


### 6. Viewing Reports
Open the generated Allure report in your default browser to view detailed test results.

## Project Structure
- tests/ Directory containing test scripts.
- allure-reports/ Directory for storing generated test reports (This one will not be generated until step [__5.__](#5-running-tests) is executed).
- requirements.txt File listing Python dependencies.

## Resources
- [Allure Documentation](https://docs.qameta.io/allure/)
- [pytest Documentation](https://docs.pytest.org/en/latest/)
- [Selenium Documentation](https://www.selenium.dev/documentation/en/)