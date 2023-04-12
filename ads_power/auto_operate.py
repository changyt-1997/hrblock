from selenium import webdriver
from selenium.webdriver.common.by import By


class AutoOperate(object):

    def __init__(self, address):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", address)
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome("chromedriver")
        self.driver.implicitly_wait(60)

    def home_to_create_an_account(self):
        self.driver.get("https://idp.hrblock.com/idp/profile/SAML2/Redirect/SSO?execution=e1s1")
        self.driver.find_element(
            By.XPATH,
            "/html/body/main/div[1]/div[1]/div/div/div/div/section/div/div/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element(By.XPATH, '//*[@id="card1"]/div[2]/div/div[2]/div[2]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="createID"]/a').click()

    def register_email(self, email, username):
        self.driver.find_element(By.XPATH, '//*[@id="email"]/span/input').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="userName"]/span/input').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="showhideNew"]/button').click()

    def run(self):
        self.home_to_create_an_account()

if __name__ == '__main__':
    operate = AutoOperate("127.0.0.1:50761")
    operate.run()
