# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from ads_power.auto_operate import AutoOperate


class Test(AutoOperate):

    def test_(self):
        # self.driver.get("https://www.hrblock.com/")
        # self.driver.set_window_size(1263, 1012)
        # self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        # element = self.driver.find_element(By.LINK_TEXT, "Sign in")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # self.driver.find_element(By.CSS_SELECTOR, ".btn--transparent-black > .btn-label").click()
        # self.driver.find_element(By.ID, "x1e97441e").click()
        # self.driver.find_element(By.ID, "x1e97441e").send_keys("dahykj@hotmail.com")
        # self.driver.find_element(By.ID, "smvy5kvc0__label").click()
        # self.driver.find_element(By.ID, "smvy5kvc0").send_keys("dahykj")
        # self.driver.find_element(By.CSS_SELECTOR, "#showhideNew rect").click()
        # self.driver.find_element(By.ID, "uga1ar1yc__label").click()
        # self.driver.find_element(By.ID, "uga1ar1yc").send_keys("unRekQY8Eu1Aa!")
        # self.driver.find_element(By.ID, "pfc5y4dic").click()
        # self.driver.find_element(By.ID, "pfc5y4dic").send_keys("unRekQY8Eu1Aa!")
        # self.driver.find_element(By.CSS_SELECTOR, ".mobCheck .hrb-checkbox__checkmark").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".float-left .hrb-checkbox__checkmark").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#submitButton .hrb-button__container").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, "#submitButton .hrb-button__container")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mb-sp-32 .link-text").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".hero-content")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".hero-content").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#imbPsBtnFour .hrb-text--body-copy-small").click()
        self.driver.find_element(By.CSS_SELECTOR, "#imbPsNext .hrb-button__text").click()
        self.driver.find_element(By.ID, "Run2").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.LINK_TEXT, "Yes, use Free").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").click()
        element = self.driver.find_element(By.ID, "XFormatTextBoxTPFullName")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "XFormatTextBoxTPFullName")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "XFormatTextBoxTPFullName")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").click()
        element = self.driver.find_element(By.ID, "XFormatTextBoxTPFullName")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").send_keys("john	")
        self.driver.find_element(By.ID, "XFormatTextBoxTPCurrentDate").click()
        element = self.driver.find_element(By.ID, "XFormatTextBoxTPFullName")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "XFormatTextBoxTPFullName")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "XFormatTextBoxTPFullName")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").click()
        element = self.driver.find_element(By.ID, "XFormatTextBoxTPFullName")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").send_keys("john")
        self.driver.find_element(By.ID, "Run20").click()
        self.driver.find_element(By.ID, "mainContents").click()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        element = self.driver.find_element(By.ID, "Run6")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "XFormatTextBoxTPCurrentDate").click()
        self.driver.find_element(By.ID, "insText_id51").click()
        self.driver.find_element(By.ID, "insText_id51").click()
        self.driver.find_element(By.ID, "insText_id51").click()
        element = self.driver.find_element(By.ID, "insText_id51")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "insText_id51").click()
        self.driver.find_element(By.ID, "insText_id51").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPCurrentDate").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPCurrentDate").send_keys("04/16/2023")
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").send_keys("john jones")
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.ID, "XLineBreak2").click()
        self.driver.find_element(By.ID, "Run7").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "XFormatTextBoxfirst_t").click()
        self.driver.find_element(By.ID, "XFormatTextBoxfirst_t").click()
        self.driver.find_element(By.ID, "XFormatTextBoxfirst_t").send_keys("john")
        self.driver.find_element(By.ID, "XFormatTextBoxlast_t").click()
        self.driver.find_element(By.ID, "XFormatTextBoxlast_t").send_keys("jones")
        self.driver.find_element(By.ID, "XFormatTextBoxdob_t").click()
        self.driver.find_element(By.ID, "XFormatTextBoxdob_t").click()
        self.driver.find_element(By.ID, "XFormatTextBoxdob_t").send_keys("12/31/1952")
        self.driver.find_element(By.ID, "XListBoxxmaritalStatus-shdo").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span6:nth-child(2) #list-option1").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPSSN").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPSSN").send_keys("***-**-****")
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".rightArrow")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "XFormatTextBoxTpDayPhone").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTpDayPhone").send_keys("207-668-5215")
        self.driver.find_element(By.CSS_SELECTOR, "#ShowHidePanelDomesticAddress .span8").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPAddress").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPAddress").send_keys("1251 n massasoit")
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPZip").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPZip").send_keys("60637")
        self.driver.find_element(By.CSS_SELECTOR, "#ShowHidePanelDomesticAddress .span8").click()
        self.driver.find_element(By.ID, "Run21").click()
        self.driver.find_element(By.ID, "XRadioButtonrblOtherResidentStateY").click()
        self.driver.find_element(By.CSS_SELECTOR, "#ShowHidePanelshpAllYear > div > .row-fluid:nth-child(2)").click()
        self.driver.find_element(By.ID, "mainContents").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        element = self.driver.find_element(By.LINK_TEXT, "Let\'s Go")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".span10 > .nextButton > span:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".yes .binaryradiolabel").click()
        self.driver.find_element(By.ID, "Run1").click()
        self.driver.find_element(By.CSS_SELECTOR, ".binaryradiolabel > .hrbo-icon-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".no .binaryradiolabel").click()
        self.driver.find_element(By.CSS_SELECTOR, ".no label").click()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#XHyperlink1 > .icon")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span10 > .nextButton > span:nth-child(1)").click()
        element = self.driver.find_element(By.LINK_TEXT, "Start Now")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".buttonStyle > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.LINK_TEXT, "Start Now").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span4:nth-child(3) #cardContentPanel").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span4:nth-child(3) #cardActionPanel span").click()
        self.driver.find_element(By.ID, "XFormatTextBoxbb1").click()
        element = self.driver.find_element(By.ID, "XFormatTextBoxbc_ename")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "fieldset:nth-child(4) > div > .row-fluid:nth-child(2) > .span6:nth-child(1) > .formFieldBox")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "fieldset:nth-child(4) > div > .row-fluid:nth-child(2) > .span6:nth-child(1) > .formFieldBox").click()
        self.driver.find_element(By.ID, "XFormatTextBoxbc_ename").send_keys("34TH TERRACE, LLC")
        self.driver.find_element(By.ID, "XFormatTextBoxbb1").click()
        self.driver.find_element(By.ID, "XFormatTextBoxbb1").send_keys("20-2206720")
        self.driver.find_element(By.ID, "XFormatTextBoxbc_eaddress").click()
        self.driver.find_element(By.ID, "XFormatTextBoxbc_eaddress").send_keys("6337 KIMBARK")
        self.driver.find_element(By.ID, "XFormatTextBoxBC_EZIP").click()
        self.driver.find_element(By.ID, "XFormatTextBoxBC_EZIP").send_keys("60637")
        self.driver.find_element(By.ID, "mainContents").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_wages").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_wages").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_wages").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_wages").send_keys("4000")
        self.driver.find_element(By.ID, "XFormatTextBoxW2_SS_wages").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_SS_wages").send_keys("4000")
        self.driver.find_element(By.ID, "XFormatTextBoxW2_Medicare_wages").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_Medicare_wages").send_keys("4000")
        self.driver.find_element(By.ID, "XFormatTextBoxW2_SS_WH").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_SS_WH").send_keys("248")
        self.driver.find_element(By.ID, "XFormatTextBoxW2_Medicare_WH").send_keys("58")
        self.driver.find_element(By.ID, "XListBox3-shdo").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span3 #list-option15").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > .span5").click()
        self.driver.find_element(By.ID, "XFormatTextBox5").click()
        self.driver.find_element(By.ID, "XFormatTextBox5").send_keys("4000")
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_Fed_WH").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_Fed_WH").send_keys("0")
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        element = self.driver.find_element(By.ID, "_id25")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".rightArrow")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row-fluid:nth-child(3) > .span10").click()
        self.driver.find_element(By.ID, "primaryOccupation").click()
        self.driver.find_element(By.ID, "ui-id-5").click()
        self.driver.find_element(By.ID, "primaryOccupation").send_keys("Sales")
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "Run5").click()
        self.driver.find_element(By.CSS_SELECTOR, ".binaryradiolabel > .hrbo-icon-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".no label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 > .nextButton > span:nth-child(1)").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.find_element(By.ID, "mainContentsBoxBorder").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.ID, "mainContents").click()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 > .nextButton > span:nth-child(1)").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.find_element(By.ID, "Run8").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 > .nextButton > span:nth-child(1)").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .row-fluid:nth-child(4)").click()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, "#pageBodyInnerDiv .row-fluid:nth-child(5)").click()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".buttonStyle > span").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, "#TextBlock10 span").click()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#StackPanelstateTransferPod .span12").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_id15769544 > .file").click()
        self.driver.find_element(By.CSS_SELECTOR, "#lottieParent .span12").click()
        self.driver.find_element(By.CSS_SELECTOR, ".buttonStyle > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".buttonStyle > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#XFormatTextBlock109 span:nth-child(1)").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "TextBlockNextButtonText").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".footerRowDebugLinks").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span5 div:nth-child(3) .labelContainer").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span5 div:nth-child(3) .labelContainer").click()
        self.driver.find_element(By.ID, "Run9").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".rightButtons").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".yes label").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "div:nth-child(2) > .row-fluid div:nth-child(2) .labelContainer").click()
        self.driver.find_element(By.ID, "Run3").click()
        self.driver.find_element(By.ID, "XRadioButtonNonMFJIdentityPinNo").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span6 span:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".span6 span:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "TextBlock24").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".span10 span:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.LINK_TEXT, "Next")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.ID, "XFormatTextBoxTPPin").click()
        self.driver.find_element(By.CSS_SELECTOR, ".formFieldBox").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPPin").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPPin").send_keys("93737")
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.find_element(By.ID, "btnBack").click()
        element = self.driver.find_element(By.ID, "btnBack")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "XFormatTextBoxTPPin").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span2 > .nextButton > span:nth-child(1)").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "ac-guess").click()
        self.driver.find_element(By.ID, "ac-guess").send_keys("514393")
        self.driver.find_element(By.LINK_TEXT, "E-FILE RETURN").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".secondaryButtonStyle:nth-child(1) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.LINK_TEXT, "No, I’m not interested")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.LINK_TEXT, "No, I’m not interested").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        element = self.driver.find_element(By.ID, "Run9")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "XHyperlink2")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "Run11")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "XHyperlink2").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.ID, "TextBlock10").click()
        self.driver.find_element(By.ID, "XFormatTextBlock10").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row-fluid:nth-child(3) > .span12").click()
        self.driver.find_element(By.ID, "XHyperlink2").click()
        self.driver.find_element(By.ID, "btnBack").click()
        element = self.driver.find_element(By.ID, "btnBack")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("window.scrollTo(0,214.44444274902344)")
        self.driver.find_element(By.ID, "XFormatTextBlock12").click()
