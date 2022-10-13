import requests
from selenium.webdriver.common.by import By
from cornerpro.selenium.game import GamePage


class TipPage:
    def __init__(self, driver):
        self.driver = driver
        self.unconfirmed = "//div[@class='unconfirmed cpa_section']/div[@class='content']/div[@class='tipList']/div"
        self.confirmed = "//div[@class='confirmed cpa_section']/div[@class='content']/div[@class='tipList']/div"
        self.date_game = 'date'
        self.alert_time_game = 'alertTime'
        self.game = 'game'
        self.league = 'league'
        self.result = 'data-result'
        self.bot_name = 'bot_name'
        self.__games = None
        self.__tips = []
        self.base_url = f'http://localhost:8000/game'

    @property
    def page_game(self):
        if self.__games is None:
            raise Exception('Object is None')
        return self.__games

    def click_games(self, game):
        self.__games = GamePage(self.driver)
        game.click()

    def bot_detail(self):
        self.driver.implicitly_wait(5)
        return self.confirmed_games()

    def confirmed_games(self):
        total_games = len(self.driver.find_elements(By.XPATH, self.confirmed))
        for i in range(total_games):
            game = self.driver.find_elements(By.XPATH, self.confirmed)[i]
            url_link = self.__get_link_game(game)
            response = requests.get(f'{self.base_url}/code/{url_link.split("/")[-1]}')
            if response.status_code == 200:
                continue
            new_dict = {
                'bot': self.__get_bot_name(),
                'date': self.__get_date_game(game),
                'name': self.__get_game_name(game),
                'league': self.__get_league_name(game),
                'result': self.__get_result_game(game),
                'link': url_link,
                'code': url_link.split('/')[-1],
                'events': ''
            }
            self.__games = GamePage(self.driver)
            self.driver.get(url_link)
            events = self.page_game.get_events()
            new_dict.update({
                'events': events
            })
            requests.post(url=self.base_url, json=new_dict)
            self.__tips.append(new_dict)
            self.driver.execute_script("window.history.go(-1)")
            self.driver.implicitly_wait(3)
        return self.__tips

    def unconfirmed_games(self):
        total_games = self.driver.find_elements(By.XPATH, self.unconfirmed)
        for i in range(total_games):
            game = self.driver.find_element(By.XPATH, self.unconfirmed)[i]
            self.__games = GamePage(self.driver)
            self.driver.get(self.__get_link_game(game))
            events = self.page_game.get_events()
            self.driver.execute_script("window.history.go(-1)")

            print(
                self.__get_date_game(game),
                self.__get_alert_time(game),
                self.__get_game_name(game),
                self.__get_league_name(game),
                self.__get_link_game(game)
            )

    def __get_bot_name(self):
        name = self.driver.find_element(By.CLASS_NAME, self.bot_name).text
        return name

    def __get_league_name(self, element):
        return element.find_element(By.CLASS_NAME, self.league).text

    def __get_game_name(self, element):
        return element.find_element(By.CLASS_NAME, self.game).text

    def __get_alert_time(self, element):
        return element.find_element(By.CLASS_NAME, self.alert_time_game).text

    def __get_date_game(self, element):
        return element.find_element(By.CLASS_NAME, self.date_game).text

    def __get_link_game(self, element):
        return element.find_element(By.CLASS_NAME, self.game).get_attribute('href')

    def __get_result_game(self, element):
        return element.get_attribute(self.result)
