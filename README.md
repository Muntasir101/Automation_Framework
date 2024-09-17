# Python Selenium Test Automation Project
This is a Python Selenium project using the Page Object Model (POM) design pattern, which supports logging, configuration management, 
data-driven testing, reporting, parallel execution, and cross-browser capabilities. 
The project is designed to be scalable and easy to maintain for complex web automation.


## Features

- **Page Object Model (POM)**: A structured design pattern where page elements and methods are encapsulated in separate classes, improving maintainability and scalability.
  
- **Logging**: Logs are generated during test execution and stored in the `logs/automation.log` file, capturing details of test flows and errors.

- **Configuration Management**: All environment settings (URLs, browsers, credentials) are managed via the `config/config.ini` file, making it easy to switch between environments.

- **Data-Driven Testing**: Test data is stored in the `data/test_data.xlsx` file, and tests dynamically read data from it, ensuring easy test coverage with various data sets.

- **Reporting**: Test results are stored in `reports/report.html`, which provides detailed execution summaries and statuses.

- **Parallel Execution**: Tests can be run in parallel using `pytest-xdist` for faster execution.

- **Cross-Browser Testing**: Tests can be run across different browsers (Chrome, Firefox, Edge) using Selenium WebDriver.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/selenium-automation.git
2. **Install Dependencies: Install the required Python packages**:
    ```bash
   pip install -r requirements.txt
3. **Configure Settings: Update config/config.ini with the desired environment settings and browser preferences.**
4. **Run Tests: You can run all tests using Pytest:**
    ```bash
    pytest

    # To run tests in parallel (e.g., 2 parallel threads):
    pytest -n 2
5. **Generate Report: After test execution, an HTML report will be generated in the reports/ folder:**
   ```bash
   pytest --html=reports/report.html
6. **Run Tests on Multiple Browsers: Use pytest to run tests on different browsers:**
   ```bash
   pytest --browser=firefox

## Project Highlights
- **Logging**: Every test action, including failures, is logged for easier debugging.
  
- **Cross-Browser**: Easily switch between Chrome, Firefox, and other supported browsers via config.
  
- **Data-Driven**: Tests are dynamically driven by external data (Excel), making it easy to test various scenarios without hardcoding.
  
- **Parallel Execution**: Boosts performance by allowing tests to run simultaneously across multiple threads.

## Running Tests
# Example Test Command
    pytest -v --html=reports/report.html --browser=chrome

## Dependencies
# Ensure you have the following dependencies listed in requirements.txt:
- **selenium**
- **pytest**
- **pytest-xdist**
- **pytest-html**
- **openpyxl**
- **configparser**
