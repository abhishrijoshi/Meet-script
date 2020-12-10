#!/usr/bin/python3
import time 
import random
import re
from selenium import webdriver 

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
class Commenter:
   
  
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(750, 900)

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='identifier']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        
        user_name_elem.send_keys(Keys.RETURN)
        time.sleep(3)
        passwoword_elem = driver.find_element_by_xpath("//input[@jsname='YPqjbf']")
        passwoword_elem.clear()  
        passwoword_elem.send_keys(self.password)
        passwoword_elem.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.get("  Your_link  ")
        time.sleep(2)
        n = 7
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB * n)
        actions.perform()
        time.sleep(1)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.RETURN * 1)
        actions.perform()
        
com = Commenter(username=' ', password=' ')
com.login()
