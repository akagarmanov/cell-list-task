from src.cell_list_page import CellListHelpers
import pytest


def test_open_page(browser):
    CardsTests = CellListHelpers(browser)
    CardsTests.open_page(CardsTests.PAGE_URL)

    assert CardsTests.element_by_xpath(CardsTests.XPATH_TEXT % CardsTests.XPATH_NAME_OF_PAGE)


@pytest.mark.parametrize("test_category", CellListHelpers.TEST_CATEGORY)
def test_cards_creation(browser, test_category):
    CardsTests = CellListHelpers(browser)
    start_value_of_cards = CardsTests.total_cards_value()
    person = CardsTests.create_contact(test_category)
    assert CardsTests.total_cards_value() == start_value_of_cards + 1

    CardsTests.scroll_cards_to_bottom()
    #person = 'Fake Test'
    assert CardsTests.element_by_xpath(CardsTests.XPATH_TEXT % person)
