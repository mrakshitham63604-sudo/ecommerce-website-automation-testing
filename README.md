# E-Commerce Website Automation Testing

## Project Overview
Automated testing of an e-commerce website using Selenium WebDriver and Pytest.

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- Chrome WebDriver
- WebDriver Manager

## Website Tested
https://www.saucedemo.com/

## Project Structure
```text
ecommerce-website-automation-testing/
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Scenarios
- Valid login
- Invalid login
- Locked user login
- Products page verification
- Add product to cart
- Open shopping cart
- Cart item verification
- Checkout process
- Checkout validation

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
python -m pytest -v
```

## Test Results
All 10 automated test cases passed successfully.

## Author
Automation Testing Project