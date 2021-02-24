from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

# opts = Options()
# #opts.set_headless()
# #assert opts.headless  # Operating in headless mode
# browser = Firefox(options=opts)
# browser.get('https://leginfo.legislature.ca.gov/faces/billSearchClient.xhtml')

def get_bill_search(browser):
    return browser.find_element_by_id('j_idt75:nav_bar_top_search')

def get_text_search(browser):
    return browser.find_element_by_id('j_idt75:nav_bar_top_text_search')

def get_keyword_fields(browser):
    field_dict = {}
    and_container = browser.find_element_by_id('adv_search_form_and')
    or_container = browser.find_element_by_id('adv_search_form_or')

    def get_fields_from_container(container):
        return container.find_elements_by_tag_name('input')
    field_dict['and'] = get_fields_from_container(and_container)
    field_dict['or'] = get_fields_from_container(or_container)
    return field_dict

def get_submit_button(browser):
    return browser.find_element_by_id('billSearchAdvForm:attrSearch')

def press_submit(submitable, wait=1):
    time.sleep(wait)
    submitable.submit()
    time.sleep(wait)

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
        raise Exception(f'Found {len(bill_table)} elements. Should have found 1.')
    return bill_table.find_elements_by_class_name('commdataRow')

def get_bill_pages_from_bill_table_elements(table_elements):
    return [el.find_element_by_tag_name('a').get_attribute('href') for el in table_elements]
    
   

# text_search = get_text_search(browser)
# text_search.click()
# fields = get_keyword_fields(browser)
# fields['and'][0].send_keys('housing')
# submit_button = get_submit_button(browser)
# press_submit(submit_button)
# next_page = get_navigate_bill_page_button(browser)
# print(next_page.tag_name)
# time.sleep(1)
# next_page.click()
# bills = get_bills_from_search_results(browser)
# links = get_bill_pages_from_bill_table_elements(bills)
# print(links)