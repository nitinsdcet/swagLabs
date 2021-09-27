import pytest
from selenium.common.exceptions import NoSuchElementException

from pageObjects.LoginPage import Login
from pageObjects.shoppingPage import shopping
from utilities.readProperties import ReadConfig
from pageObjects.clearPage import clear


class Test_oo4_Clear:
    baseURL = ReadConfig.getApplicationURL()
    userEmail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    @pytest.mark.regression
    def testClear(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.userEmail)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        self.sp = shopping(self.driver)
        self.sp.addToCart()
        self.sp.clickCart()
        if self.driver.find_element_by_xpath("//div[@class='cart_quantity']").is_displayed():
            assert True
        else:
            assert False
        self.cls = clear(self.driver)
        self.cls.clickRemove()
        try:
            item = self.driver.find_element_by_xpath("//div[@class='cart_quantity']")
            s = item.text
            if s == 1:
                print("Item not removed and item added:" + s)
        except NoSuchElementException:
            print("Item removed")
