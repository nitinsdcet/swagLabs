import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from pageObjects.sortingPage import sorting


class Test_003_Sorting:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    @pytest.mark.regression
    def testSorting(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        self.sr = sorting(self.driver)
        self.sr.clickPriceSorting()
        self.sr.getPrice()

