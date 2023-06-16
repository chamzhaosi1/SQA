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
        driver.get("https://elp.newera.edu.my/moodle/")

        ## check the title (html title, this will show on the browser tab)
        self.assertIn("New Era University College Electronic Learning Portal", driver.title)

        ## find the element by id (Log in button)
        elem = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/header/div/div[2]/span/a")
        ## click the element
        elem.send_keys(Keys.RETURN)

        ## find the element by id (Form input - Username)
        elem = driver.find_element(By.XPATH, "//*[@id='username']")
        ## enter the username
        elem.send_keys("chamzhaosi0808")

        ## find the element by id (Form input - Password)
        elem = driver.find_element(By.XPATH, "//*[@id='password']")
        ## enter the password
        elem.send_keys("chamzhaosi0808") ## wrong password

        ## find the element by id (Form input - Log in button)
        elem = driver.find_element(By.XPATH, "//*[@id='loginbtn']")
        ## click the element
        elem.send_keys(Keys.RETURN)
        
        self.assertNotIn("No results found.", driver.page_source)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()