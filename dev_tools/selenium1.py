import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgSearch(unittest.TestCase):

    '''
    Learning point 1: Combination of Unittest framework with the selenium
    Learning point 2: Web page navigation: driver.get(), forward(), back()
    Learning point 3: Find element(s): id,name,xpath,class_name,link,tag,css
    Learning point 3: Web interaction: click, send_keys,
    Learning point 4: todo: select from drop-down options
    Learning point 5: todo: drag-and-drop,
    Learning point 6: todo: switch between windows and frames (iframe)
    Learning point 7: todo: handling popup dialog
    Learning point 8: todo: explicit wait (conditions) and implicit wait
    Learning point 9: todo: execution sequence
    Learning point10: todo: PageObjectModel (see python_org.py codes)
    '''

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.google.com")
        assert "Google" in driver.title
        elem = driver.find_element_by_name('q')
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_explicit_wait(self):
        driver = self.driver
        driver.get("http://somedomain/url_that_delays_loading")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement")))

    def test_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(10)  # sec
        driver.get("http://somedomain/url_that_delays_loading")
        myDynamicElement = driver.find_element_by_id("myDynamicElement")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
        unittest.main()
