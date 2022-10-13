from selenium import webdriver
from dotenv import dotenv_values
from cornerpro.selenium.home import CornerPro

config = dotenv_values(".env")


def main():
    ff = webdriver.Firefox()
    g = CornerPro(ff)
    games = []

    g.navigate()
    g.click_login()
    g.page_login.login(username=config['USER_CORNERPRO'], password=config['PASS_CORNERPRO'])
    g.click_bot()
    g.page_bot.expanded_button()
    total_tips = g.page_bot.total_tips()
    for i in range(total_tips):
        tip = g.page_bot.find_tip(i)
        g.page_bot.click_tips(tip)
        games.append(g.page_bot.page_tips.bot_detail())
        g.click_bot()
        g.page_bot.expanded_button()
    ff.quit()
    return games


if __name__ == '__main__':
    print(main())

