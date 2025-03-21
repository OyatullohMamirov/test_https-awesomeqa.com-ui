from config import driver, wait, ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pyautogui


def test_checkout():
    try:
        driver.get("https://awesomeqa.com/ui/index.php?route=common/home")
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[1]')))

        macbook_add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        macbook_add_button.click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))

        driver.find_element(By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/a').click()
        driver.find_element(By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a').click()
        driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div[2]/div[2]/button[1]').click()

        # Proceed to cart
        driver.get("https://awesomeqa.com/ui/index.php?route=checkout/cart")
        time.sleep(2)
        # Click Checkout
        checkout_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[2]/a')
        checkout_button.click()
        time.sleep(2)
        # Select Guest Checkout
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label')))
        driver.find_element(By.XPATH, '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label').click()
        driver.find_element(By.XPATH, '//*[@id="button-account"]').click()
        time.sleep(2)
        # Fill Billing Details
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="input-payment-firstname"]')))
        driver.find_element(By.XPATH, '//*[@id="input-payment-firstname"]').send_keys("John")
        driver.find_element(By.XPATH, '//*[@id="input-payment-lastname"]').send_keys("Doe")
        driver.find_element(By.XPATH, '//*[@id="input-payment-email"]').send_keys("john.doe@example.com")
        driver.find_element(By.XPATH, '//*[@id="input-payment-telephone"]').send_keys("123456789")
        driver.find_element(By.XPATH, '//*[@id="input-payment-company"]').send_keys("TestCorp")
        driver.find_element(By.XPATH, '//*[@id="input-payment-address-1"]').send_keys("123 Test St")
        driver.find_element(By.XPATH, '//*[@id="input-payment-address-2"]').send_keys("Suite 456")
        driver.find_element(By.XPATH, '//*[@id="input-payment-city"]').send_keys("Test City")
        driver.find_element(By.XPATH, '//*[@id="input-payment-postcode"]').send_keys("12345")
        Select(driver.find_element(By.XPATH, '//*[@id="input-payment-zone"]')).select_by_index(13)
        driver.find_element(By.XPATH, '//*[@id="button-guest"]').click()
        time.sleep(2)
        # # Fill Delivery Details if needed
        # wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="accordion"]/div[3]/div[1]/h4/a"]')))
        # driver.find_element(By.XPATH, '//*[@id="input-shipping-firstname"]').send_keys("John")
        # driver.find_element(By.XPATH, '//*[@id="input-shipping-lastname"]').send_keys("Doe")
        # driver.find_element(By.XPATH, '//*[@id="input-shipping-company"]').send_keys("TestCorp")
        # driver.find_element(By.XPATH, '//*[@id="input-shipping-address-1"]').send_keys("123 Test St")
        # driver.find_element(By.XPATH, '//*[@id="input-shipping-address-2"]').send_keys("Suite 456")
        # driver.find_element(By.XPATH, '//*[@id="input-shipping-city"]').send_keys("Test City")
        # driver.find_element(By.XPATH, '//*[@id="input-shipping-postcode"]').send_keys("12345")
        # driver.find_element(By.XPATH, '//*[@id="button-guest-shipping"]').click()
        # time.sleep(2)
        # Delivery Method
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="collapse-shipping-method"]/div/p[4]/textarea')))
        driver.find_element(By.XPATH, '//*[@id="collapse-shipping-method"]/div/p[4]/textarea').send_keys("Fast Delivery")
        driver.find_element(By.XPATH, '//*[@id="button-shipping-method"]').click()
        time.sleep(2)
        # Payment Method
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="collapse-payment-method"]/div/p[3]/textarea')))
        driver.find_element(By.XPATH, '//*[@id="collapse-payment-method"]/div/p[3]/textarea').send_keys("Credit Card Payment")
        driver.find_element(By.XPATH, '//*[@id="collapse-payment-method"]/div/div[2]/div/input[1]').click()
        driver.find_element(By.XPATH, '//*[@id="button-payment-method"]').click()
        time.sleep(2)
        # Confirm Order
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="button-confirm"]')))
        driver.find_element(By.XPATH, '//*[@id="button-confirm"]').click()

        print("Order successfully placed!")
        return True

    except Exception as e:
        print(f"Checkout test failed with error: {str(e)}")
        return False


if __name__ == "__main__":
    test_checkout()
