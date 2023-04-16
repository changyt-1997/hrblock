import time
from io import BytesIO
import pytesseract
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from PIL import Image, ImageFilter

from core.information import search_one_data
from core.hotemail import get_mail
from core.zip_info import get_zip_info


class AutoOperate(object):

    def __init__(self, address):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", address)
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1200, 1050)

        # self.driver = webdriver.Chrome("chromedriver")1200  1050
        self.driver.implicitly_wait(120)

    def home_to_create_an_account(self):
        self.driver.get("https://www.hrblock.com/")
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
        self.driver.find_element(By.XPATH, '//*[@id="createaccounttwo"]/hrb-checkbox[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="createaccounttwo"]/hrb-checkbox[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="submitButton"]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="twoStepVerify"]/hrb-card-content/hrb-link/a').click()

    def start_on_your_taxes(self):
        # self.driver.find_element(By.XPATH, '//*[@id="imbHero"]/button').click()
        # self.driver.find_element(By.XPATH, '//*[@id="imbPsBtnFour"]').click()
        # self.driver.find_element(By.XPATH, '//*[@id="imbPsNext"]/button').click()

        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock4"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[1]/a').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="StackPanelproformaimport"]/div/div[4]/div/fieldset/div/div[3]/div/div/div/div/label').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()

    def your_info(self, first_name, last_name, birthday, ssn, phone, address, zip_number, info_one):
        # 个人信息
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxfirst_t"]').send_keys(first_name)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxlast_t"]').send_keys(last_name)
        date_of_birth, age = self.handle_date(birthday)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxdob_t"]').send_keys(date_of_birth)
        self.driver.find_element(By.ID, "XListBoxxmaritalStatus-shdo").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span6:nth-child(2) #list-option1").click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # # 社保号
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPSSN"]').send_keys(ssn)
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # # 手机地址信息
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxTpDayPhone"]').send_keys(phone)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPAddress"]').send_keys(address)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPZip"]').send_keys(zip_number)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPAddress"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrblOtherResidentStateY"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()
        # # were
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbmfjUSCitizenY"]').click()
        """
        //*[@id="XFormatTextBoxtbTPSSN"]
        """

        # age
        if age == "early":
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbSingleStatusY"]').click()
            self.juvenile()
            # 处理选择学生
        else:
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbSingleStatusN"]').click()
            # 处理不选择学生
        self.start_w_2(zip_number, info_one, age)
        self.send_group(age, info_one["工作"])

    def juvenile(self):
        # pass
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonTPSingleFullPartStudent2"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrblClaimableStatusN"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbParentsLivingY"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbDefineHalfSupportY"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonhasDependents2"]').click()
        # self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()  #  no
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrblNonDependentQustnN"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()

    def start_w_2(self, zip_number, info_one, age):
        # W-2
        self.driver.find_element(By.XPATH, '//*[@id="pageBodyInnerDiv"]/div[2]/div[2]/div[1]/div/a').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[13]/div/div[4]/div[1]/div[3]/div[5]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div[3]/a').click()
        """
        //*[@id="cardActionPanel"]/a
        """
        emp_name, emp_number, emp_address, emp_address_zip = get_zip_info(zip_number)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxbb1"]').send_keys(emp_number)
        except:
            self.driver.find_element(By.XPATH, '//*[@id="XHyperlink1"]').click()
            try:
                self.driver.find_element(By.XPATH, '//*[@id="cardActionPanel"]/a').click()
            except:
                self.driver.find_element(By.XPATH, '//*[@id="cardActionPanel"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxbb1"]').send_keys(emp_number)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxbc_ename"]').send_keys(emp_name)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxbc_eaddress"]').send_keys(emp_address)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxBC_EZIP"]').send_keys(zip_number)
        # Boxes
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_wages"]').send_keys(int(info_one[1]))  # 1
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_Fed_WH"]').send_keys(int(info_one[2]))  # 2
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_SS_wages"]').send_keys(int(info_one[3]))  # 3
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_SS_WH"]').send_keys(int(info_one[4]))  # 4
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_Medicare_wages"]').send_keys(int(info_one[5]))  # 5
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_Medicare_WH"]').send_keys(int(info_one[6]))  # 6

        self.driver.find_element(By.XPATH, '//*[@id="XListBox3-shdo"]').send_keys(info_one[15])  # 15
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox5"]').send_keys(int(info_one[16]))  # 16
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox6"]').send_keys(int(info_one[17]))  # 17
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="TextBlocktbNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()


    def send_group(self, age, work):
        self.driver.find_element(By.XPATH, '//*[@id="primaryOccupation"]').send_keys(work)
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrdbVirtualCurrencyNo"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrdbDynamic1"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbEarnedMoneyN"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelFooter"]/div[2]/div/div/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelFooter"]/div[2]/div/div/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelshpPreCalcs_Footer"]/div/div/div[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelFooter"]/div[2]/div/div/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelshpPreCalcs_Footer"]/div/div/div[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtoncoverageComplete0"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelFooter"]/div[2]/div/div/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock4"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="TextBlock10"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()

        # file
        self.driver.set_window_size(1500, 1050)
        self.driver.find_element(By.XPATH, '//*[@id="menuPanel"]/ul/li[4]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock3"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock109"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="TextBlockIsBasket"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonShowZeroBalance"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        if self.is_exist("The IRS let us know that someone else has already filed with the same SSN as you."):
            # 记录失败信息
            raise SystemExit
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()

        # Enter your driver’s license or state ID.
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonPinAvailable"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButton2"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonNonMFJIdentityPinNo"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="XCheckBoxcbTPUnwilling"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPPin").send_keys("93737")
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        if not self.is_exist("All your hard work has paid off! It’s time to e-file."):
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # 验证码
        src = self.driver.find_element(By.XPATH, '//*[@id="ac-image"]').get_attribute('src')
        code = self.get_img_code(src)
        self.driver.find_element(By.XPATH, '//*[@id="ac-guess"]').send_keys(code)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock1"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock14"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="XHyperlink2"]').click()


    def get_img_code(self, src):
        cookies = self.driver.get_cookies()
        url = f"https://taxes.hrblock.com{src}"
        # session = requests.session()
        cookies_str = ""
        for cookie in cookies:
            cookies_str += f"{cookie['name']}={cookie['value']};"
            # session.cookies.set(cookie['name'], cookie['value'])
        cookies_str = cookies_str[0: -2]
        # res = session.get(url)
        headers = {
            "cookie": cookies_str,
            "host": "taxes.hrblock.com",
            "user-agent": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        }
        res = requests.get(url, headers=headers)
        print(res)
        print(res)
        img_file = BytesIO()
        img_file.write(res.content)
        img = Image.open(img_file)
        img = img.convert('L')
        threshold = 200
        img = img.point(lambda x: 0 if x < threshold else 255)
        img = img.filter(ImageFilter.MedianFilter(size=3))
        code = pytesseract.image_to_string(img)
        return code


    def handle_date(self, birthday):
        try:
            date_of_birth = birthday.strftime("%m/%d/%Y")
            year = birthday.year
        except:
            date_of_birth = birthday
            time_info = birthday.split('/')
            year = time_info[-1]
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
        # self.home_to_create_an_account()
        # info_email = info_one["邮箱----密码"]
        # email, password = info_email.split("----")
        # try:
        #     self.register_email(email, info_one["账号"], info_one["密码"])
        # except Exception as e:
        #     print("账号已存在，进入登录流程")
        #     self.home_to_login(info_one["账号"], info_one["密码"], email, password)
        self.start_on_your_taxes()
        self.your_info(info_one["名"], info_one["姓"], info_one["生日"],
                       int(info_one["社保号"]), int(info_one["电话"]), info_one["街道"], int(info_one["邮编"]), info_one)


if __name__ == '__main__':
    # qrmhayfbsyc@hotmail.com CFQCPD76J
    operate = AutoOperate("127.0.0.1:51625")
    info_one, info_data = search_one_data()
    operate.run(info_one)
    # operate.get_img_code("/captcha/image/MmhESDZPamxCSllpYWJpc1o3Lzg1SG5ia04yYnFSVTdFWVBXeGtEWERiYzRMRWRycXYvVEVkWlRBRnZ6YnA5TnNlNW1BYmFnTEdlMElvMEFVbWQrbzdId0RNb0xBRmIzMGpoTXJSTlh2a1k9")
    # try:
    #     operate.run(info_one)
    # except:
    #     operate.run(info_one)