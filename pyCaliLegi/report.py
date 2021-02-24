from pyCaliLegi.bill import *
from pyCaliLegi.summarize import summarize_bill
import pandas as pd


def bill_url_to_LAC_row(url, browser):
    browser.get(url)
    bill_dict = {}
    status_page_link = get_status_page_link(browser)
    history_page_link = get_history_page_link(browser)

    bill_dict.update({'summary': summarize_bill(browser)})

    # parse history page
    browser.get(history_page_link)
    bill_dict['Brief Status'] = format_last_action_tuple(
        get_last_action_from_history_page(browser)
    )

    # parse the status page
    browser.get(status_page_link)
    bill_dict.update(parse_status_page(browser))
    bill_dict.update({'url': url})

    return bill_dict


def write_csv_from_bill_dicts(bill_dicts, filepath):
    pd.DataFrame.from_dict(bill_dicts).to_csv(str(filepath))
    return filepath
