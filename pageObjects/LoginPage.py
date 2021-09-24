class Login:
    textBox_userName_id = "user-name"
    textBox_password_id = "password"
    button_logIn_id = "login-button"
    button_hamburger_id = "react-burger-menu-btn"
    link_logOut_id = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, userName):
        self.driver.find_element_by_id(self.textBox_userName_id).clear()
        self.driver.find_element_by_id(self.textBox_userName_id).send_keys(userName)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textBox_password_id).clear()
        self.driver.find_element_by_id(self.textBox_password_id).send_keys(password)

    def clickLogIn(self):
        self.driver.find_element_by_id(self.button_logIn_id).click()

    def clickLogOut(self):
        self.driver.find_element_by_id(self.link_logOut_id).click()

    def clickHamburger(self):
        self.driver.find_element_by_id(self.button_hamburger_id).click()



