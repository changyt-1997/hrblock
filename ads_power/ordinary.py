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
        # self.driver.find_element(By.CSS_SELECTOR, ".padding-bottom-100").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".btn > .icon-svg").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".btn > .icon-svg")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # self.driver.find_element(By.LINK_TEXT, "Create Account").click()
        # self.driver.find_element(By.ID, "rvrhxxz9k").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".single-col-form__card").click()
        # self.driver.find_element(By.ID, "rvrhxxz9k").send_keys("eqsectp@hotmail.com")
        # self.driver.find_element(By.ID, "x90l7ffw3").click()
        # self.driver.find_element(By.ID, "x90l7ffw3").click()
        # self.driver.find_element(By.ID, "x90l7ffw3").click()
        # element = self.driver.find_element(By.ID, "x90l7ffw3")
        # actions = ActionChains(self.driver)
        # actions.double_click(element).perform()
        # self.driver.find_element(By.ID, "x90l7ffw3").send_keys("eqsectp231")
        # self.driver.find_element(By.CSS_SELECTOR, "#showhideNew .hrb-button__container").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, "#showhideNew .hrb-button__container")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # self.driver.find_element(By.ID, "qifm5zo57").click()
        # self.driver.find_element(By.ID, "qifm5zo57").send_keys("Qwe123321..")
        # self.driver.find_element(By.ID, "xvi1w04h3").click()
        # self.driver.find_element(By.ID, "xvi1w04h3").send_keys("Qwe123321..")
        # self.driver.find_element(By.CSS_SELECTOR, ".mobCheck .hrb-checkbox__checkmark").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".float-left .hrb-checkbox__checkmark").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#submitButton .hrb-button__text").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, "#submitButton .hrb-button__text")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".mb-sp-32 .link-text").click()
        self.driver.find_element(By.CSS_SELECTOR, ".boot-content-wrapper").click()
        self.driver.find_element(By.CSS_SELECTOR, "#imbPsBtnFour .hrb-text--body-copy-small").click()
        self.driver.find_element(By.CSS_SELECTOR, "#imbPsNext .hrb-button__container").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.execute_script("window.scrollTo(0,0)")
        element = self.driver.find_element(By.LINK_TEXT, "Yes, use Free")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "Yes, use Free").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").send_keys("Carrie	Schultz")
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".row-fluid:nth-child(4) > .span5:nth-child(2) > .formFieldBox").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".row-fluid:nth-child(4) > .span5:nth-child(2) > .formFieldBox").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".row-fluid:nth-child(4) > .span5:nth-child(2) > .formFieldBox")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "insText_id242").click()
        self.driver.find_element(By.ID, "insText_id242").click()
        element = self.driver.find_element(By.ID, "insText_id242")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "insText_id242").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPCurrentDate").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPCurrentDate").send_keys("04/16/2023")
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
        self.driver.find_element(By.ID, "XFormatTextBoxTPFullName").send_keys("Carrie Schultz")
        self.driver.find_element(By.ID, "Run20").click()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.ID, "XLineBreak2").click()
        self.driver.find_element(By.ID, "Run7").click()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "XFormatTextBoxfirst_t").click()
        self.driver.find_element(By.ID, "XFormatTextBoxfirst_t").send_keys("Carrie")
        self.driver.find_element(By.ID, "XFormatTextBoxlast_t").click()
        self.driver.find_element(By.ID, "XFormatTextBoxlast_t").send_keys("Schultz")
        self.driver.find_element(By.ID, "XFormatTextBoxdob_t").click()
        self.driver.find_element(By.ID, "XFormatTextBoxdob_t").send_keys("04/03/1973")
        self.driver.find_element(By.ID, "XListBoxxmaritalStatus-shdo").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span6:nth-child(2) #list-option1").click()
        self.driver.find_element(By.CSS_SELECTOR, ".rightArrow").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".rightArrow")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".clearfix").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPSSN").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPSSN").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPSSN").send_keys("***-**-****")
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTpDayPhone").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTpDayPhone").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTpDayPhone").send_keys("203-560-2013")
        self.driver.find_element(By.CSS_SELECTOR, "#ShowHidePanelDomesticAddress .span8").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPAddress").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPAddress").send_keys("2126 Rolling Rock Pl")
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPZip").click()
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPZip").send_keys("77845")
        self.driver.find_element(By.ID, "XFormatTextBoxtbTPAddress").click()
        self.driver.find_element(By.CSS_SELECTOR, "#ShowHidePanelDomesticAddress .span8").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#ShowHidePanelshpAllYear > div > .row-fluid .listBoxWrap > div:nth-child(1) .formFieldBox").click()
        self.driver.find_element(By.ID, "XRadioButtonrblOtherResidentStateY").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".span10 > .nextButton > span:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".span10 > .nextButton > span:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".yes .binaryradiolabel").click()
        element = self.driver.find_element(By.ID, "XRadioButtonrbSingleStatusY")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "Run1").click()
        self.driver.find_element(By.CSS_SELECTOR, ".binaryradiolabel > .hrbo-icon-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".no .binaryradiolabel").click()
        self.driver.find_element(By.CSS_SELECTOR, ".no .binaryradiolabel").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.LINK_TEXT, "Let’s Go").click()
        self.driver.find_element(By.LINK_TEXT, "Start Now").click()
        self.driver.find_element(By.LINK_TEXT, "Enter manually").click()
        self.driver.find_element(By.ID, "XFormatTextBoxbc_ename").click()
        self.driver.find_element(By.ID, "XFormatTextBoxbc_ename").send_keys("ADAM BANK GROUP, INC.")
        self.driver.find_element(By.ID, "XFormatTextBoxbb1").click()
        self.driver.find_element(By.ID, "XFormatTextBoxbb1").send_keys("35-2274945")
        self.driver.find_element(By.ID, "XFormatTextBoxbc_eaddress").click()
        self.driver.find_element(By.ID, "XFormatTextBoxbc_eaddress").send_keys("ONE MOMENTUM BOULEVARD")
        self.driver.find_element(By.ID, "XFormatTextBoxBC_EZIP").click()
        self.driver.find_element(By.ID, "XFormatTextBoxBC_EZIP").send_keys("1000")
        self.driver.find_element(By.ID, "XFormatTextBoxBC_EZIP").click()
        self.driver.find_element(By.ID, "XFormatTextBoxBC_EZIP").click()
        element = self.driver.find_element(By.ID, "XFormatTextBoxBC_EZIP")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "XFormatTextBoxBC_EZIP").send_keys("77845")
        self.driver.find_element(By.CSS_SELECTOR, "#ShowHidePanelDOMEMPLOYERADDR2 .span12").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "fieldset:nth-child(6) > div:nth-child(2) > .row-fluid:nth-child(1) > .span6:nth-child(1)").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_wages").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_wages").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_wages").click()
        element = self.driver.find_element(By.ID, "XFormatTextBoxW2_wages")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_wages").send_keys("4000")
        self.driver.find_element(By.ID, "XFormatTextBoxW2_SS_wages").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_SS_wages").send_keys("4000")
        self.driver.find_element(By.ID, "XFormatTextBoxW2_Medicare_wages").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_Medicare_wages").send_keys("4000")
        self.driver.find_element(By.ID, "XFormatTextBoxW2_Fed_WH").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_Fed_WH").send_keys("0")
        self.driver.find_element(By.ID, "XFormatTextBoxW2_SS_WH").click()
        self.driver.find_element(By.ID, "XFormatTextBoxW2_SS_WH").send_keys("248")
        self.driver.find_element(By.ID, "XFormatTextBoxW2_Medicare_WH").send_keys("58")
        self.driver.find_element(By.ID, "XListBox3-shdo").click()
        self.driver.find_element(By.CSS_SELECTOR, ".dgTableBaseDiv #list-option47").click()
        self.driver.find_element(By.ID, "XFormatTextBox5").click()
        self.driver.find_element(By.ID, "XFormatTextBox5").send_keys("4000")
        self.driver.find_element(By.CSS_SELECTOR, ".rightArrow:nth-child(2)").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "primaryOccupation").click()
        self.driver.find_element(By.ID, "ui-id-5").click()
        self.driver.find_element(By.ID, "primaryOccupation").send_keys("Sales")
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".no .binaryradiolabel").click()
        self.driver.find_element(By.CSS_SELECTOR, ".no .binaryradiolabel").click()
        self.driver.find_element(By.CSS_SELECTOR, ".binaryradiolabel > .hrbo-icon-close").click()
        element = self.driver.find_element(By.LINK_TEXT, "Next")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".span12 > .nextButton > span:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        element = self.driver.find_element(By.LINK_TEXT, "Next")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".nextButton:nth-child(2) > span:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .span12 > .formFieldBox").click()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .span12 > .formFieldBox").click()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .span12 > .formFieldBox").click()
        self.driver.find_element(By.ID, "Run9").click()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".rightArrow")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .row-fluid:nth-child(4)").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.ID, "mainContents").click()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, "#TextBlock10 span").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_id73643007 > .file").click()
        self.driver.find_element(By.LINK_TEXT, "Finish up").click()
        self.driver.find_element(By.CSS_SELECTOR, "#XFormatTextBlock109 span:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".rightArrow").click()
        self.driver.find_element(By.ID, "TextBlockNextButtonText").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#StackPanelRefundOptionsForNonRT > .listBoxWrap > div:nth-child(1) .labelContainer").click()
        self.driver.find_element(By.ID, "Run5").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 h3").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#ShowHidePanelPAYMENT_METHOD .row-fluid:nth-child(2) > .span12").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 h3").click()
        self.driver.find_element(By.ID, "XFormatTextBlockRefundAmount").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 h3").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 h3").click()
        self.driver.find_element(By.CSS_SELECTOR, "#StackPanelRefundOptionsForNonRT div:nth-child(1) > .span12").click()
        self.driver.find_element(By.ID, "mainContentsBox").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 h3").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 h3").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 h3").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span12 h3").click()
        self.driver.find_element(By.ID, "mainContents").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span6 > .nextButton > span:nth-child(1)").click()
        self.driver.find_element(By.ID, "XFormatTextBox1").click()
        element = self.driver.find_element(By.ID, "XFormatTextBox1")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "XFormatTextBox1")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "XFormatTextBox1")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "XFormatTextBox1").click()
        self.driver.find_element(By.ID, "XFormatTextBox1").send_keys("124085299")
        self.driver.find_element(By.CSS_SELECTOR, "#XLabelRouting\\ transit\\ number__Label > span").click()
        self.driver.find_element(By.CSS_SELECTOR, "thead .span3:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span3:nth-child(1) > .tableHeaderStyle").click()
        self.driver.find_element(By.ID, "XFormatTextBox1").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span3:nth-child(1) > .tableHeaderStyle").click()
        self.driver.find_element(By.ID, "XFormatTextBox2").click()
        self.driver.find_element(By.ID, "XFormatTextBox2").click()
        self.driver.find_element(By.ID, "XFormatTextBox2").send_keys("3392914")
        self.driver.find_element(By.ID, "XListBox1-shdo").click()
        self.driver.find_element(By.ID, "list-option2").click()
        self.driver.find_element(By.ID, "XListBox1-shdo").click()
        self.driver.find_element(By.ID, "list-option1").click()
        self.driver.find_element(By.ID, "XListBox1-shdo").click()
        self.driver.find_element(By.ID, "list-option1").click()
        self.driver.find_element(By.ID, "XListBox1-shdo").click()
        self.driver.find_element(By.ID, "list-option2").click()
        self.driver.find_element(By.ID, "XListBox1-shdo").click()
        self.driver.find_element(By.ID, "list-option2").click()
        self.driver.find_element(By.CSS_SELECTOR, "thead .span2:nth-child(4)").click()
        self.driver.find_element(By.ID, "XFormatTextBox3").click()
        self.driver.find_element(By.ID, "XFormatTextBox3").click()
        self.driver.find_element(By.ID, "XListBox1-shdo").click()
        self.driver.find_element(By.ID, "XFormatTextBox3").click()
        self.driver.find_element(By.ID, "XFormatTextBox3").click()
        self.driver.find_element(By.ID, "XFormatTextBox3").send_keys("308")
        self.driver.find_element(By.ID, "TextBlock2").click()
        self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").click()
        self.driver.find_element(By.ID, "TextBlock2").click()
        self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").click()
        self.driver.find_element(By.ID, "TextBlock2").click()
        self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").click()
        self.driver.find_element(By.ID, "XFormatTextBox3").click()
        self.driver.find_element(By.ID, "XFormatTextBox3").click()
        element = self.driver.find_element(By.ID, "XFormatTextBox3")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#pageBodyInnerDiv div:nth-child(2) > .row-fluid > .span12").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "XFormatTextBox1").click()
        self.driver.find_element(By.ID, "XFormatTextBox1").send_keys("124085299")
        self.driver.find_element(By.ID, "XFormatTextBox2").click()
        self.driver.find_element(By.ID, "XFormatTextBox2").send_keys("3392914")
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "mainContents").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".yes label").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "div:nth-child(2) > .row-fluid div:nth-child(2) .formFieldBox").click()
        self.driver.find_element(By.ID, "Run3").click()
        self.driver.find_element(By.ID, "XRadioButtonNonMFJIdentityPinNo").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span6 span:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".span6 span:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "TextBlock24").click()
        self.driver.find_element(By.CSS_SELECTOR, ".span10 span:nth-child(1)").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.ID, "XFormatTextBoxTPPin").click()
        self.driver.find_element(By.ID, "XFormatTextBoxTPPin").send_keys("93737")
        self.driver.find_element(By.LINK_TEXT, "Next").click()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.ID, "ac-holder").click()
        element = self.driver.find_element(By.ID, "ac-guess")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "awesome-captcha")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "awesome-captcha").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#menu_id212727973 > .federal")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "awesome-captcha").click()
        self.driver.find_element(By.ID, "ac-guess").click()
        self.driver.find_element(By.ID, "ac-guess").send_keys("428518")
        self.driver.find_element(By.LINK_TEXT, "E-FILE RETURN").click()
        self.driver.find_element(By.ID, "btnNext").click()
        element = self.driver.find_element(By.ID, "btnNext")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "btnNext").click()
        self.driver.find_element(By.LINK_TEXT, "No, I’m not interested").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row-fluid:nth-child(1) > .span6").click()
        self.driver.find_element(By.ID, "XHyperlink1").click()


if __name__ == '__main__':
    test_ = Test("127.0.0.1:56748")
    # test_.home_to_create_an_account()
    # test_.register_email()
    test_.test_()