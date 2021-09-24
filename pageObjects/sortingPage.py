class sorting:
    drp_productSortContainer_xpath = "//select[@class='product_sort_container']"
    priceSorting_xpath = "//select[@class='product_sort_container']"
    price_xpath = "//div[@class='inventory_item_price']"

    def __init__(self, driver):
        self.driver = driver

    def clickPriceSorting(self):
        self.driver.find_element_by_xpath(self.priceSorting_xpath).send_keys("Price (low to high)")

    def getPrice(self, value=None):
        prices = self.driver.find_elements_by_xpath(self.price_xpath)
        for value in prices:
            print(value.text)
           # return list(value.text)
       # if value.text == sorted(value.text):
       #     assert True
       # else:
    #    assert False


