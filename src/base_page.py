from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseHelpers:

    def __init__(self, browser):
        self.driver = browser

    def open_page(self, url):
        return self.driver.get(url)

    def element_by_css(self, css_selector):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

    def element_by_xpath(self, xpath_selector):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_selector))
        )

    def enter_text_into_field(self, css_selector, text):
        field = self.element_by_css(css_selector)
        field.clear()
        field.send_keys(text)

    def click_button(self, css_selector):
        self.element_by_css(css_selector).click()

    def get_element_text(self, css_selector):
        return self.element_by_css(css_selector).text
