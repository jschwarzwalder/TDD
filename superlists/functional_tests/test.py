# to run Django type in
# python manage.py runserver
# cd Documents/GitHub/TDD/superlists


from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import unittest

#run server with clean database each time
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
	
    def setUp(self):  
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
        #run server and clean database each time

    def tearDown(self):  
        self.browser.quit()
        
        
        
    def check_for_row_in_list_table(self, expected_row):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr') 
        self.assertIn(
            expected_row, [row.text for row in rows]
        )
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith goes to cool new todo list app homepage
                
            self.browser.get(self.live_server_url)
        
        #She notices the page title and header mention to-do lists
            self.assertIn('To-Do-Lists', self.browser.title)  
            header_text = self.browser.find_element_by_tag_name('h1').text  
            self.assertIn('To-Do', header_text)

        # We use self.assertIn instead of just assert to make our test assertions. 
        # unittest provides lots of helper functions like this to make test assertions, 
        # like assertEqual, assertTrue, assertFalse
        # Unit Test Documentation http://docs.python.org/3/library/unittest.html 
        
        # She is invited to enter a to-do item straight away
            inputbox = self.browser.find_element_by_id('id_new_item')  
            self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
            )
        
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
            inputbox.send_keys('Buy peacock feathers')  
        
        # When she hits enter, the page updates, and now the page lists
            inputbox.send_keys(Keys.ENTER)  
            time.sleep(1)  
        
        # "1: Buy peacock feathers" as an item in a to-do list table
            self.check_for_row_in_list_table("1: Buy peacock feathers")
        
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputbox.send_keys("Use peacock feathers to make a fly")
            inputbox.send_keys(Keys.ENTER)
            time.sleep(1)  
        
        # The page updates again, and now shows both items on her list
                       
            self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")
            self.check_for_row_in_list_table('1: Buy peacock feathers')
            
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        
        # She visits that URL - her to-do list is still there.
        
        # Satisfied, she goes back to sleep
            self.fail('Finish the test!')
        
    def test_isolation_and_evolving_applicaiton(self):
        # / = homepage
        # /lists/new - POST new list
        # /lists/(list-id)/ - existing list
        # /lists/(list-id)/add - add to list
        # Modelforlist, FK to items
        pass
        
        
if __name__ == '__main__':  
    unittest.main(warnings='ignore')