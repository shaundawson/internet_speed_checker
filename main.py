import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.keys import Keys
from keys import CHROME_BINARY_LOC, CHROME_DRIVER_PATH, CHROME_PROFILE_PATH, TWITTER_USER,TWITTER_PASSWORD
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

s=Service(executable_path=CHROME_DRIVER_PATH)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location=(CHROME_BINARY_LOC)

def pause():
    time_break = random.randint(2,5)
    return time.sleep(time_break)

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
        self.driver.get("https://www.speedtest.net")
        self.driver.maximize_window()
        pause()
        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        time.sleep(60)
        notification = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a").click()
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        self.down =self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(self.up, self.down)
    
   
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        self.driver.maximize_window()
        pause()
        twitter_user = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        twitter_user.send_keys(TWITTER_USER)
        twitter_user.send_keys(Keys.ENTER)
        pause()
        twitter_password = self.driver.find_element(By.NAME,"password")
        twitter_password.send_keys(TWITTER_PASSWORD)
        twitter_password.send_keys(Keys.ENTER)
        pause()
        tweet = f"Hey @ATT, why is my internet speed {self.down}⬇︎/{self.up}⬆︎ when I pay for 500⬇︎/500⬆︎?"
        tweet_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        tweet_button.click()
        print(tweet)
        pause()
        try:
            self.driver.implicitly_wait(10)
            tweet_content = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div")
            pause()
            tweet_content.send_keys(tweet)
            pause()
            send_tweet_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]")
            send_tweet_button.click()
            pause()
            self.driver.quit()
        except exceptions.StaleElementReferenceException as e:
            print(e)
             
                 
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
