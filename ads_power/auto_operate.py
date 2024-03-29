import random
import signal
import time
from io import BytesIO
from selenium.webdriver.support import expected_conditions as EC

import pytesseract
import retrying
from aip import AipOcr
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image, ImageFilter, ImageEnhance
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from ads_power.s5_proxy import get_proxy_guys
from core.config import settings
from core.error_info import ExistsNameException, SSNisUseException, VerifyCodeException, RiskControlException
from core.information import search_one_data
from core.hotemail import get_mail_hr
from core.logger_info import logger
from core.zip_info import get_zip_info, get_ein_info


pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_PATH


class AutoOperate(object):

    def __init__(self, address):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", address)
        # options.add_argument('--disable-popup-blocking')
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1200, 1050)

        # self.driver = webdriver.Chrome("chromedriver")
        self.driver.implicitly_wait(180)

    def home_to_create_an_account(self):
        logger.info(f"正在打开注册页面")
        try:
            self.driver.get("https://www.hrblock.com/")
        except:
            try:
                self.driver.get("https://www.hrblock.com/")
            except:
                get_proxy_guys()
                self.driver.get("https://www.hrblock.com/")
        self.accept_cookies()
        try:
            self.driver.find_element(
                By.XPATH,
                '//*[@id="clambtn"]').click()
        except:
            self.driver.get("https://www.hrblock.com/")
            self.driver.find_element(
                By.XPATH,
                '//*[@id="clambtn"]').click()
        try:
            self.driver.find_element(By.XPATH, '//*[@id="ciamElmnt"]/app-user-lookup/app-app-layout/main/hrb-layout/hrb-card-content/hrb-button/button').click()
        except:
            target_element = self.driver.find_element('css selector', 'button[data-automation-action="HrbButton_12"]')
            # Perform the click using JavaScript
            self.driver.execute_script("arguments[0].click();", target_element)
            self.accept_cookies()
        # self.driver.find_element(By.XPATH,    //*[@id="ciamElmnt"]/app-user-lookup/app-app-layout/main/hrb-layout/hrb-card-content/hrb-button/button

    def accept_cookies(self):
        if self.is_exist("We use tracking technologies for the correct functioning of our website.  If you click “allow” you are also permitting us to use targeted advertising technologies, if you click “decline” we will not use targeted advertising technologies.  If you would like to configure other preferences, click “customize settings.”"):
            try:
                logger.info(f"正在同意set cookie")
                self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
            except Exception as e:
                logger.info(f"set cookie Error")

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
        time.sleep(30)
        code = get_mail_hr(email_name, email_pwd)
        if not code:
            logger.info(f"获取验证码超时！！！{email_name}")
            raise VerifyCodeException("获取验证码超时")
        self.driver.find_element(By.XPATH, '//*[@id="oobField"]/span/input').clear()
        self.driver.find_element(By.XPATH, '//*[@id="oobField"]/span/input').send_keys(code)
        if self.is_exist("Please review the following information. "):
            if depth > 5:
                raise VerifyCodeException("获取验证码超时")
            self.verify_code(email_name, email_pwd, depth + 1)

    def register_email(self, email, email_pwd, username, password, first_name, last_name):
        logger.info(f"创建H&R账户：邮箱:{email}, 用户名：{username}， 密码：{email_pwd}")
        if self.is_exist("We've got your back."):
            raise RiskControlException("风控错误，重试！")
        self.driver.find_element(By.XPATH, '//*[@name="email"]/span/input').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="password"]/span/input').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="confirmPassword"]/span/input').send_keys(password)
        target_element = self.driver.find_element('css selector', 'span.hrb-checkbox__checkmark.hrb-checkbox--light-green')
        # Perform the click using JavaScript
        self.driver.execute_script("arguments[0].click();", target_element)
        # self.driver.find_element(By.XPATH, '//*[@name="agreePolicy"]/label/span/span').click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn_createaccount"]/button')))
        if self.is_exist("Account already exists for this email."):
            raise ExistsNameException("重复的email")
        try:
            time.sleep(10)
            self.driver.find_element(By.XPATH, '//*[@id="btn_createaccount"]/button').click()
        except:
            raise ExistsNameException("重复的email")

        time.sleep(3)
        self.verify_code(email, email_pwd)
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//input[@name="first_name"]').send_keys(first_name[:1])
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//input[@name="first_name"]').send_keys(first_name[1:2])
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//input[@name="first_name"]').send_keys(first_name[2:])
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//input[@name="Last name"]').send_keys(" ")
        time.sleep(5)
        try:
            for i in last_name:
                self.driver.find_element(By.XPATH, '//input[@name="Last name"]').send_keys(i)
        except:
            self.driver.find_element(By.XPATH, '//input[@name="Last name"]').send_keys(last_name)

        self.driver.find_element(By.XPATH, '//*[@id="createAccount"]/button').click()

        self.driver.find_element(By.XPATH, '//*[@id="ciamElmnt"]/app-ca-two-step-verification/app-app-layout/main/hrb-layout/hrb-card-content/hrb-link/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="accnt_success"]/button').click()
        logger.info(f"创建H&R账户完成")

    def start_on_your_taxes(self):
        logger.info(f"进入用户信息填写流程")
        try:
            self.driver.find_element(By.XPATH, '//*[@id="imbHero"]/button').click()
        except:
            self.driver.refresh()
            self.driver.find_element(By.XPATH, '//*[@id="imbHero"]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="imbPsBtnFour"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="imbPsNext"]/button').click()
        # //*[@id="btnNext"]
        try:
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        except:
            self.driver.refresh()
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock4"]/a').click()
        # To help us get you started,
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonOptionFirstTime"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()

    def your_info(self, first_name, last_name, birthday, ssn, phone, address, zip_number, info_one):
        # 个人信息
        logger.info(f"开始填写个人信息")
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxfirst_t"]').send_keys(first_name)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxlast_t"]').send_keys(last_name)
        date_of_birth, age = self.handle_date(birthday)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxdob_t"]').send_keys(date_of_birth)
        self.driver.find_element(By.XPATH, '//*[@id="XListBoxxmaritalStatus-shdo"]').click()
        try:
            self.driver.find_element(By.XPATH, "/html/body/div[14]/div/div[4]/div[1]/div[3]/div[5]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/ul/li[2]").click()
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxdob_t"]').send_keys(date_of_birth)
        except:
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[14]/div/div[4]/div[1]/div[3]/div[5]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/ul/li[2]").click()
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxdob_t"]').send_keys(date_of_birth)
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()

        try:
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPSSN"]').send_keys(ssn)
        except:
            self.driver.refresh()
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxfirst_t"]').send_keys(first_name)
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxlast_t"]').send_keys(last_name)
            date_of_birth, age = self.handle_date(birthday)
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxdob_t"]').send_keys(date_of_birth)
            self.driver.find_element(By.ID, "XListBoxxmaritalStatus-shdo").click()
            self.driver.find_element(By.CSS_SELECTOR, ".span6:nth-child(2) #list-option1").click()
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # 社保号
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPSSN"]').send_keys(ssn)
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # 手机地址信息
        if len(str(zip_number)) == 4:
            zip_number = f"0{str(zip_number)}"
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxTpDayPhone"]').send_keys(phone)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPAddress"]').send_keys(address)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPZip"]').send_keys(zip_number)
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbTPAddress"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxtbInCareOf"]').send_keys(info_one["工作"])
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrblOtherResidentStateY"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()
        # were
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbmfjUSCitizenY"]').click()
        """
        //*[@id="XFormatTextBoxtbTPSSN"]
        """

        # age
        if age == "early":
            logger.info(f"学生用户，开始处理学生特有流程")
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbSingleStatusY"]').click()
            self.juvenile()
            # 处理选择学生
            logger.info(f"学生用户，处理完成")
        elif age == "old":
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbSingleStatusN"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrblClaimableStatusN"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonhasDependents2"]').click()
            try:
                self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrblNonDependentQustnN"]').click()
            except:
                self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            # Let's personalize your H&R Block experience
            try:
                full_name = self.driver.find_element(By.XPATH, '//*[@id="insText_id87"]').text
            except:
                full_name = self.driver.find_element(By.XPATH, '/html/body/div[14]/div/div[4]/div[1]/div[3]/div[5]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div/p').text
            try:
                today_date = self.driver.find_element(By.XPATH, '//*[@id="insText_id92"]').text
            except:
                today_date = self.driver.find_element(By.XPATH, '/html/body/div[14]/div/div[4]/div[1]/div[3]/div[5]/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/p').text
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxTPFullName"]').send_keys(full_name)
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxTPCurrentDate"]').send_keys(today_date)
            self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[3]/a').click()

            # 老年人，无特殊处理
            pass
        elif age == "common":
            # 普通人，添加银行处理
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbSingleStatusN"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrblClaimableStatusN"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonhasDependents2"]').click()
            try:
                self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrblNonDependentQustnN"]').click()
            except:
                self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            try:
                self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            except:
                self.driver.refresh()
                self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrblNonDependentQustnN"]').click()
                self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            # Let's personalize your H&R Block experience
            time.sleep(3)
            full_name = self.driver.find_element(By.XPATH, '//*[@id="insText_id87"]').text
            today_date = self.driver.find_element(By.XPATH, '//*[@id="insText_id92"]').text
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxTPFullName"]').send_keys(full_name)
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxTPCurrentDate"]').send_keys(today_date)
            self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[3]/a').click()

            pass
        else:
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbSingleStatusN"]').click()
            # 处理不选择学生
        self.start_w_2(zip_number, info_one, age, ssn)
        self.send_group(age, info_one["工作"], info_one)

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

    def start_w_2(self, zip_number, info_one, age, ssn):
        logger.info(f"开始填写w-2表单")
        # W-2  //*[@id="pageBodyInnerDiv"]/div[2]/div[2]/div[1]/div/a
        try:
            self.driver.find_element(By.XPATH, '//a[@class="nextButton"]').click()
        except:
            try:
                self.driver.find_element(By.XPATH,
                                         '/html/body/div[14]/div/div[4]/div[1]/div[4]/div[1]/div/div/div/div[2]/a').click()
            except:
                self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()

        try:
            self.driver.find_element(By.XPATH, '//*[@id="pageBodyInnerDiv"]/div[2]/div[2]/div[1]/div/a').click()
        except:
            try:
                self.driver.find_element(By.XPATH,
                                         '/html/body/div[13]/div/div[4]/div[1]/div[4]/div[1]/div/div/div/div[2]/a').click()
            except:
                pass

            self.driver.find_element(By.XPATH, '//*[@id="pageBodyInnerDiv"]/div[2]/div[2]/div[1]/div/a').click()
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH,
                                     '/html/body/div[14]/div/div[4]/div[1]/div[3]/div[5]/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div[3]/a').click()
        except:
            self.driver.find_element(By.XPATH, '//*[@id="cardActionPanel"]/a').click()
        try:
            self.w_2_table(zip_number, info_one, age, ssn)
        except:
            self.driver.refresh()
            self.w_2_table(zip_number, info_one, age, ssn)

    def w_2_table(self, zip_number, info_one, age, ssn):
        print(zip_number)
        # //*[@id="cardActionPanel"]/a
        emp_name, emp_number, emp_address = info_one["公司名称"], info_one["公司编号"], info_one["公司地址"]
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

        # ssn
        if self.is_exist("Employee's Information"):
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxEmployeeValidSSN"]').send_keys(ssn)

        # Boxes
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_wages"]').send_keys(int(info_one[1]))  # 1
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_Fed_WH"]').send_keys(int(info_one[2]))  # 2
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_SS_wages"]').send_keys(int(info_one[3]))  # 3
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_SS_WH"]').send_keys(int(info_one[4]))  # 4
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_Medicare_wages"]').send_keys(int(info_one[5]))  # 5
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxW2_Medicare_WH"]').send_keys(int(info_one[6]))  # 6

        # self.driver.find_element(By.XPATH, '//*[@id="XListBox3-shdo"]').click()  # 15
        # ul_element = self.driver.find_element(By.XPATH, '/html/body/div[14]/div/div[4]/div[1]/div[3]/div[5]/div[2]/div/div[2]/fieldset[7]/div[1]/div/div/div/div/table/tbody/tr[2]/td[2]/div/div/div/ul')
        result = ['Choose', 'Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado',
                  'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
                  'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
                  'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
                  'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Marianas', 'Ohio',
                  'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota',
                  'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Virgin Islands(US)', 'Washington',
                  'Washington DC', 'West Virginia', 'Wisconsin', 'Wyoming']
        # dex = result.index(info_one[15]) * 2
        # self.driver.execute_script(f"arguments[0].scrollTop += {dex};", ul_element)
        # target_element = self.driver.find_element(By.XPATH, f'//*[@id="select-list"]/li[text() = "{info_one[15]}"]')
        # while True:
        #     if not target_element.is_displayed():
        #         self.driver.execute_script("arguments[0].scrollTop += 10;", ul_element)
        #         continue
        #     break
        # target_element.click()
        # self.driver.execute_script("arguments[0].click();", target_element)   //*[@id="XListBox1-shdo"]
        self.driver.find_element(By.ID, "XListBox3-shdo").click()
        self.driver.find_element(By.CSS_SELECTOR, f".span3 #list-option{result.index(info_one[15])}").click()


        # self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox4"]').send_keys(emp_number)  # state ID number
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox5"]').send_keys(int(info_one[16]))  # 16
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox6"]').send_keys(int(info_one[17]))  # 17
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox6"]').click()  # 17
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="TextBlocktbNext"]').click()
        except:
            self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()
        # time.sleep(10)
        # if self.is_exist("EIN entry is not in the normal range"):   - 程序运行失败：Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="insText_id87"]"}
        #     self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxbb1"]').clear()
        #     self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxbc_ename"]').clear()
        #     self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxbc_eaddress"]').clear()
        #     emp_name, emp_number, emp_address, emp_address_zip = get_zip_info(str(int(zip_number)))
        #     if not emp_name:
        #         emp_name, emp_number, emp_address = get_ein_info(str(int(zip_number)), num=2)
        #     self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxbb1"]').send_keys(emp_number)
        #     self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxbc_ename"]').send_keys(emp_name)
        #     self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxbc_eaddress"]').send_keys(emp_address)
        #     self.driver.find_element(By.XPATH, '//*[@id="TextBlocktbNext"]').click()  //*[@id="btnNext"]     //*[@id="btnNext"]
        try:
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        except:
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            # self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBoxBC_EZIP"]').send_keys(zip_number)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()  # //*[@id="btnNext"]
        except:
            self.driver.find_element(By.XPATH, '/html/body/div[13]/div/div[4]/div[1]/div[4]/div[2]/div[1]/a').click()
        logger.info(f"w-2表单填写完成")

    def send_group(self, age, work, info_one):
        self.driver.find_element(By.XPATH, '//*[@id="primaryOccupation"]').send_keys(work)
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        #  Did you receive, sell, exchange, or dispose of any cryptocurrency?
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrdbVirtualCurrencyNo"]').click()
        # Do you have any foreign accounts or assets?
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrdbDynamic1"]').click()
        # Did you earn money in any states besides Michigan in 2022?
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonrbEarnedMoneyN"]').click()
        # Here's your income.
        self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelFooter"]/div[2]/div/div/a').click()
        # Here’s all your income we know about.
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # //*[@id="ShowHidePanelFooter"]/div[2]/div/div/a/span[1]  Here are your adjustments a
        try:
            self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelFooter"]/div[2]/div/div/a').click()
        except:
            self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelFooter"]/div[2]/div/div/a/span[1]').click()
        # Delanna, the standard deduction is the best choice for you!
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # Here are all your adjustments and deductions we know about.
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # Here are your credits.
        self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelshpPreCalcs_Footer"]/div/div/div[2]/a').click()
        # Your return doesn’t currently include any credit
        self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelFooter"]/div[2]/div/div/a').click()
        # Let's start on your taxes, payments, and penalties.
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # Did everyone in your household have health insurance in 2022?   //*[@id="XRadioButtoncoverageComplete0"]
        try:
            self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelshpPreCalcs_Footer"]/div/div/div[2]/a').click()
        except:
            pass
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtoncoverageComplete0"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # Thanks, that’s all we needed to know
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # Here are your additional taxes, payments, and penalties.
        self.driver.find_element(By.XPATH, '//*[@id="ShowHidePanelFooter"]/div[2]/div/div/a').click()
        # Here are all your taxes, payments, and penalties we know about.
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # Let's wrap up your Federal taxes.
        # Here are some things we'll ask about:
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # Let us know if any of these apply to you.
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # Let's start checking what you've entered.
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # Federal Accuracy ReviewTM
        # Report
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock4"]/a').click()
        # Here's a quick look.
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        # //*[@id="TextBlock10"]/a
        # self.driver.find_element(By.XPATH, '//*[@id="TextBlock10"]/a').click()   //*[@id="ShowHidePanelFooter"]/div[2]/div/div/a    //*[@id="btnNext"]
        # self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()

        # file
        self.driver.set_window_size(1500, 1050)
        time.sleep(20)
        self.driver.find_element(By.XPATH, '//*[@id="menuPanel"]/ul/li[4]').click()
        try:
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock3"]/a').click()
        except:
            self.driver.find_element(By.XPATH, '//*[@id="menuPanel"]/ul/li[4]').click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock3"]/a').click()
        # self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock109"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div[2]/div[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="TextBlockNextButtonText"]').click()
        # self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()  //*[@id="PageFooter1"]/div/div[2]/div[2]/a   //*[@id="btnNext"]
        # self.driver.find_element(By.XPATH, '//*[@id="TextBlockIsBasket"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        if age == "common":
            time.sleep(4)
            self.driver.execute_script("window.scrollBy(0, 1000);")
            # How do you want to receive your federal refund?   //*[@id="PageFooter1"]/div/div[1]/div[2]/a   //*[@id="XRadioButtonDDOption"]
            try:
                self.driver.find_element(By.ID, "XRadioButtonDDOption").click()
            except:
                target_element = self.driver.find_element(By.ID, "XRadioButtonDDOption")
                self.driver.execute_script("arguments[0].click();", target_element)
            self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div[1]/div[2]/a').click()

            amount = self.driver.find_element(By.XPATH, '//*[@id="TextBlock2"]').text
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox1"]').send_keys(self.handle_bank_number(int(info_one['transit_number'])))
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox2"]').send_keys(int(info_one['account_number']))
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox3"]').send_keys(amount)
            # select
            self.driver.find_element(By.ID, "XListBox1-shdo").click()
            if info_one["account_type"] == "Savings":
                self.driver.find_element(By.ID, "list-option2").click()
            else:
                self.driver.find_element(By.ID, "list-option1").click()

            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox1"]').send_keys(self.handle_bank_number(int(info_one['transit_number'])))
            self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBox2"]').send_keys(int(info_one['account_number']))   # //*[@id="XRadioButtonPinAvailable"]
            self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        else:
            pass

        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        time.sleep(10)
        if self.is_exist("The IRS let us know that someone else has already filed with the same SSN as you."):
            # 记录失败信息
            logger.info(f"该ssn已经被使用，程序结束")
            raise SSNisUseException("SSN Error")
        time.sleep(10)
        if self.is_exist("If you need to change your SSNs:"):
            # 记录失败信息
            logger.info(f"该ssn已经被使用，程序结束")
            raise SSNisUseException("SSN Error")
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        try:
            self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonPinAvailable"]').click()

            # self.driver.find_element(By.XPATH, '/html/body/div[13]/div/div[4]/div[1]/div[3]/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/input').click()   //*[@id="XRadioButtonPinAvailable"]
        except:
            try:
                self.driver.find_element(By.XPATH, '/html/body/div[13]/div/div[4]/div[1]/div[3]/div[5]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div').click()
            except:
                self.driver.refresh()
                self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonPinAvailable"]').click()

        # Some questions about your tax and IRS history  //*[@id="XRadioButtonPinAvailable"]
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButton2"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="XRadioButtonNonMFJIdentityPinNo"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        #  Good news! Verifying just got easier
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()
        # Enter your driver’s license or state ID.
        self.driver.find_element(By.XPATH, '//*[@id="XCheckBoxcbTPUnwilling"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()

        self.driver.find_element(By.ID, "XFormatTextBoxTPPin").send_keys("93737")
        # //*[@id="PageFooter1"]/div/div/div[2]/a
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="PageFooter1"]/div/div/div[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        time.sleep(3)
        if not self.is_exist("All your hard work has paid off!"):
            try:
                self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            except:
                pass
        # 验证码  //*[@id="ac-image"]
        logger.info(f"开始识别验证码")
        count_while = 1
        while count_while < 10:
            ac_img = self.driver.find_element(By.XPATH, '//*[@id="ac-image"]')
            print(ac_img.location)
            src = ac_img.get_attribute('src')
            try:
                code = self.baidu_get_img_code(ac_img)
            except:
                code = None
            if code:
                logger.info(f"识别成功！验证码为：{code}")
                self.driver.find_element(By.XPATH, '//*[@id="ac-guess"]').send_keys(code)
                self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock1"]/a').click()
                logger.info(f"等待验证码识别完成...")
                time.sleep(20)
                # //*[@id="XFormatTextBlock1"]/a    //*[@id="ac-holder"]/div/button[2]  //*[@id="ac-guess"]

                if self.is_exist("Please try again."):
                    pass
                else:
                    logger.info(f"验证码识别完成...")

                    break
            count_while += 1
            self.driver.find_element(By.XPATH, '//*[@id="ac-holder"]/div/button[2]').click()
            time.sleep(2)
            logger.info(f"识别失败，开始重试：{count_while}")

        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()   #  //*[@id="btnNext"]  //*[@id="btnNext"]  //*[@id="liveForm"]/div/div[2]/neb-form-footer/div/div[1]/div/div/div/div/button[1]   //*[@id="XFormatTextBlock14"]/a
        # self.perform_selenium_operation()
        self.driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
        self.perform_selenium_operation()
        self.driver.find_element(By.XPATH, '//*[@id="XFormatTextBlock14"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="XHyperlink2"]').click()
        # TODO 记录到达最后一步

    def timeout_handler(self, signum, frame):
        raise TimeoutException("Selenium operation timed out")

    def perform_selenium_operation(self):
        try:
            # 在操作内设置自己的计时器
            signal.signal(signal.SIGALRM, self.timeout_handler)
            signal.alarm(10)  # 设置操作的超时时间为10秒

            # 执行 Selenium 操作
            # 如果操作超时，会触发 TimeoutException 异常
            self.driver.find_element(By.XPATH, '//*[@id="liveForm"]/div/div[2]/neb-form-footer/div/div[1]/div/div/div/div/button[1]').click()  # 示例操作：打开一个网页

            # 如果操作在规定时间内完成，取消超时计时器
            signal.alarm(0)
        except TimeoutException:
            print("Selenium operation timed out")

    def baidu_get_img_code(self, img_element, option=True, num=0):
        client = AipOcr(settings.APP_ID, settings.API_KEY, settings.SECRET_KEY)

        # 获取整个浏览器窗口的截图
        screenshot = self.driver.get_screenshot_as_png()

        # 打开截图并转换为Pillow Image对象
        img = Image.open(BytesIO(screenshot))
        # img.save("screenshot.png")
        # 获取第一张图片的位置和大小
        location = img_element.location
        size = img_element.size
        if self.is_exist("Please try again.") and option:
            img_file = img.crop((location["x"], location["y"]+92, location["x"] + size["width"], location["y"] + size["height"]+92))
        else:
            img_file = img.crop((location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"]))
        # image = get_file_content('image.png')
        # 调用通用文字识别（高精度版）
        file = BytesIO()
        img_file.save(file, format="png")
        res_image = client.basicAccurate(file.getvalue())
        if "words_result" not in res_image:
            return None
        result = ""
        for i in res_image["words_result"]:
            result += i["words"]
        if len(result) > 6 and num < 6:
            result = self.baidu_get_img_code(img_element, False, num+1)
        return result

    def get_img_code(self, url, img_element, option=True, num=1):
        logger.info(f"开始识别代码：{option, num}")

        # 获取整个浏览器窗口的截图
        screenshot = self.driver.get_screenshot_as_png()

        # 打开截图并转换为Pillow Image对象
        img = Image.open(BytesIO(screenshot))
        # img.save("screenshot.png")
        # 获取第一张图片的位置和大小
        location = img_element.location
        size = img_element.size
        print(size)
        # print(location)
        # # 剪切出图片部分并保存
        if self.is_exist("Please try again.") and option:
            img_file = img.crop((location["x"], location["y"]+92, location["x"] + size["width"], location["y"] + size["height"]+92))
        else:
            img_file = img.crop((location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"]))
        img_file.save("image.png")
        img_file = img_file.convert('L')
        # 增加对比度
        contrast = ImageEnhance.Contrast(img_file)
        img_file = contrast.enhance(4)
        threshold = 200
        img_file = img_file.point(lambda x: 0 if x < threshold else 255)
        img_file = img_file.filter(ImageFilter.MedianFilter(size=3))
        # img_file.show()
        code = pytesseract.image_to_string(img_file).strip()
        logger.info(f"识别代码为：{code}, 长度为{len(code)}")
        if len(code) > 6 and num < 6:
            self.get_img_code(url, img_element, False, num+1)
        return code

    def handle_date(self, birthday):
        try:
            date_of_birth = birthday.strftime("%m/%d/%Y")
            year = birthday.year
        except:
            date_of_birth = birthday
            if "/" in birthday:
                split_str = "/"
                time_info = birthday.split(split_str)
                year = int(time_info[-1])
            else:
                split_str = '-'
                time_info = birthday.split(split_str)
                date_of_birth = f"{time_info[1]}/{time_info[2]}/{time_info[0]}"
                year = int(time_info[0])
        age = ""
        if 2006 >= year >= 1996:
            age = "early"
        elif 1957 >= year >= 1930:
            age = "old"
        elif 1995 >= year >= 1958:
            age = "common"
        logger.info(f"检测到信息为：{age}")
        return date_of_birth, age

    def is_exist(self, str_to_find):
        # print(self.driver.page_source)
        if str_to_find in self.driver.page_source:
            logger.info(f"检测：{str_to_find}  在当前页面")
            return True
        logger.info(f"检测：{str_to_find}  不在当前页面")
        return False

    def handle_bank_number(self, code):
        code = str(code)
        num = 9 - len(code)
        for i in range(num):
            code = f"0{code}"
        return code

    def run(self, info_one):
        for i in range(6):
            try:
                self.home_to_create_an_account()
                break
            except:
                if i == 5:
                    raise TimeoutException("打开注册页面超时")
                pass
        info_email = info_one["邮箱----密码"]
        email, password = info_email.split("----")
        print(info_one["名"], info_one["姓"])
        # try:
        self.register_email(email, password, info_one["账号"], info_one["密码"], info_one["名"], info_one["姓"])
        # except Exception as e:
        #     logger.info("账号已存在，进入登录流程")
        #     self.home_to_login(info_one["账号"], info_one["密码"], email, password)
        ssn = str(int(info_one["社保号"]))
        if len(ssn) == 7:
            ssn = f"00{ssn}"
        elif len(ssn) == 8:
            ssn = f"0{ssn}"
        else:
            pass
        self.start_on_your_taxes()
        self.your_info(info_one["名"], info_one["姓"], info_one["生日"],
                       ssn, int(info_one["电话"]), info_one["街道"], int(info_one["邮编"]), info_one)
        return True


if __name__ == '__main__':
    # qrmhayfbsyc@hotmail.com CFQCPD76J
    operate = AutoOperate("127.0.0.1:59532")
    info_one, info_data = search_one_data()
    try:
        operate.run(info_one)
    except:
        import traceback
        traceback.print_exc()
        time.sleep(400)
    # operate.run(info_one)
    # operate.start_on_your_taxes()
    # operate.your_info(info_one["名"], info_one["姓"], info_one["生日"],
    #                    int(info_one["社保号"]), int(info_one["电话"]), info_one["街道"], int(info_one["邮编"]), info_one)
    date_of_birth, age = operate.handle_date(info_one["生日"])
    operate.start_w_2(int(info_one["邮编"]), info_one, age)
    operate.send_group(age, info_one["工作"], info_one)

    #
    # pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"
    # img_file = Image.open("image.png")
    # img_file = img_file.convert('L')
    # # 增加对比度
    # contrast = ImageEnhance.Contrast(img_file)
    # img_file = contrast.enhance(4)
    # threshold = 200
    # img_file = img_file.point(lambda x: 0 if x < threshold else 255)
    # img_file = img_file.filter(ImageFilter.MedianFilter(size=3))
    # img_file.show()
    # code = pytesseract.image_to_string(img_file)
    # print(code)
    # with open("1.png", "rb+") as e:
    #     result = e.read()
    # client = AipOcr(settings.APP_ID, settings.API_KEY, settings.SECRET_KEY)
    # res_image = client.basicAccurate(result)
    # print(res_image)
    # print(res_image["words_result"][0]["words"])
    # 程序运行失败：Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="XFormatTextBlock109"]/a"}