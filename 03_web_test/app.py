import time, unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Browser:
    browser, service = None, None

    def __init__(self, driver:str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url:str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

if __name__ == '__main__':
    browser = Browser('driver\chromedriver.exe')
    browser.open_page('https://www.google.com')
    time.sleep(5)
    browser.open_page('https://www.naver.com')
    time.sleep(5)
    browser.close_browser()