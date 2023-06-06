import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('driver\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        elem = driver.find_element(By.XPATH, "//*[@id=\"APjFqb\"]")
        elem.send_keys("youasdafasdfasdfasdfasdftube")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()