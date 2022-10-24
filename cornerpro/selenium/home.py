from selenium.webdriver.common.by import By
from cornerpro.selenium.login import PageLogin
from cornerpro.selenium.bot import PageBot


class CornerPro:
    def __init__(self, driver, url):
        self.__driver = driver
        self.__url = url
        self.__login = None
        self.__bot = None

    def navigate(self):
        self.driver.get(self.__url)

    @property
    def driver(self):
        return self.__driver

    @property
    def page_login(self):
        if self.__login is None:
            raise Exception('Object is None')
        return self.__login

    @property
    def page_bot(self):
        if self.__bot is None:
            raise Exception('Object is None')
        return self.__bot

    def click_login(self):
        # TODO - Validar se o usuário já não esta logado.
        self.driver.implicitly_wait(5)
        self.__click_menu(text='login')
        self.__login = PageLogin(self.driver)

    def click_bot(self):
        self.driver.implicitly_wait(5)
        self.__click_menu(text='bot')
        self.__bot = PageBot(self.driver)

    def click_home(self):
        self.driver.implicitly_wait(5)
        self.__click_menu(text='todos jogos')

    def click_encontrar(self):
        self.driver.implicitly_wait(5)
        self.__click_menu(text='encontrar')

    def click_live(self):
        self.driver.implicitly_wait(5)
        self.__click_menu(text='live')

    def click_tips(self):
        self.driver.implicitly_wait(5)
        self.__click_menu(text='automated tips')

    def click_time_machine(self):
        self.driver.implicitly_wait(5)
        self.__click_menu(text='timemachine')

    def click_analise_compacta(self):
        self.driver.implicitly_wait(5)
        self.__click_menu(text='análise compacta')

    def __click_menu(self, text):
        elements = self.driver.find_elements(By.CLASS_NAME, "navItem")
        for element in elements:
            self.driver.implicitly_wait(5)
            if element.text.lower() != text:
                continue
            self.driver.implicitly_wait(10)
            element.click()
            break
