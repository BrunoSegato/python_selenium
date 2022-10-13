from selenium.webdriver.common.by import By


class PageLogin:

    def __init__(self, driver):
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver

    def login(self, username: str, password: str):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CLASS_NAME, "submit").click()
