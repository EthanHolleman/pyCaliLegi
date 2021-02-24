from pyCaliLegi import search
from pyCaliLegi import report
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pandas as pd




def main():
    pass

if __name__ == '__main__':
    main()


url = 'https://leginfo.legislature.ca.gov/faces/billSearchClient.xhtml'
browser = search.create_browser(url, headless=False)
browser = search.search_for_bills(browser, ['housing'])
bill_urls = search.collect_all_bill_urls_from_search_results(browser)

bill_dicts = []
for bill_url in bill_urls:
    bill_dicts.append(report.bill_url_to_LAC_row(bill_url, browser))

pd.DataFrame.from_dict(bill_dicts).to_csv('test.csv')
    
