from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time

driver = webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://202.205.80.9/0.htm")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# form = soup.select("form")[1] # what's different with findAll
# print(form)
# form = soup.findAll('form')[1] # the two ouput are exactly the same
# print(form)

# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm (from ClientForm).
"""
# the driver_form can't receive the form's data , Complete failure
form = soup.select("form")[1]
form.find("input", {"name": "DDDDD"})["value"] = "1309090220"
form.find("input", {"name": "upass"})["value"] = "yy175173"
form.find("input", {"name": "0MKKey"})["value"] = ""
driver_form = driver.find_element_by_name("form1")
driver_form.submit()
"""

form = driver.find_element_by_name("form1")
driver.find_element_by_xpath('//form[@name="form1"]/input[1]').send_keys('1309090220')
driver.find_element_by_xpath('//form[@name="form1"]/input[2]').send_keys('yy175173')
driver.find_element_by_xpath('//form[@name="form1"]/input[3]').send_keys('')
# driver.find_element_by_xpath('//input[@value = "Submit"]').click()
form.submit()

time.sleep(3)

print(driver.find_element_by_name("form1").text)

driver.close()

