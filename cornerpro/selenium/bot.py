from selenium.webdriver.common.by import By
from cornerpro.selenium.bot_tips import TipPage


class PageBot:
    def __init__(self, driver):
        self.__driver = driver
        self.btn_bots_expanded = \
            "//div[@class='botCategory cpa-flex-col']/div[@class='cpa-flex-row']/div/button/i[@class='fas fa-minus']"
        self.btn_bots_compressed = \
            "//div[@class='botCategory cpa-flex-col']/div[@class='cpa-flex-row']/div/button/i[@class='fas fa-plus']"
        self.btn_tips = "//div[@class='list']/div/div/div/a[@onclick='botv2.confirmTips(this)']"
        self.__tips = None

    @property
    def driver(self):
        return self.__driver

    @property
    def page_tips(self):
        if self.__tips is None:
            raise Exception('Object is None')
        return self.__tips

    def find_tip(self, index):
        self.driver.implicitly_wait(5)
        return self.driver.find_elements(By.XPATH, self.btn_tips)[index]

    def total_tips(self):
        self.driver.implicitly_wait(5)
        return len(self.driver.find_elements(By.XPATH, self.btn_tips))

    def expanded_button(self):
        buttons = self.driver.find_elements(By.XPATH, self.btn_bots_compressed)
        for button in buttons:
            button.click()

    def collapsed_button(self):
        buttons = self.driver.find_elements(By.XPATH, self.btn_bots_expanded)
        for button in buttons:
            button.click()

    def click_tips(self, tip):
        self.__tips = TipPage(self.driver)
        tip.click()
