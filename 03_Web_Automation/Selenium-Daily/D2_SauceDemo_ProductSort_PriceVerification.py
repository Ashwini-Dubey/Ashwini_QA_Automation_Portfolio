"""
Title: Day 2 – Web Automation Challenge: Product Sort & Price Verification (SauceDemo)

Description:
Automate the SauceDemo site to:
1. Log in with standard user credentials
2. Sort products from "Price (low to high)"
3. Capture the names and prices of the first and last product shown after sorting
4. Verify:
   - The first product has the **lowest** price
   - The last product has the **highest** price
5. Take a screenshot of the sorted inventory page
6. Print all product names with their prices in sorted order

Tools & Tech:
- Selenium WebDriver (Python)
- ChromeDriver
- Explicit waits
- Element collections using find_elements()

Hints:
- Use the `<select>` dropdown with tag name `select`
- Sort option value: `lohi` for low-to-high
- Use CSS selectors or XPath to extract product names and prices

Author: Ashwini Dubey
Date: 23 July 2025
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Base_URL = "https://www.saucedemo.com/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

#Step1: Logs in using standard user credentials
def User_Login():
    driver.get(Base_URL)
    current_url = driver.current_url
    assert current_url == Base_URL, "Website Launch failed!"
    print("Website Launched Successfully!")
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    assert "inventory.html" in driver.current_url, "Login failed!"
    print("Login successful!")

#Step2: Sort products from "Price (low to high)"
def Product_Sort():
    sort = Select(driver.find_element(By.CSS_SELECTOR,".product_sort_container"))
    sort.select_by_value("lohi")


#Step3:
def Product_Capture():
    lowest_priced_product_name = driver.find_element(By.CSS_SELECTOR,"a[id='item_2_title_link'] div[class='inventory_item_name ']").text
    lowest_priced_product_price = driver.find_element(By.CSS_SELECTOR,"div[class='inventory_list'] div:nth-child(1) div:nth-child(2) div:nth-child(2) div:nth-child(1)").text
    print(f"{lowest_priced_product_name}:{lowest_priced_product_price}")

    highest_priced_product_name = driver.find_element(By.CSS_SELECTOR,"a[id='item_5_title_link'] div[class='inventory_item_name ']").text
    highest_priced_product_price = driver.find_element(By.CSS_SELECTOR,"div:nth-child(6) div:nth-child(2) div:nth-child(2) div:nth-child(1)").text
    print(f"{highest_priced_product_name}:{highest_priced_product_price}")

#Step5:
def Capture_Screenshot_SortedInventory():
    driver.save_screenshot("SortedInventory.png")

if __name__ == '__main__':
    User_Login()
    Product_Sort()
    Product_Capture()
    Capture_Screenshot_SortedInventory()



