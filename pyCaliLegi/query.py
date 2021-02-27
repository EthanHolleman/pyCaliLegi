from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time


def get_bill_search(browser):
    return browser.find_element_by_id('j_idt75:nav_bar_top_search')


def get_text_search(browser):
    '''Get the button that navigates to the bill text search page
    as a selenium element object.

    Args:
        browser (webdriver): Selenium webdriver 

    Returns:
        [type]: [description]
    '''
    return browser.find_element_by_id('j_idt75:nav_bar_top_text_search')


def get_keyword_fields(browser):
    '''Find the "and" and "or" keyword search fields on the bill
    search page.

    Args:
        browser (webdriver): Selenium webdriver navigated to the
        bill keyword search page.

    Returns:
        dict: Dictionary with two keys; "and" and "or". Values for
        each key will be the selenium elements representing the
        text entry boxes for each type of keyword search.
    '''
    field_dict = {}
    and_container = browser.find_element_by_id('adv_search_form_and')
    or_container = browser.find_element_by_id('adv_search_form_or')

    def get_fields_from_container(container):
        return container.find_elements_by_tag_name('input')
    field_dict['and'] = get_fields_from_container(and_container)
    field_dict['or'] = get_fields_from_container(or_container)
    return field_dict


def get_submit_button(browser):
    '''Find the submit button on the bill search page.

    Args:
        browser (webdriver): Selenium webdriver. Should be navigated
        to the bill search page.

    Returns:
        element: Selenium element object.
    '''
    return browser.find_element_by_id('billSearchAdvForm:attrSearch')


def get_navigate_bill_page_button(browser, next_page=True):
    data_nav = browser.find_element_by_id('dataNavForm')
    buttons = data_nav.find_elements_by_tag_name('input')
    active_buttons = []
    for button in buttons:
        if button.get_attribute('onclick'):
            active_buttons.append(button)

    if next_page:
        keyword = 'next'
    else:
        keyword = 'previous'

    for button in active_buttons:
        id_ = button.get_attribute('id')  # id describes button function
        if keyword in id_:
            return button

    raise Exception('Cannot navigate in selected direction')


def get_bills_from_search_results(browser):
    bill_table = browser.find_elements_by_tag_name('table')
    if len(bill_table) == 1:
        bill_table = bill_table.pop()
    else:
        raise Exception(
            f'Found {len(bill_table)} elements. Should have found 1.')
    return bill_table.find_elements_by_class_name('commdataRow')


def get_bill_pages_from_bill_table_elements(table_elements):
    return [el.find_element_by_tag_name('a').get_attribute('href') for el in table_elements]
