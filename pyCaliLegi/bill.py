from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

# opts = Options()
# #opts.set_headless()
# #assert opts.headless  # Operating in headless mode
# browser = Firefox(options=opts)
# browser.get('https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202120220AB1358&search_keywords=housing')

def get_bill_title(browser):
    title_container = browser.find_element_by_id('bill_title')
    title = title_container.find_element_by_tag_name('h2').text
    return title


def get_bill_intro(browser):
    digest_text = browser.find_element_by_id('digesttext')
    return digest_text.text


def get_status_page_link(browser):
    status = browser.find_element_by_id('nav_bar_top_status')
    return status.get_attribute('href')

def get_history_page_link(browser):
    history = browser.find_element_by_id('nav_bar_top_history')
    return history.get_attribute('href')

def get_lead_authors_from_status_page(browser):
    return browser.find_element_by_id('leadAuthors').text.strip()

def get_measure_num_from_status_page(browser):
    return browser.find_element_by_id('measureNum').text.strip()

def get_topic_from_status_page(browser):
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
    table = browser.find_element_by_id('billhistory')
    table_body = table.find_element_by_tag_name('tbody')
    events = table_body.find_elements_by_tag_name('tr')
    if events:
        date, text = events[0].find_elements_by_class_name('columnField')
        return date.text, text.text

def format_last_action_tuple(last_action):
    return ' '.join(last_action).strip()


# title = get_bill_title(browser)
# print(title)
# digest = get_bill_intro(browser)
# print(digest)
# status_link = get_status_page_link(browser)
# print(status_link)
# browser.get(status_link)
# status_page = parse_status_page(browser)
# print(status_page)
# history_page = get_history_page_link(browser)
# browser.get(history_page)
# last_event = get_last_action_From_history_page(browser)
# print(last_event)