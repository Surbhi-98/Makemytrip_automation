from re import T
from selenium.webdriver.common.by import By

class Flights_page_locators:
    #Locators
    FROM_PLACE = (By.XPATH, "//div[@class='fsw_inputBox searchCity inactiveWidget ']/label/span[@class = 'lbl_input latoBold  appendBottom5']")
    ENTER_FROM_PLACE = (By.XPATH, "//div/input[@placeholder='From']")
    SELECT_FROM_PLACE = (By.XPATH, "//ul/li[@role = 'option']/div/div/p[@class = 'font14 appendBottom5 blackText']")
    TO_DESTINATION = (By.XPATH, "//label[@for = 'toCity']/span[@class = 'lbl_input latoBold  appendBottom5']")
    ENTER_TO_PLACE = (By.XPATH, "//div/input[@placeholder='To']")
    SELECT_DESTINATION = (By.XPATH, "//ul/li[@role = 'option']/div/div/p[@class = 'font14 appendBottom5 blackText']")
    SEARCH_BUTTON = (By.XPATH, "//a[normalize-space()='Search']")
    CLOSE_CARD = (By.XPATH, "//span[@class = 'langCardClose']")

    def __init__(self, driver):
        self.driver = driver
    
    def click_on_close_land_card(self):
        """"
            Close land card
        """
        return self.driver.find_element(*Flights_page_locators.CLOSE_CARD).click()

    def click_on_from_place(self):
        """"
            Click on From dropdown button
        """
        return self.driver.find_element(*Flights_page_locators.FROM_PLACE).click()

    def select_from_place(self):
        """"
            Select From place from dropdown
        """
        self.driver.find_element(*Flights_page_locators.ENTER_FROM_PLACE).send_keys("Kol")
        select_place = self.driver.find_elements(*Flights_page_locators.SELECT_FROM_PLACE)
        print(len(select_place))
        for place in select_place:
            place_text = place.text
            if place_text == "Kolkata, India":
                place.click()
                break
    
    # def click_on_from_place(self):
    #     """"
    #         Click on From Dropdown
    #     """
    #     return self.driver.find_element(*Flights_page_locators.FROM_PLACE).click()

    def click_on_to_detination(self):
        """"
            Click on To dropdown button
        """
        return self.driver.find_element(*Flights_page_locators.TO_DESTINATION).click()
    
    def select_destination(self):
        """"
            Select To place from dropdown
        """
        self.driver.find_element(*Flights_page_locators.ENTER_TO_PLACE).send_keys("Mum")
        select_place = self.driver.find_elements(*Flights_page_locators.SELECT_DESTINATION)
        print(len(select_place))
        for place in select_place:
            place_text = place.text
            if place_text == "Mumbai, India":
                place.click()
                break
        
    def click_on_search_button(self):
        """"
            Click on Search button
        """
        return self.driver.find_element(*Flights_page_locators.SEARCH_BUTTON).click()


















# //div[@class='fsw_inputBox searchCity inactiveWidget ']/label/span[@class = 'lbl_input latoBold  appendBottom5']