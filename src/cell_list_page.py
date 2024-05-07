from src.base_page import BaseHelpers
from src.pages_description import CellListPage

from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support.ui import Select
from faker import Faker
import time


class CellListHelpers(BaseHelpers, CellListPage):

    def enter_date(self, css_selector, date):
        date_field = self.element_by_css(css_selector)
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

    def select_category(self, css_selector, category):
        select = Select(self.element_by_css(css_selector))
        select.select_by_visible_text(category)

    def scroll_cards_to_bottom(self):
        scrolling_frame = self.element_by_css(self.CSS_CARDS_LIST)
        # it seems to be a bug in card addition when scroll already at the bottom
        # and we need to go up (HOME Button) before go down (END Button)
        scrolling_frame.send_keys(Keys.HOME)
        counter = self.element_by_css(self.CSS_COUNTER)

        start_value = counter.text

        while True:
            scrolling_frame.send_keys(Keys.END)
            time.sleep(0.5)
            if counter.text != start_value:
                start_value = counter.text
            else:
                break

    def total_cards_value(self):
        raw_text = self.get_element_text(self.CSS_COUNTER)
        return int(re.split(r"\s+", raw_text)[4])

    def create_contact(self, category):
        # let's create som names using faker library
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()

        # fullname of the person we need to check if card was created
        person = f"{first_name} {last_name}"
        address = fake.address()
        self.enter_text_into_field(self.CSS_FIRST_NAME, first_name)
        self.enter_text_into_field(self.CSS_LAST_NAME, last_name)
        self.select_category(self.CSS_CATEGORY, category)
        self.enter_text_into_field(self.CSS_ADDRESS, address)
        self.enter_date(self.CSS_BIRTHDAY, "November 16, 2023")
        self.click_button(self.CSS_CREATE_BUTTON)
        return person
