from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from pyCaliLegi.bill import *
from pyCaliLegi.query import *
from pyCaliLegi.utils import *
import time

def create_browser(start_url, headless=True):
    '''Create a seleium browser and navigate to the
    specified url.

    Args:
        start_url (str): Url to open browser to.
        headless (bool, optional): Run browser in headless mode. Defaults to True.

    Returns:
        webdriver: Selenium firefox wedriver.
    '''
    opts = Options()
    if headless:
        opts.set_headless()

    browser = Firefox(options=opts)
    browser.get(start_url)
    return browser

def search_for_bills(browser, and_keywords=[], or_keywords=[], wait=0.5):
    '''Given a browser that is navigated to the Cali Legi bill search
    portal (URL constant in __init__.py) use keywords to search for
    specific bills.

    Args:
        browser (webdriver): Selenium webdriver object.
        and_keywords (list, optional): List of up to three keywords to use in 
                                       the "and" search. Defaults to [].
        or_keywords (list, optional): List of up to three keywords to use in the
                                      "or" search. Defaults to [].
        wait (float, optional): Time to pause in seconds after submiting the search
                                . Defaults to 0.5. Longer wait times tend to help
                                if connections are slower.

    Returns:
        webdriver: Webdriver navigated to the first page of bill seach results.
    '''
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
    '''Given a webdriver (browser) navigated to the first page
    of search results from a bill search, collects urls to all
    bills for all results pages. 

    Args:
        browser ([type]): [description]

    Returns:
        [type]: [description]
    '''
    all_bill_links = []
    next_page_button = get_navigate_bill_page_button(browser, next_page=True)
    try:
        while True:
            current_page_bills = get_bills_from_search_results(browser)
            all_bill_links += get_bill_pages_from_bill_table_elements(current_page_bills)
            next_page_button.click()
            time.sleep(1)  # allow time for page to load fully
    except Exception as e:
        return all_bill_links







    


