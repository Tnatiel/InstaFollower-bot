from cradentials import USERNAME, PASSWORD
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
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
        time.sleep(3)

    def login(self, username: str, password: str):
        """
        Connect the user to instagram
        :param username: str
        :param password: str
        :return: void
        """
        logger.info(f"login >>> Username: {username}, password: {password}")
        user_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")
        user_input.send_keys(username)
        password_input.send_keys(password)
        submit_btn.click()

    def find_followers(self, username: str):
        """
        Get to the instagram page of the given username
        :param username: str
        :return: void
        """
        time.sleep(4)
        logger.info(f"find_followers >>> click search btn")
        search_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]"
                                                        "/div[1]/div/div/div/div/div[2]/div[2]/div/a/div")
        search_btn.click()
        time.sleep(2)
        search_input = self.driver.find_element(
            By.XPATH,
            '/html/body/div[2]/div/div/div/div[1]/div/div/div/'
            'div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        search_input.send_keys(username)
        time.sleep(2)
        search_res = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]"
            "/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a/div")
        logger.info(f"find_followers >>> click res")
        search_res.click()

    def follow(self):
        """
        Follow the followers of the user from find_followers method
        :return: void
        """
        time.sleep(3)
        followers = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]"
            "/div[2]/section/main/div/header/section/ul/li[2]/a/div")
        logger.info(f"follow >>> click followers")
        followers.click()
        time.sleep(5)

        logger.info(f"follow >>> Start following")
        last_follow_count = 0
        while True:
            follow_btns = self.driver.find_elements(By.TAG_NAME, "button")
            wait = WebDriverWait(self.driver, 10)
            for btn in follow_btns:
                if btn.text == "Follow":
                    wait.until(element_to_be_clickable(btn))
                    logger.info(f"follow >>> click on : {btn}")
                    try:
                        btn.click()
                    except ElementClickInterceptedException:
                        logger.info(f"follow >>> this fucker unclickable : {btn}")
                        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(1)
            new_follow_count = len(follow_btns)
            if new_follow_count == last_follow_count:
                break
            last_follow_count = new_follow_count
            actions = ActionChains(self.driver)
            actions.move_to_element(follow_btns[-1]).perform()
            time.sleep(4)
        logger.info(f"follow >>> Done following")


SIMILAR_ACCOUNT = "memes"
"ABC!@#123"

inf = InstaFollower()
inf.login(USERNAME, PASSWORD)
inf.find_followers(SIMILAR_ACCOUNT)
inf.follow()

input("Press enter to close")
