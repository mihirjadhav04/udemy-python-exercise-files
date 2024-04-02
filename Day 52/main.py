from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "C:/Development/chromedriver"
SIMILAR_ACCOUNT = "nusta_timepass_ntp_"
USERNAME = "mihirjadhav04"
PASSWORD = "@kinnari#143$"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div'
        )
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div/div[2]"
        )
        for i in range(10):
            self.follow()
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal
            )
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_tag_name("ul li button")
        # all_buttons.click()
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(
                    "/html/body/div[7]/div/div/div/div[3]/button[2]"
                )
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
# bot.follow()
