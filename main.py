import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
from keys import CHROME_BINARY_LOC, CHROME_DRIVER_PATH, CHROME_PROFILE_PATH

speedtest_url="https://www.speedtest.net/"

def pause():
    time_break = random.randint(2,5)
    return time.sleep(time_break)

s=Service(executable_path=CHROME_DRIVER_PATH)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location=(CHROME_BINARY_LOC)

class InternetSpeedTwitterBot:
    def __init__(self, CHROME_DRIVER_PATH):
        self.s=Service(executable_path=CHROME_DRIVER_PATH)
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")
        self.chrome_options.binary_location=(CHROME_BINARY_LOC)
        self.driver = webdriver.Chrome(service=s, options=chrome_options)
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        self.driver.get(speedtest_url)
        self.driver.maximize_window()
        pause()
        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        time.sleep(60)
        notification = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a").click()
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.down =self.driver.find_element(By.CLASS_NAME, "download-speed")
        print(self.up.text)
        print(self.down.text)
    
    def tweet_at_provider(self):
        pass
    
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
# bot.tweet_at_provider()

