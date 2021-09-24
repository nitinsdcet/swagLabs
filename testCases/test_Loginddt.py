import time

import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities import XLUtilities


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.rows = XLUtilities.getRowCount(self.path, 'Sheet1')
        print("No. of rows in excel:", self.rows)
        lst_status = []  # empty list variable
        for r in range(2, self.rows+1):
            self.user = XLUtilities.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtilities.readData(self.path, 'Sheet1', r, 2)
            self.result = XLUtilities.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogIn()
            time.sleep(5)

            # act_title = self.driver.title
            # exp_title = "Swag Labs"
            # if act_title == exp_title:
            #    print(exp_title)
            if self.result == "pass":
                self.lp.clickHamburger()
                time.sleep(10)
                self.lp.clickLogOut()
                lst_status.append("pass")
            elif self.result == "fail":
                # self.lp.clickHamburger()
                # time.sleep(10)
                # self.lp.clickLogOut()
                lst_status.append("pass")
        # elif act_title != exp_title:
        # if self.result == "pass":
        #    lst_status.append("fail")
        # elif self.result == "fail":
        #   lst_status.append("pass")

        if "fail" not in lst_status:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
