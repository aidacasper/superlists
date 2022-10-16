import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # One heard about a cool new online to-do list app, one goes to check out the homepage
        self.browser.get('http://localhost:8000')

        # One notices the page header and title mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # One is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # One types 'buy peacock feathers' into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the pages lists
        # '1: Buy peacock feathers'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table= self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # There is still text inviting her to add another to-do item, she enters
        # 'Make lure with peacock feathers'
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again and both of her to-do items are listed
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )

        # One wonders whether the site will remember the list. 
        self.fail('Finish the test!')
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')

