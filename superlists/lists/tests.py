from django.test import TestCase
from django.http import HttpRequest  

from lists.views import home_page

class HomePageTest(TestCase):

	# def test_root_url_resolves_to_home_page_view(self):
		# found = resolve('/')  
		# self.assertEqual(found.func, home_page)
		
	def test_home_page_is_about_todo_lists(self):
		request = HttpRequest()
		
		response = home_page(request)
		
		self.assertTrue(response_content.startswith(b'<html>'))
		self.assertIn(b'<title>To-Do-Lists</title>', response_content)
		self.assertTrue(response.content.endswith(b'</html>'))