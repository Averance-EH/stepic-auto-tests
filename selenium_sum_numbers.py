from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/selects1.html')

	x1_element = browser.find_element_by_id('num1')
	x2_element = browser.find_element_by_id('num2')

	x1 = x1_element.text
	x2 = x2_element.text

	result = str(int(x1)+int(x2))

	select = Select(browser.find_element_by_tag_name('select'))
	select.select_by_value(result)

	button = browser.find_element_by_class_name('btn')
	button.click()

finally:
	time.sleep(30)
	browser.quit()