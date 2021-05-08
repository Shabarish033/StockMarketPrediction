from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import time
"""The function below downloads the Market data"""
def DownloadData(i):
    chromeOptions = webdriver.ChromeOptions()
    """Define the path where the downloaded files are kept"""
    prefs = {"download.default_directory" : "/home/spilkun/Desktop/projects/TestandFeatures/weather/data/"}
    chromeOptions.add_experimental_option("prefs",prefs)
    """Path to the google chrome driver"""
    chromedriver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
    """Open Chrome"""
    """Go to Yahoo, finance .com"""
    driver.get("https://finance.yahoo.com/")
    driver.implicitly_wait(200)
    """Agree to the terms and conditions"""
    driver.find_element_by_name('agree').click()
    driver.page_source
    """Go to the website to search for the companies history data"""
    inputElement = driver.find_element_by_id('yfin-usr-qry')
    """Get the company name"""
    inputElement.send_keys(i)
    inputElement.submit()
    """In the website go to the historical data tab and click on Download"""
    Historical_data = driver.find_element_by_link_text('Historical Data').click()
    Historical_data = driver.find_element_by_link_text('Download').click()
    """wait for 5 seconds before closing abruptly"""
    time.sleep(5)  
    driver.quit()
    return Historical_data

"""The input"""
ListOfCompanies = ['GE', 'safran', 'boeing', 'airbus']
"""For each company download its corresponding data"""
for i in ListOfCompanies:
    Data = DownloadData(i)
