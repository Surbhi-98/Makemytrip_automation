import sys
from telnetlib import SE
import time
sys.path.append("/home/cbnits/Documents/Makemytrip_Assignment/Utility")
sys.path.append("/home/cbnits/Documents/Makemytrip_Assignment/Pages")
import base_page
import flights_page
import flight_options_page
import flight_description_page




class Test_Script(base_page.BasePage):

    def test_makemytrip(self):
        self.driver.implicitly_wait(10)
        driver_title = self.driver.title
        print(driver_title)
        assert driver_title == "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"
        # assert driver_title == test_data.Test_Data.PAGE_TITLE
        self.message_logging(driver_title)
    
        flights_page_driver = flights_page.Flights_page_locators(self.driver)
        flights_page_driver.click_on_close_land_card()
        self.wait_clickable(flights_page_driver.FROM_PLACE)
        flights_page_driver.click_on_from_place()
        time.sleep(3)
        flights_page_driver.select_from_place()
        self.wait_clickable(flights_page_driver.TO_DESTINATION)
        flights_page_driver.click_on_to_detination()
        time.sleep(3)
        flights_page_driver.select_destination()
        self.wait_clickable(flights_page_driver.SEARCH_BUTTON)
        flights_page_driver.click_on_search_button()
        self.message_logging("Successfully click on Search Button")
    
        flight_options_page_driver = flight_options_page.Flights_options_page_locators(self.driver)
        self.wait_clickable(flight_options_page_driver.WINDOW_BUTTON)
        get_window_status = flight_options_page_driver.click_on_window()
        if len(get_window_status) > 0:
            self.taking_screen_short("window_popup.png")
            get_window_status[0].click()
        else:
            self.message_logging("Pop up window is not display")
        time.sleep(2)
        self.wait_clickable(flight_options_page_driver.VIEW_PRICE_BUTTON)
        airlines = flight_options_page_driver.get_airlines_name_click_on_viewprice(2)
        print(airlines)
        self.message_logging("List of Airlines "+ str(airlines))
        flight_options_page_driver.scroll_window()
        self.message_logging("Successfully click on View Price Button")
        time.sleep(2)
        self.wait_clickable(flight_options_page_driver.BOOK_NOW)
        flight = flight_options_page_driver.get_flight_list_click_on_booknow(2)
        print(flight)
        self.message_logging("List of flight "+ str(flight[0]))
        self.message_logging("List of flight prices "+ str(flight[1]))

                        # flight_name = flight_options_page_driver.get_flight_name()
                        # print(flight_name)
                        # self.message_logging("Flight to be clicked "+flight_name)
                        # time.sleep(5)
                        # flight_options_page_driver.click_on_book_now()
        self.message_logging("Successfully click on Book Now Button")

        flight_description_page_driver = flight_description_page.Flight_description_page_locators(self.driver)
        flight_description_page_driver.switch_to_new_tab()
        self.message_logging("Successfully switch to the new tab")
        time.sleep(2)
        flight_description_page_driver.scroll_to_location()
        time.sleep(2)
        self.wait_clickable(flight_description_page_driver.RADIO_BUTTON)
        flight_description_page_driver.click_on_radio_button()
        self.wait_clickable(flight_description_page_driver.ADULT_BUTTON)
        time.sleep(5)
        flight_description_page_driver.add_new_adult()
        flight_description_page_driver.enter_first_name()
        flight_description_page_driver.enter_last_name()
        self.wait_clickable(flight_description_page_driver.GENDER)
        flight_description_page_driver.select_gender()
        flight_description_page_driver.check_gst()
        flight_description_page_driver.enter_mobile_number()
        flight_description_page_driver.enter_email()
                                # self.wait_clickable(flight_description_page_driver.GST_CHECK)
                                # time.sleep(5)
                                # self.wait_clickable(flight_description_page_driver.GENDER)
                                # flight_description_page_driver.check_gst()
        flight_description_page_driver.enter_company_name()
        flight_description_page_driver.enter_gst_number()
        self.wait_clickable(flight_description_page_driver.CONTINUE_BUTTON)
        self.message_logging("Successfully Fill all the details")
        flight_description_page_driver.click_on_continue_button()
        self.message_logging("Successfully click on Continue Button")
        time.sleep(2)
        self.wait_clickable(flight_description_page_driver.CONFIRM_BUTTON)
        flight_description_page_driver.click_on_confirm_button()
        self.message_logging("Successfully click on Confirm Button")
        time.sleep(2)
        self.wait_clickable(flight_description_page_driver.POPUP)
        flight_description_page_driver.click_on_popup()
        # time.sleep(2)
        self.wait_clickable(flight_description_page_driver.SELECT_MEAL)
        get_meal_status = flight_description_page_driver.click_on_meal()
        if len(get_meal_status) > 0:
            get_meal_status[0].click()
            self.taking_screen_short("mealSS.png")
            self.wait_clickable(flight_description_page_driver.SEAT_CONTINUE_BUTTON)
            flight_description_page_driver.click_on_seat_continue_button()
            self.message_logging("Successfully selected seat and click on continue Button")
            time.sleep(2)
            self.wait_clickable(flight_description_page_driver.CONTINUE_ANYWAY)
            get_continue_anyway = flight_description_page_driver.click_on_continue_anyway_button()
            if len(get_continue_anyway) > 0:
                get_continue_anyway[0].click()
                self.message_logging("Successfully click on continue anyway Button")
            time.sleep(2)
            flight_description_page_driver.scroll_to_bottom()
        else:
            self.message_logging("Meal option is not available")
            self.taking_screen_short("mealSS.png")
            self.wait_clickable(flight_description_page_driver.SEAT_CONTINUE_BUTTON)
            flight_description_page_driver.click_on_seat_continue_button()
            self.message_logging("Successfully selected seat and click on continue Button")  
            time.sleep(2)
            flight_description_page_driver.scroll_to_bottom()  
        time.sleep(2)
        self.wait_clickable(flight_description_page_driver.PROCEED_TO_PAY)
        flight_description_page_driver.click_on_proceed_to_pay_button()
        self.message_logging("Successfully click on proceed to pay Button")
        time.sleep(4)
        self.driver.back()
        time.sleep(5)
        flight_description_page_driver.close_new_tab()

    

