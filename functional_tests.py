import unittest
from selenium import webdriver


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
        self.fail('Finish the test!')

        # One is invited to enter a to-do item straight away


if __name__ == '__main__':
    unittest.main(warnings='ignore')

