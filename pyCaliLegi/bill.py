from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time


def get_bill_intro(browser):
    '''Given a webdriver navigated to the status page of
    a specific bill return the intro to the bill. This
    should be a few sentences describing the proposals
    layed out by the bill.

    Args:
        browser (webdriver): Selenium webdriver.

    Returns:
        str: Intro to the bill as a string.
    '''
    digest_text = browser.find_element_by_id('digesttext')
    return digest_text.text


def get_status_page_link(browser):
    '''Given a webdriver navigated to the webpage for a specific
    bill return the link to the bill's status page. The status
    page will contain must of the general information about the
    bill including title, topics, author, coauthors etc which
    can be extracted with other functions.

    Args:
        browser (webdriver): Selenium webdriver.

    Returns:
        str: Url to the bill's status page as a string.
    '''
    status = browser.find_element_by_id('nav_bar_top_status')
    return status.get_attribute('href')

def get_history_page_link(browser):
    '''Given a webdriver navigated to the webpage for a specific bill
    return the link to the history page.

    Args:
        browser (webdriver): Selenium webdriver.

    Returns:
        str: Url to the bill's history page as a string.
    '''
    history = browser.find_element_by_id('nav_bar_top_history')
    return history.get_attribute('href')

def get_lead_authors_from_status_page(browser):
    return browser.find_element_by_id('leadAuthors').text.strip()

def get_measure_num_from_status_page(browser):
    '''Given a webdriver navigated to the status tab of a
    bill's webpage return the measure number of the bill
    as a string.

    Args:
        browser (webdriver): Selenium webdriver.

    Returns:
        str: Bill's measure number, can be used as a unique id.
    '''
    return browser.find_element_by_id('measureNum').text.strip()


def get_topic_from_status_page(browser):
    '''Given a webdriver navigated to the status tab
    of a bill's webpage return the subject information
    for the bill.

    Args:
        browser (webdriver): Selenium webdriver.

    Returns:
        str: Bill subject information as a string.
    '''
    return browser.find_element_by_id('subject').text.strip()


def parse_status_page(browser):
    find_dict = {
        'Title': 'title',
        'Measure Number': 'measureNum',
        'Lead Authors': 'leadAuthors',
        'Topic': 'subject',
        'Coauthors': 'coAuthors',
        'Principal Coauthors': 'principalAuthors'
    }
    attr_dict = {}
    for attr, id_ in find_dict.items():
        attr_dict[attr] = browser.find_element_by_id(id_).text.strip()
    return attr_dict


def get_last_action_from_history_page(browser):
    '''Given a webdriver object navigated to a bill's history
    page return the last legeslative action that has been
    taken.

    Args:
        browser (webdriver): Selenium webdriver.

    Returns:
        tuple: Tuple of length two. First item is the date (str) of last
        action and second is the action as as string.
    '''
    table = browser.find_element_by_id('billhistory')
    table_body = table.find_element_by_tag_name('tbody')
    events = table_body.find_elements_by_tag_name('tr')
    if events:
        date, text = events[0].find_elements_by_class_name('columnField')
        return date.text, text.text

def format_last_action_tuple(last_action):
    return ' '.join(last_action).strip()