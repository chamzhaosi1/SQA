import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('driver\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        ## open the web page
        driver.get("https://shopee.com.my/")

        ## select the language (English)
        elem = driver.find_element(By.XPATH, "//*[@id='modal']/div[1]/div[1]/div/div[3]/div[1]/button")
        ## click the element 
        elem.send_keys(Keys.RETURN)

        # ## close the pop up (if any)
        # elem = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div/shopee-banner-popup-stateful//div/div/div/div/div")
        # ## click the element
        # elem.send_keys(Keys.RETURN)

        ## check the title (html title, this will show on the browser tab) 
        ## (can through the html source code or js code "document.title" to find the title name)
        self.assertIn("Shopee Malaysia | Free Shipping Across Malaysia", driver.title)

        ## find the element by id (Log in link)
        elem = driver.find_element(By.XPATH, "//*[@id='main']/div/header/div[1]/nav/ul/a[3]")
        ## click the element
        elem.send_keys(Keys.RETURN)
        ## wait for 1 second, to let the page load
        time.sleep(1)

        ## find the element by id (Form input - Phone number)
        elem = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/input")
        ## enter the username
        elem.send_keys("+60172879545")

        ## find the element by id (Form input - Password)
        elem = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[3]/div[1]/input")
        ## enter the password
        elem.send_keys("Testing1234") ## wrong password
        ## wait for 1 second,  to let the page load
        time.sleep(1)

        ## find the element by id (Form input - Log in button)
        elem = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div/div/div/div[2]/form/div/div[2]/button")
        ## click the element
        elem.send_keys(Keys.RETURN)
        
        self.assertNotIn("No results found.", driver.page_source)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()