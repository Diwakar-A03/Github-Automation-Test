import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestGithub(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_login(self):
        print("Running Test: Login")
        self.driver.get("https://github.com/login")
        username = self.driver.find_element(By.XPATH, '//*[@id="login_field"]')
        password = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        username.send_keys("diwakara510@gmail.com")
        password.send_keys("Diwakar@10072003")
        enter = self.driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
        enter.send_keys(Keys.RETURN)
        time.sleep(3)

    def test_feedback(self):
        self.test_login()
        self.driver.find_element(By.XPATH, '//*[@id="dashboard"]/div/feed-container/div[1]/div/a').click()
        time.sleep(5)

    def test_homepage(self):
        self.test_login()
        hme = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[1]/a')
        hme.click()
        time.sleep(2)

    def test_search(self):
        self.test_login()
        search = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div[1]/qbsearch-input/div[1]/div[1]/div/div/button/div')
        search.click()
        search1 = self.driver.find_element(By.XPATH, '//*[@id="query-builder-test"]')
        search1.send_keys("Login Page")
        search1.send_keys(Keys.RETURN)
        time.sleep(5)

    def test_issues(self):
        self.test_login()
        issue = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[2]/a[1]')
        issue.click()
        time.sleep(3)

    def test_pull_request(self):
        self.test_login()
        pull_request = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[2]/a[2]')
        pull_request.click()
        time.sleep(3)

    def test_notification(self):
        self.test_login()
        noti = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/notification-indicator/a')
        noti.click()
        time.sleep(3)

    def test_repo_search(self):
        self.test_login()
        hme = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[1]/a')
        hme.click()
        time.sleep(1)
        repo_search = self.driver.find_element(By.XPATH, '//*[@id="dashboard-repos-filter-left"]')
        repo_search.click()
        repo_search.send_keys("Software_Testing")
        time.sleep(3)

    def test_create_repo(self):
        self.test_login()
        hme = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[1]/a')
        hme.click()
        repo = self.driver.find_element(By.XPATH, '//*[@id="repository[name]"]')
        repo.send_keys("Demo")
        repo_button = self.driver.find_element(By.XPATH,'//*[@id="dashboard"]/div/feed-container/div[2]/article[1]/div/div[1]/section/form/div/button')
        repo_button.click()
        time.sleep(3)

    def test_delete_repo(self):
        self.test_login()
        self.driver.get("https://github.com/Diwa")
        demo_repo = self.driver.find_element(By.XPATH, '//*[@id="settings-tab"]')
        demo_repo.click()
        time.sleep(1)
        del_repo = self.driver.find_element(By.XPATH, '//*[@id="dialog-show-repo-delete-menu-dialog"]')
        del_repo.click()
        time.sleep(1)
        del_repo1 = self.driver.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]')
        del_repo1.click()
        time.sleep(1)
        del_repo2 = self.driver.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]')
        del_repo2.click()
        time.sleep(1)
        repo_name = self.driver.find_element(By.XPATH, '//*[@id="verification_field"]')
        repo_name.send_keys("Diwakar-A03/Demo")
        repo_name.submit()
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()