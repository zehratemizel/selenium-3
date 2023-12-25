from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
import pytest


class Test_Case_Homework2:
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 

    def teardown_method(self):
        self.driver.quit()


    @pytest.mark.parametrize("username,password",[("1","secret_sauce"),("locked_out_user","1"),("1","1")])
    def test_invalid_login(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_valid_remove(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.execute_script("window.scrollTo(0,500)") 
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-onesie']")))
        addToCart.click()
        cartControl = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        cartControl.click()
        remove = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='remove-sauce-labs-onesie']")))
        assert remove.text == "Remove"
 
    

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_valid_purchase(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.execute_script("window.scrollTo(0,500)") 
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-fleece-jacket']")))
        addToCart.click()
        cartControl = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        cartControl.click()
        successCheckout = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='checkout']")))
        successCheckout.click()
        firstnameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        firstnameInput.send_keys("Zehra")
        lastnameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"last-name")))
        lastnameInput.send_keys("Temizel")
        postalcodeInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"postal-code")))
        postalcodeInput.send_keys("3344")  
        successContinue = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='continue']")))
        successContinue.click()
        successFinish = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='finish']")))
        successFinish.click()
        finishMessage = self.driver.find_element(By.XPATH,"//*[@id='checkout_complete_container']/h2")
        assert finishMessage.text == "Thank you for your order!"




    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_valid_checkout(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.execute_script("window.scrollTo(0,500)") 
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-fleece-jacket']")))
        addToCart.click()
        cartControl = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        cartControl.click()
        successCheckout = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='checkout']")))
        successCheckout.click()
        finishMessage1 = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span")
        assert finishMessage1.text == "Checkout: Your Information"
 
    
