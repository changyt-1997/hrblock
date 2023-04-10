from selenium import webdriver


class AutoOperate(object):

    def __init__(self, address):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", address)
        self.driver = webdriver.Chrome(options=options)

    def run(self):
        self.driver.get("https://idp.hrblock.com/idp/profile/SAML2/Redirect/SSO?execution=e1s1")


if __name__ == '__main__':
    operate = AutoOperate("127.0.0.1:50761")
    operate.run()
