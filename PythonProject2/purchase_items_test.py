from config import driver, wait, ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pyautogui

def test_purchase_items():
    try:
        driver.get("https://awesomeqa.com/ui/index.php?route=common/home")
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[1]')))

        macbook_add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        driver.execute_script("arguments[0].scrollIntoView(true);", macbook_add_button)
        macbook_add_button.click()

        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        driver.get("https://awesomeqa.com/ui/index.php?route=common/home")
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[3]')))

        monitor_add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[3]/button[1]/span')
        driver.execute_script("arguments[0].scrollIntoView(true);", monitor_add_button)
        monitor_add_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="input-option218"]/div[2]/label')))


        driver.find_element(By.XPATH, '//*[@id="input-option218"]/div[2]/label').click()
        driver.find_element(By.XPATH, '//*[@id="input-option223"]/div[1]/label').click()
        driver.find_element(By.XPATH, '//*[@id="input-option223"]/div[2]/label').click()
        driver.find_element(By.XPATH, '//*[@id="input-option223"]/div[3]/label').click()

        text_area_1 = driver.find_element(By.XPATH, '//*[@id="input-option208"]')
        text_area_1.send_keys("dbirebvys")
        dropdown = Select(driver.find_element(By.XPATH, '//*[@id="input-option217"]'))
        dropdown.select_by_index(3)


        text_area_2 = driver.find_element(By.XPATH, '//*[@id="input-option209"]')
        text_area_2.send_keys("vfhsrvbybiuef nidufvbi")

        upload_button = driver.find_element(By.XPATH, '//*[@id="button-upload222"]')
        upload_button.click()

        time.sleep(2)
        pyautogui.write(r"uri_ifs___M_d1528c8d-fdb5-401d-9a5f-d7d61e8945a9.jpg")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(5)

        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="button-cart"]')
        add_to_cart_button.click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        driver.get("https://awesomeqa.com/ui/index.php?route=checkout/cart")
        wait.until(ec.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Shopping Cart")]')))

        cart_items = driver.find_elements(By.CSS_SELECTOR, ".table-responsive .text-left a")
        cart_item_names = [item.text for item in cart_items]

        assert "MacBook" in cart_item_names
        assert "Monitor" in cart_item_names

        print("Both items successfully added to cart")
        return True

    except Exception as e:
        print(f"Purchase test failed with error: {str(e)}")
        return False


if __name__ == "__main__":
    test_purchase_items()
