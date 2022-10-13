from selenium.webdriver.common.by import By


class GamePage:
    def __init__(self, driver):
        self.driver = driver
        self.event = "//div[@class='events-list cpa-flex-col']/div"

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
