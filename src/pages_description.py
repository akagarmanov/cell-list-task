class CellListPage:

    PAGE_URL = 'http://samples.gwtproject.org/samples/Showcase/Showcase.html#!CwCellList'

    CSS_FIRST_NAME = "tr:nth-child(2) > td > .gwt-TextBox"
    CSS_LAST_NAME = "tr:nth-child(3) .gwt-TextBox"
    CSS_ADDRESS = ".gwt-TextArea"
    CSS_BIRTHDAY = ".gwt-DateBox"
    CSS_CREATE_BUTTON = ".gwt-Button:nth-child(2)"
    CSS_COUNTER = "td > .gwt-HTML"
    CSS_CARDS_LIST = ".CMWVMEC-p-b"
    CSS_CATEGORY = "tr:nth-child(4) .gwt-ListBox"
    XPATH_NAME_OF_PAGE = "Cell List"
    XPATH_TEXT = "//*[text()='%s']"

    TEST_CATEGORY = ["Family", "Friends", "Coworkers", "Businesses", "Contacts"]

