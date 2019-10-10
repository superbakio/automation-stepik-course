from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
#import os

try:
     browser = webdriver.Chrome()
     browser.get("http://suninjuly.github.io/explicit_wait2.html")
     book = WebDriverWait(browser, 12)
     element = book.until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100"))
     book = browser.find_element_by_xpath ("//button[@id='book']")
     book.click()    
     #next page
     def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
     x_element = browser.find_element_by_xpath("//span[@id='input_value']")
     x = x_element.text
     y = calc(x)
     answer = browser.find_element_by_id("answer")
     answer.send_keys(y)
     button = browser.find_element_by_id("solve")
     browser.execute_script("window.scrollBy(0, 100);", button)
     button.click()
 
finally:
     time.sleep(5)
     browser.quit()

     


    







    



