from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from pyCaliLegi.bill import *
from pyCaliLegi.query import *
from pyCaliLegi.utils import *
import time

def create_browser(start_url, headless=True):
    opts = Options()
    if headless:
        opts.set_headless()

    browser = Firefox(options=opts)
    browser.get(start_url)
    return browser

def search_for_bills(browser, and_keywords=[], or_keywords=[], wait=0.5):
    # search for bills using keywords return a browser on the first page of
    # the search results
    text_search = get_text_search(browser)
    text_search.click()
    search_fields = get_keyword_fields(browser)
    if and_keywords:
        print(len(search_fields['and']))
        for i in range(0, min((len(and_keywords), 3))):
            search_fields['and'][i].send_keys(and_keywords[i])
    if or_keywords:
        for i in range(0, min((len(or_keywords), 3))):
            search_fields['or'][i].send_keys(or_keywords[i])
    
    search_button = get_submit_button(browser)
    press_submit(search_button, wait=1)

    return browser

def collect_all_bill_urls_from_search_results(browser):
    all_bill_links = []
    next_page_button = get_navigate_bill_page_button(browser, next_page=True)
    try:
        while True:
            current_page_bills = get_bills_from_search_results(browser)
            all_bill_links += get_bill_pages_from_bill_table_elements(current_page_bills)
            next_page_button.click()
            time.sleep(1)
    except Exception as e:
        print(e)
        return all_bill_links







    


