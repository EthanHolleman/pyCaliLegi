import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from pyCaliLegi import URL, args, report, search


def main():
    cmd_args = args.get_args()
    browser = search.create_browser(URL, headless=cmd_args.headless)
    browser.search.search_for_bills(
        browser, cmd_args.and_keywords, cmd_args.or_keywords)
    bill_urls = search.collect_all_bill_urls_from_search_results(browser)
    bill_dicts = [
        report.bill_url_to_LAC_row(bill_url, browser)
        for bill_url in bill_urls
    ]
    report.write_csv_from_bill_dicts(bill_dicts, cmd_args.outpath)


if __name__ == '__main__':
    main()
