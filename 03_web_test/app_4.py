import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('driver\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        ## open the web page
        driver.get("https://www.sinchew.com.my/")

        ## check the title (html title, this will show on the browser tab) 
        ## (can through the html source code or js code "document.title" to find the title name)
        self.assertIn("星洲网 Sin Chew Daily Malaysia Latest News and Headlines", driver.title)

        ## if the pop up appear, close it otherwise continue
        self.close_pop_up(driver)

        ## find the element by id (Log in link)
        elem = driver.find_element(By.XPATH, "//*[@id='header-login-btn']")
        ## click the element
        elem.click()
        ## wait for 1 second, to let the page load
        time.sleep(1)

        ## if the pop up appear, close it otherwise continue
        self.close_pop_up(driver)
        
        ## find the element by id (Form input - Email)
        elem = driver.find_element(By.XPATH, "//*[@id='email']")
        ## enter the username
        elem.send_keys("chamzhaosi@gmail.com")

        ## find the element by id (Form input - Password)
        elem = driver.find_element(By.XPATH, "//*[@id='signinForm']/div[2]/input")
        ## enter the password
        elem.send_keys("Testing12345") ## correct password
        ## wait for 1 second,  to let the page load
        time.sleep(1)

        ## find the element by id (Form input - Log in button)
        elem = driver.find_element(By.XPATH, "//*[@id='signinForm']/div[3]/input")
        ## click the element
        elem.send_keys(Keys.RETURN)
        
        self.assertNotIn("No results found.", driver.page_source)
        time.sleep(1)

        ## if the pop up appear, close it otherwise continue
        self.close_pop_up(driver)

        ## find the element by id (Latest News link)
        elem = driver.find_element(By.XPATH, "//*[@id='menu-item-3309626']/a")
        ## click the element
        elem.click()
        ## wait for 1 second, to let the page load
        time.sleep(1)

        self.assertNotIn("No results found.", driver.page_source)
        time.sleep(1)

        ## if the pop up appear, close it otherwise continue
        self.close_pop_up(driver)

        ## find the element by id (First News link)
        elem = driver.find_element(By.XPATH, "//*[@id='cat-post-list']/div[1]/div[2]/a")
        ## click the element
        elem.click()
        ## wait for 1 second, to let the page load
        time.sleep(1)

        self.assertNotIn("No results found.", driver.page_source)
        time.sleep(1)

        ## if the pop up appear, close it otherwise continue
        self.close_pop_up(driver)

        ## find the element by id (Hover on the div)
        hover_element = driver.find_element(By.XPATH, "//*[@id='header-login-btn']")
        actions = ActionChains(driver)
        actions.move_to_element(hover_element).perform()
        time.sleep(1)

        ## find the element by id (Log out link)
        elem = driver.find_element(By.XPATH, "//*[@id='header-login-btn']/div[2]")
        ## click the element
        elem.click()
        ## wait for 1 second, to let the page load
        time.sleep(1)

    
    def close_pop_up(self, driver):
        ## if the pop up appear, close it, otherwise skip
        try:
            elem = driver.find_element(By.XPATH, "//*[@id='full_screen_btn_close']")
            ## click the element
            elem.click()
            ## wait for 1 second, to let the page load
            time.sleep(1)

        except NoSuchElementException:
            pass

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()