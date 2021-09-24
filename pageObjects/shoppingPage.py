class shopping:
    button_addToCart_id = "add-to-cart-sauce-labs-backpack"
    link_cart_xpath = "//a[@class='shopping_cart_link']"
    button_checkOut_id = "checkout"
    textbox_firstName_id = "first-name"
    textbox_lastName_id = "last-name"
    textbox_zip_id = "postal-code"
    button_continue_id = "continue"
    button_finish_id = "finish"

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        self.driver.find_element_by_id(self.button_addToCart_id).click()

    def clickCart(self):
        self.driver.find_element_by_xpath(self.link_cart_xpath).click()

    def clickCheckout(self):
        self.driver.find_element_by_id(self.button_checkOut_id).click()

    def setFirstName(self, firstName):
        self.driver.find_element_by_id(self.textbox_firstName_id).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element_by_id(self.textbox_lastName_id).send_keys(lastName)

    def setZip(self, zip):
        self.driver.find_element_by_id(self.textbox_zip_id).send_keys(zip)

    def clickContinue(self):
        self.driver.find_element_by_id(self.button_continue_id).click()

    def clickFinish(self):
        self.driver.find_element_by_id(self.button_finish_id).click()
