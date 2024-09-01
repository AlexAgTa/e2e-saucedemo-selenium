from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# Set up WebDriver
driver = webdriver.Edge()  # Adjust path as needed
wait = WebDriverWait(driver, 10)

# Test Scenario
@allure.feature("Purchasing Flow")
@allure.story("User adds items to the cart and completes a purchase")
def test_purchase_flow():
    try:
        # Navigate to Saucedemo homepage
        driver.get("https://www.saucedemo.com/")
        allure.dynamic.title("Navigate to Saucedemo Homepage")

        #Login to Saucedemo
        login("standard_user","secret_sauce")
        allure.dynamic.title("Login to Swag Labs purchase page")

        # Add items to cart
        add_to_cart("Sauce Labs Backpack")
        allure.dynamic.title("Add Backpack to Cart")

        # Add items to cart
        add_to_cart("Sauce Labs Bike Light")
        allure.dynamic.title("Add Bike Light to Cart")

        # Visualize the cart
        view_cart()
        allure.dynamic.title("View Cart")

        # Complete purchase flow
        complete_purchase_form("John", "Doe", "123")
        allure.dynamic.title("Complete Purchase Form")

        # Finalize purchase
        finalize_purchase()
        allure.dynamic.title("Finalize Purchase")

    finally:
        # Quit WebDriver
        driver.quit()

# Helper functions
@allure.step("Login to Sacedemo web page:")
def login(username, password):
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.XPATH, "//*[@id='login-button']")

    # Fill out purchase form
    wait.until(EC.element_to_be_clickable(username_field)).send_keys(username)
    wait.until(EC.element_to_be_clickable(password_field)).send_keys(password)
    
    # Click on the purchase button
    wait.until(EC.element_to_be_clickable(login_button)).click()

@allure.step("Add item to cart: {item_name}")
def add_to_cart(item_name):
    item_locator = (By.XPATH, f"//div[contains(text(), '{item_name}')]")
    button_expression = item_name.lower().replace(' ', '-') #Turn the item into Add to Cart ID
    add_to_cart_button = (By.ID, f"add-to-cart-{button_expression}")

    wait.until(EC.visibility_of_element_located(item_locator))
    wait.until(EC.element_to_be_clickable(add_to_cart_button)).click()
    

@allure.step("View Cart")
def view_cart():
    cart_link = (By.ID, "shopping_cart_container")
    wait.until(EC.element_to_be_clickable(cart_link)).click()

@allure.step("Complete Purchase Form: First Name={first_name}, Last Name={last_name}, Postal Code={postal_code}")
def complete_purchase_form(first_name, last_name, postal_code):
    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    postal_code_field = (By.ID, "postal-code")
    checkout_button = (By.ID, "checkout")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")

    # Click on the place order button
    wait.until(EC.element_to_be_clickable(checkout_button)).click()

    # Fill out checkout form
    wait.until(EC.element_to_be_clickable(first_name_field)).send_keys(first_name)
    wait.until(EC.element_to_be_clickable(last_name_field)).send_keys(last_name)
    wait.until(EC.element_to_be_clickable(postal_code_field)).send_keys(postal_code)

    #Click on the continue button
    wait.until(EC.element_to_be_clickable(continue_button)).click()

    # Click on the Finish button
    wait.until(EC.element_to_be_clickable(finish_button)).click()

@allure.step("Finalize Purchase")
def finalize_purchase():
    success_message = (By.XPATH, "//h2[contains(text(), 'Thank you for your order!')]")

    # Wait for confirmation message
    confirmation_element = wait.until(EC.visibility_of_element_located(success_message))

    # Assert the text of the confirmation message
    assert "Thank you for your order!" in confirmation_element.text, "Purchase confirmation message not found or incorrect"

    allure.attach(driver.get_screenshot_as_png(), name="Purchase Confirmation", attachment_type=allure.attachment_type.PNG)

# Entry point for running the test
if __name__ == "__main__":
    test_purchase_flow()
