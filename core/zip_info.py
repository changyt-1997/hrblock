import time

import requests
from lxml import etree
from selenium.webdriver.common.by import By
from seleniumwire import webdriver


def get_zip_info(code):
    """
    http://search.sunbiz.org/Inquiry/CorporationSearch/SearchResultDetail?inquirytype=ZipCode&directionType=Initial&searchNameOrder=CREATIVEDESIGNRESOLUTIONS%20F190000014730&aggregateId=forp-f19000001473-a8792b53-e434-433a-90fd-3814f5add5b3&searchTerm=20722&listNameOrder=CREATIVEDESIGNRESOLUTIONS%20F190000014730

    :param code:
    :return:
    """
    url = f"http://search.sunbiz.org/Inquiry/CorporationSearch/SearchResults?inquiryType=ZipCode&searchTerm={code}"
    res = requests.get(url)
    ele = etree.HTML(res.text)
    index = 0
    try:
        href = ele.xpath('//div[@id="search-results"]//a/@href')[0]
        result = get_info(href)
    except:
        result = None
    while not result:
        index += 1
        try:
            href = ele.xpath('//div[@id="search-results"]//a/@href')[index]
            result = get_info(href)
        except:
            result = None
        if index > 4:
            return None
    return result


def get_info(href):
    url = f"http://search.sunbiz.org{href}"
    res = requests.get(url)
    ele = etree.HTML(res.text)
    emp_name = ele.xpath('//*[@id="maincontent"]/div[2]/div[1]/p[2]/text()')[0].strip()
    emp_number = ele.xpath('//*[@id="maincontent"]/div[2]/div[2]/span[2]/div/span[2]/text()')[0]
    if emp_number == "NONE":
        return None, None, None, None
    emp_address = ele.xpath('//*[@id="maincontent"]/div[2]/div[4]/span[2]/div/text()[1]')[0].strip()
    emp_address_zip = ele.xpath('//*[@id="maincontent"]/div[2]/div[4]/span[2]/div/text()[2]')[0].split(" ")[-1]
    return emp_name, emp_number, emp_address, emp_address_zip


def get_ein_info(code):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    js = "window.open('https://www.hipaaspace.com/ein/ein_verification/', '_blank')"
    driver.execute_script(js)
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element(By.XPATH, '//*[@id="tbxSearchRequest"]').send_keys(code)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="Healthcare_Codes_Search_Results"]/div[1]/div[1]/a').click()
    emp_number = driver.find_element(By.XPATH, '//*[@id="masterForm"]/div[3]/div/div/main/div/div[10]/div[1]/table/tbody/tr[2]/td[2]/strong').text
    emp_name = driver.find_element(By.XPATH, '//*[@id="masterForm"]/div[3]/div/div/main/div/div[10]/div[1]/table/tbody/tr[4]/td[2]/strong').text
    emp_address = driver.find_element(By.XPATH, '//*[@id="masterForm"]/div[3]/div/div/main/div/div[10]/div[1]/table/tbody/tr[14]/td[2]/strong').text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return emp_name, emp_number, emp_address


if __name__ == '__main__':
    # print(get_zip_info(77845))
    print(get_ein_info(61738))