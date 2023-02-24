import random
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)


class InstaFollower:

    def __init__(self):
        self.service = ChromeService(executable_path=r"C:\Users\gever\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)

    def login(self, username: str, password: str):
        """
        Connect the user to instagram
        :param username: str
        :param password: str
        """
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        logger.info(f"login >>> Username: {username}, password: {password}")
        user_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")
        user_input.send_keys(username)
        time.sleep(1)
        password_input.send_keys(password)
        submit_btn.click()

    def find_followers(self, username: str):
        """
        Get to the instagram page of the given username
        :param username: str
        :return: void
        """
        search_btn_locator = "/html/body/div[2]/div/div/div/div[1]/div/div/div/" \
                             "div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div"
        search_input_locator = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/" \
                               "div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input"
        search_result_locator = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/" \
                                "div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a/div"

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, search_btn_locator)))
        logger.info(f"find_followers >>> click search btn")
        search_btn = self.driver.find_element(By.XPATH, search_btn_locator)
        search_btn.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, search_input_locator)))
        search_input = self.driver.find_element(By.XPATH, search_input_locator)
        search_input.send_keys(username)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, search_result_locator)))
        search_result = self.driver.find_element(By.XPATH, search_result_locator)
        logger.info(f"find_followers >>> click res")
        search_result.click()

    def follow(self):
        """
        Follow the followers of the user from find_followers method
        """
        followers_btn_locator = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/" \
                                "div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div"
        ok_btn_locator = "/html/body/div[2]/div/div/div/div[2]/div/div[2]/div[1]/" \
                         "div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]"
        try_again_h3_locator = "/html/body/div[2]/div/div/div/div[2]/div/div[2]/" \
                               "div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/h3"

        self.wait.until(EC.presence_of_element_located((By.XPATH, followers_btn_locator)))
        followers = self.driver.find_element(By.XPATH, followers_btn_locator)
        logger.info(f"follow >>> click followers")
        followers.click()

        last_follow_count = 0
        logger.info(f"follow >>> Start following")
        while True:
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
            follow_btns = self.driver.find_elements(By.TAG_NAME, "button")
            for btn in follow_btns:
                if btn.text == "Follow":
                    self.wait.until(EC.element_to_be_clickable(btn))
                    try:
                        btn.click()
                        logger.info(f"follow >>> click on : {btn}")
                    except ElementClickInterceptedException:
                        logger.info(f"follow >>> this btn is cover : {btn} --> need to scroll")
                        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(random.randrange(1, 4))

                if len(self.driver.find_elements(By.XPATH, try_again_h3_locator)):
                    self.driver.find_element(By.XPATH, ok_btn_locator).click()
                    time.sleep(300)
            new_follow_count = len(follow_btns)
            if new_follow_count == last_follow_count:
                break
            last_follow_count = new_follow_count
            actions = ActionChains(self.driver)
            actions.move_to_element(follow_btns[-1]).perform()
            time.sleep(4)
        logger.info(f"follow >>> Done following")


USERNAME = 'sagolmelafefon'
PASSWORD = 'N*t13!217'
SIMILAR_ACCOUNT = "memes"

inf = InstaFollower()
inf.login(USERNAME, PASSWORD)
inf.find_followers(SIMILAR_ACCOUNT)
inf.follow()

input("Press enter to close")
