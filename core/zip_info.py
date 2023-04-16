import requests
from lxml import etree


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
    href = ele.xpath('//div[@id="search-results"]//a/@href')[0]
    result = get_info(href)
    while not result:
        index += 1
        href = ele.xpath('//div[@id="search-results"]//a/@href')[index]
        result = get_info(href)
    return result


def get_info(href):
    url = f"http://search.sunbiz.org{href}"
    res = requests.get(url)
    ele = etree.HTML(res.text)
    emp_name = ele.xpath('//*[@id="maincontent"]/div[2]/div[1]/p[2]/text()')[0].strip()
    emp_number = ele.xpath('//*[@id="maincontent"]/div[2]/div[2]/span[2]/div/span[2]/text()')[0]
    if emp_number == "NONE":
        return None
    emp_address = ele.xpath('//*[@id="maincontent"]/div[2]/div[4]/span[2]/div/text()[1]')[0].strip()
    emp_address_zip = ele.xpath('//*[@id="maincontent"]/div[2]/div[4]/span[2]/div/text()[2]')[0].split(" ")[-1]
    return emp_name, emp_number, emp_address, emp_address_zip


if __name__ == '__main__':
    print(get_zip_info(77845))
