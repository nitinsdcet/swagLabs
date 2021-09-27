class clear:
    button_Remove_id = "remove-sauce-labs-backpack"

    def __init__(self, driver):
        self.driver = driver

    def clickRemove(self):
        self.driver.find_element_by_id(self.button_Remove_id).click()

