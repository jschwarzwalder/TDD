import re
from django.test import TestCase
from django.http import HttpRequest  
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    # found = resolve('/')  
    # self.assertEqual(found.func, home_page)
        
    @staticmethod
    def remove_csrf(html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', html_code)
    
    def assertEqualExceptCSRF(self, html_code1, html_code2):
        return self.assertEqual(
            self.remove_csrf(html_code1),
            self.remove_csrf(html_code2)
        )
    
    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()
        
        #response = self.client.get('/') 
        response = home_page(request)
                    
        expected_content = render_to_string('home.html', request=request)
        self.assertEqualExceptCSRF(response.content.decode(), expected_content)
        
    def test_home_page_can_remember_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'
        
        response = home_page(request)                    
       
        self.assertIn('A new item', response.content.decode())
        
        expected_content = render_to_string('home.html', {'new_item_text': 'A new item'})
        self.assertEqualExceptCSRF(response.content.decode(), expected_content)


from lists.models import Item       

class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items_to_the_database(self):
        first_item = Item()
        first_item.text = 'Item the first'
        first_item.save()
        
        second_item = Item()
        second_item.text = 'Second Item'
        second_item.save()
        
        first_item_from_db = Item.objects.all()[0]
        self.assertEqual(first_item_from_db.text, 'Item the first')
        
        second_item_from_db = Item.objects.all()[1]
        self.assertEqual(second_item_from_db.text, 'Second Item')
        