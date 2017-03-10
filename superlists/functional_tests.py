import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
	def test_starting_a_new_todo_list(self);

#Edith goes to cool new todo list app homepage
browser = webdriver.Firefox()

browser.get('http://localhost:8000')

#She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title, "Browser title was " + browser.title

#She does other stuff

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep


browser.quit()

#To run Django type in
# python manage.py runserver
# cd Documents/GitHub/TDD/superlists