import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from pageObjects.shoppingPage import shopping
from utilities.readProperties import ReadConfig
from selenium.webdriver.support import expected_conditions as EC


class Test_002_Shopping:
    baseURL = ReadConfig.getApplicationURL()
    userEmail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    firstName = ReadConfig.getFirstName()
    lastName = ReadConfig.getLastName()
    zip = ReadConfig.getZip()

    @pytest.mark.regression
    def testShopping(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.userEmail)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
        else:
            self.driver.close()
            assert False
        self.sp = shopping(self.driver)
        self.sp.addToCart()
        self.sp.clickCart()
        self.sp.clickCheckout()
        self.sp.setFirstName(self.firstName)
        self.sp.setLastName(self.lastName)
        self.sp.setZip(self.zip)
        self.sp.clickContinue()
        self.sp.clickFinish()
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "THANK YOU FOR YOUR ORDER" in self.msg:
            assert True == True
            self.driver.close()
        else:
            assert False == False
            self.driver.close()




