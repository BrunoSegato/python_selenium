from selenium.webdriver.common.by import By


class GamePage:

    INDEX_STATS = {
        "ft": "ft",
        "1ª parte": "ht",
        "2ª parte": "st"
    }

    def __init__(self, driver):
        self.driver = driver
        self.event = "//div[@class='events-list cpa-flex-col']/div"
        self.buttons = '//div[@class="stats_toggle"]/button'
        self.data_game = '//div[@class="fact_list"]/div/div[@class="match_fact"]'

    def get_events(self):
        result = []
        events = self.driver.find_elements(By.XPATH, self.event)
        for event in events:
            divs = event.find_elements(By.XPATH, 'div')
            if len(divs) < 2:
                continue
            result.append({
                'time': divs[0].text,
                'event': divs[1].text
            })
        return result

    def get_stats(self):
        result = {}
        buttons = self.driver.find_elements(By.XPATH, self.buttons)
        for button in buttons:
            button.click()
            print(button.text)
            self.driver.implicitly_wait(5)
            stats = self.driver.find_elements(By.XPATH, self.data_game)
            list_stats = []
            for stat in stats:
                data = stat.text.split("\n")
                data_dict = {
                    data[1].lower(): {
                        'home': data[0],
                        'away': data[2]
                    }
                }
                list_stats.append(data_dict)
                del data, data_dict
            result[self.INDEX_STATS.get(button.text.lower())] = list_stats
        return result
