from config import driver, wait, ec
from selenium.webdriver.common.by import By
import time


def test_login(email="mgbukxag@bphfhqbo.com", password="wzlwytgznl"):
    try:
        driver.get("https://awesomeqa.com/ui/index.php?route=account/login")

        driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(password)
        driver.find_element(By.XPATH, '//input[@value="Login"]').click()

        wait.until(
            ec.presence_of_element_located((By.XPATH, "//h2[text()='My Account']"))
        )

        account_title = driver.find_element(By.XPATH, "//h2[text()='My Account']").text
        assert "My Account" in account_title

        print(f"Login successful for user: {email}")
        return True

    except Exception as e:
        print(f"Login failed with error: {str(e)}")
        return False


if __name__ == "__main__":
    test_login()