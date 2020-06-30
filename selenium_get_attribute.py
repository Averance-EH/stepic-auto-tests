from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/get_attribute.html')

	chest = browser.find_element_by_id('treasure')
	chest_val = chest.get_attribute('valuex')
	x = chest_val
	y = calc(x)

	input1 = browser.find_element_by_id('answer')
	input1.send_keys(y)

	checkb = browser.find_element_by_id('robotCheckbox')
	checkb.click()

	radio = browser.find_element_by_id('robotsRule')
	radio.click()

	button = browser.find_element_by_class_name('btn')
	button.click()

finally:
	time.sleep(30)
	browser.quit()
