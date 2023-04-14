from selenium import webdriver
from selenium.webdriver.common.by import By

from core.information import search_one_data
from core.hotemail import get_mail


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
            '//*[@id="main-nav"]/div[3]/div[2]/div/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/div/a[1]').click()
        # self.driver.find_element(By.XPATH, '//*[@id="createID"]/a').click()

    def home_to_login(self, username, password, email_name, email_pwd):
        self.driver.get("https://www.hrblock.com/")
        self.driver.find_element(
            By.XPATH,
            '//*[@id="main-nav"]/div[3]/div[2]/div/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/div/form/button').click()
        self.verify_code(email_name, email_pwd)

    def verify_code(self, email_name, email_pwd, depth=0):
        code = get_mail(email_name, email_pwd)
        if not code:
            raise SystemExit
        self.driver.find_element(By.XPATH, '//*[@id="siEmailSCode"]/span/input').clear()
        self.driver.find_element(By.XPATH, '//*[@id="siEmailSCode"]/span/input').send_keys(code)
        if self.is_exist("Error: Sorry, we don't recognize this security code. Please try again."):
            if depth > 5:
                raise SystemExit
            self.verify_code(email_name, email_pwd, depth+1)

    def register_email(self, email, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="email"]/span/input').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="userName"]/span/input').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="showhideNew"]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="password"]/span/input').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="confirmPassword"]/span/input').send_keys(password)
        # self.driver.find_element(By.XPATH, '//*[@id="createaccounttwo"]/hrb-checkbox[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="createaccounttwo"]/hrb-checkbox[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="submitButton"]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="twoStepVerify"]/hrb-card-content/hrb-link/a').click()

    def start_on_your_taxes(self):
        self.driver.find_element(By.XPATH, '//*[@id="imbHero"]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="imbPsBtnFour"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="imbPsNext"]/button').click()

        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock4"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[1]/a').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="StackPanelproformaimport"]/div/div[4]/div/fieldset/div/div[3]/div/div/div/div/label').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()

    def your_info(self, first_name, last_name, birthday, ssn, phone, address, zip_number):
        # 个人信息
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxfirst_t"]').send_keys(first_name)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxlast_t"]').send_keys(last_name)
        date_of_birth, age = self.handle_date(birthday)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxdob_t"]').send_keys(date_of_birth)
        self.driver.find_element(By.XPATH, '//*[@id="XListBoxxmaritalStatus-shdo"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="list-option1"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # 社保号
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPSSN"]').send_keys(ssn)
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # 手机地址信息
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxTpDayPhone"]').send_keys(phone)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPAddress"]').send_keys(address)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPZip"]').send_keys(zip_number)
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrblOtherResidentStateY"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()
        # were
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbmfjUSCitizenY"]').click()

        # age
        if age == "early":
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbSingleStatusY"]').click()
            # 处理选择学生
        else:
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbSingleStatusN"]').click()
            # 处理不选择学生

    def handle_date(self, birthday):
        date_of_birth = birthday.strftime("%m/%d/%Y")
        year = birthday.year
        age = ""
        if year >= 2000:
            age = "early"
        elif 1958 >= year >= 1940:
            age = "old"
        elif 1999 >= year >= 1959:
            age = "common"
        return date_of_birth, age

    def is_exist(self, str_to_find):
        if str_to_find in self.driver.page_source:
            return True
        return False

    def run(self, info_one):
        self.home_to_create_an_account()
        info_email = info_one["邮箱----密码"]
        email, password = info_email.split("----")
        try:
            self.register_email(email, info_one["账号"], info_one["密码"])
        except Exception as e:
            print("账号已存在，进入登录流程")
            self.home_to_login(info_one["账号"], info_one["密码"], email, password)
        self.start_on_your_taxes()
        self.your_info(info_one["名"], info_one["姓"], info_one["生日"],
                       info_one["社保号"], info_one["电话"], info_one["街道"], info_one["邮编"])


if __name__ == '__main__':
    operate = AutoOperate("127.0.0.1:50761")
    info_one, info_data = search_one_data()
    try:
        operate.run(info_one)
    except:
        operate.run(info_one)