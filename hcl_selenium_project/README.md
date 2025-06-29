# HCL Selenium Excel Automation Project

This project automates login testing using:
- Selenium WebDriver (Python)
- Excel-based credential input
- Page Object Model (POM) design
- Modular folder structure

## Folder Structure
```
data/         → Excel file with login credentials  
pages/        → Page classes using POM  
utils/        → Browser and Excel utilities  
tests/        → Login test using data-driven approach  
main.py       → Optional runner  
```

## How to Run
1. Install dependencies:
```
pip install selenium webdriver-manager openpyxl
```

2. Run test:
```
python tests/test_login_excel.py
```

## Website Used
🔗 [https://practicetestautomation.com/practice-test-login/](https://practicetestautomation.com/practice-test-login/)