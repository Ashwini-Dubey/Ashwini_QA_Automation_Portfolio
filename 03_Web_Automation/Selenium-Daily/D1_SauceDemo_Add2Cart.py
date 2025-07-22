"""
Title: Day 1 – Web Automation Challenge: Add to Cart Validation (SauceDemo)

Description:
This script automates the login and cart validation workflow for the SauceDemo website.
It performs the following actions:
1. Launches the SauceDemo login page
2. Logs in using standard user credentials
3. Adds the first two products from the inventory to the cart
4. Navigates to the cart and verifies:
   - Both selected products are listed
   - The cart icon displays the correct item count
5. Takes a screenshot of the cart page
6. Closes the browser session

Tools & Tech:
- Selenium WebDriver (Python)
- Chrome Browser
- Implicit and explicit waits

Author: Ashwini Dubey
Date: 22 July 2025

Usage:
Run this script using a Python environment with Selenium installed.
Ensure that ChromeDriver is in the system path.
"""
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


Base_URL = "https://www.saucedemo.com/"

#Step1: Launches the SauceDemo login page
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(Base_URL)
current_url = driver.current_url
assert current_url == Base_URL, "Website Launch failed!"
print("Website Launched Successfully!")

#Step2: Logs in using standard user credentials
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
assert "inventory.html" in driver.current_url, "Login failed!"
print("Login successful!")

#Step3: Adds the first two products from the inventory to the cart
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
assert "Remove" in driver.find_element(By.ID,"remove-sauce-labs-backpack").text, "Backpack not added to the cart!"
print("Backpack added to cart!")
assert "Remove" in driver.find_element(By.ID,"remove-sauce-labs-bike-light").text, "Bike light not added to the cart!"
print("Bike light added to cart!")
assert "2" in driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge").text,"Products not added to the cart."
print("Products are added to cart!")

'''
Step4: Navigates to the cart and verifies:
   - Both selected products are listed
   - The cart icon displays the correct item count
'''
driver.find_element(By.ID,"shopping_cart_container").click()
assert "cart.html" in driver.current_url, "Navigation to cart failed!"
print("Navigation to card successful!")
assert "2" in driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge").text, "Cart is having incorrect product count!"
print("Cart contains correct count of products.")
assert "Backpack" and "Bike Light" in driver.find_element(By.ID,"cart_contents_container").text,"Incorrect Products are in cart."
print("Correct products in the cart.")

#Step5: Takes a screenshot of the cart page.
timestamp = datetime.now()
driver.save_screenshot(f"Cart_{timestamp}")

#Step6: Closes the browser session
driver.close()
