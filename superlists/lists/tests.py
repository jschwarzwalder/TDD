from django.test import TestCase
from django.http import HttpRequest  

from lists.views import home_page

class HomePageTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    # found = resolve('/')  
    # self.assertEqual(found.func, home_page)
        
    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()
        
        response = self.client.get('/') 
            
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do-Lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        
        with open('lists/templates/home.html') as f:
            expected_content = f.read()
        
        self.assertEqual(html, expected_content)
		
        
