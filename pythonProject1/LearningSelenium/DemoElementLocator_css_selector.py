import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByIdANDName:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys('test@test.com')
        time.sleep(4)
        driver.quit()  # It's a good practice to close the browser after the test is done

findbyid = DemoFindElementByIdANDName()  # Instantiate the class
findbyid.locate_by_id_demo()  # Call the method
