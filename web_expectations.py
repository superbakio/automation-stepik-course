from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
#import os

try:
     browser = webdriver.Chrome()
     #browser.implicitly_wait(5) # Webdriver will search every element during 5 seconds
     browser.get("http://suninjuly.github.io/explicit_wait2.html")
     #time.sleep(1)
     #button = browser.find_element_by_id("button")
     #button = browser.find_element_by_id("verify")
     #value = 100
     book = WebDriverWait(browser, 12)
     element = book.until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100"))
     book = browser.find_element_by_xpath ("//button[@id='book']")
     book.click()
     #message = browser.find_element_by_id("verify_message")
     #assert "successful" in message.text
     #button = WebDriverWait(browser, 5).until_not(
        #EC.element_to_be_clickable((By.ID, "verify"))
     #)
     #link = "http://suninjuly.github.io/redirect_accept.html"
     #browser = webdriver.Chrome()
     #browser.get(link)

     #confirm part
     #button = browser.find_element_by_xpath ("//button[@id='book']") # //button[@type="submit"]
     #button.click()
     #confirm = browser.switch_to.alert
     #confirm.accept()

     #switch to a new window
     #new_window = browser.window_handles[1]
     #browser.switch_to.window(new_window)
     #new_window = browser.window_handles[1]
     #first_window = browser.window_handles[0]

     
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

     #first = browser.find_element_by_xpath("//input[@name='firstname']")
     #first.send_keys("Yevhen")
     #last = browser.find_element_by_xpath("//input[@name='lastname']")
     #last.send_keys("Sobianin")
     #email = browser.find_element_by_xpath("//input[@name='email']")
     #email.send_keys("YevhenSobianin@gmail.com")
     #alert = browser.switch_to.alert
     #alert_text = alert.text
     #alert.accept()
     #confirm = browser.switch_to.alert
     #confirm.accept()
     #confirm.dismiss()
     #prompt = browser.switch_to.alert
     #prompt.send_keys("My answer")
     #prompt.accept()
     #alert = browser.switch_to.alert
     #alert_text = alert.text
     #addToClipBoard = alert_text.split(': ')[-1]
     #pyperclip.copy(addToClipBoard)
     #current_dir = os.path.abspath(os.path.dirname(__file__))  
     #file_path = os.path.join(current_dir, 'test.txt')
     #element = browser.find_element_by_xpath("//input[@id='file']").send_keys(file_path)
     #current_dir = os.path.abspath(os.path.dirname(__file__))  
     #file_path = os.path.join(current_dir, 'test.txt')
     #element.send_keys(file_path)   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
     time.sleep(5)
    # закрываем браузер после всех манипуляций
     browser.quit()


    







    



