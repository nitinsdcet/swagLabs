# import allure
import pytest
# from allure_commons.types import AttachmentType

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig


# allure.severity(allure.severity_level.NORMAL)


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    userEmail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

 #   allure.severity(allure.severity_level.MINOR)

    @pytest.mark.regression
    def testHomePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
           # allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",
             #             attachment_type=AttachmentType.png)
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            assert False

    # allure.severity(allure.severity_level.CRITICAL)

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.userEmail)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            print(act_title)
            self.driver.close()
            assert False














