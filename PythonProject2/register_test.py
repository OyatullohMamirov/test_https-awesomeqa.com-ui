from config import driver, wait, ec
from selenium.webdriver.common.by import By
import random
import string
import time


def generate_random_string(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_random_email():
    return f"{generate_random_string()}@{generate_random_string()}.com"


def generate_random_phone():
    return ''.join(random.choice(string.digits) for _ in range(10))


def test_register():
    try:
        driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

        first_name = generate_random_string().capitalize()
        last_name = generate_random_string().capitalize()
        email = generate_random_email()
        telephone = generate_random_phone()
        password = generate_random_string(10)

        driver.find_element(By.XPATH, '//*[@id="input-firstname"]').send_keys(first_name)
        driver.find_element(By.XPATH, '//*[@id="input-lastname"]').send_keys(last_name)
        driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="input-telephone"]').send_keys(telephone)
        driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="input-confirm"]').send_keys(password)

        driver.find_element(By.XPATH, '//input[@name="agree"]').click()
        driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

        wait.until(
            ec.url_contains("success")
        )

        success_text = driver.find_element(By.TAG_NAME, "h1").text
        assert "Your Account Has Been Created" in success_text

        print(f"Registration successful for user: {email} with password: {password}")
        return email, password

    except Exception as e:
        print(f"Registration failed with error: {str(e)}")
        return None, None


if __name__ == "__main__":
    email, password = test_register()
