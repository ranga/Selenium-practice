from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class OpenLid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://openlibrary.org/"
        self.verificationErrors = []
    
    def test_bad_user(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rangaranga")
        driver.find_element_by_name("login").click()

        body = driver.find_element_by_tag_name("body")
        error = "The username you entered isn't in the Open Library system. Please try again?"
        self.assertTrue(error in body.text)

    def test_bad_password(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("anand")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("anand123")
        driver.find_element_by_name("login").click()

        body = driver.find_element_by_tag_name("body")
        error = "That password seems incorrect."
        self.assertTrue(error in body.text)

    def test_fortgot_password(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_link_text("Forgotten your username or password").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("crangaranga@gmail.com")
        driver.find_element_by_name("sendit").click()
	
	error_elem = driver.find_element_by_class_name("invalid")
	error = "No user registered with this email address"
	self.assertTrue(error in error_elem.text)        
    
    def test_signup(self):
        driver = self.driver
        driver.get(self.base_url + "/")
    	driver.find_element_by_link_text("Sign Up").click()
        driver.find_element_by_id("displayname").clear()
        driver.find_element_by_id("username").send_keys("rangaranga")
        driver.find_element_by_id("displayname").clear()
        driver.find_element_by_id("displayname").send_keys("Rangarao")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("kingston")
        driver.find_element_by_id("emailAddr").clear()
        driver.find_element_by_id("emailAddr").send_keys("crangaranga@gmail.com")
        driver.find_element_by_xpath("//button[@id='signup']").click()
        driver.find_element_by_id("agreement").click()
    
        body = driver.find_element_by_tag_name("body")
        error = "Hi, Rangarao!"
        self.assertTrue(error in body.text)    


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
