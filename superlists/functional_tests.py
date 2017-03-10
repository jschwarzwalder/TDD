from selenium import webdriver

#Edith goes to cool new todo list app homepage
browser = webdriver.Firefox()

browser.get('http://localhost:8000')

#She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

#She does other stuff

browser.quit()

#To run Django type in
# python manage.py runserver
# cd Documents/GitHub/TDD/superlists