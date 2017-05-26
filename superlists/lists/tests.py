# to run Django type in
# python manage.py runserver
# default http://localhost:8000/
# 
# cd Documents/GitHub/TDD/superlists
# workon superlists
# python manage.py test lists

import re
from django.test import TestCase
from django.http import HttpRequest  
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item, List   

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
        
class NewListViewTest(TestCase):
        
    def test_home_page_can_save_post_to_database(self):
        self.client.post('/lists/new', {'item_text': 'A new item'})  
        item_from_db = Item.objects.all()[0]
        self.assertEqual(item_from_db.text, 'A new item')   
    
    def test_redirects_to_list_url(self):
        response = self.client.post('/lists/new', {'item_text': 'A new item'})  

        #for redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/lists/the-only-list/')

       
        #self.assertIn('A new item', response.content.decode())
        #expected_content = render_to_string('home.html', {'new_item_text': 'A new item'})
        #self.assertEqualExceptCSRF(response.content.decode(), expected_content)

        
class ListViewTest(TestCase):

    def test_list_page_shows_items_in_database(self):
        our_list = List.objects.create()
        Item.objects.create(text='Item 1', list=our_list)
        Item.objects.create(text='Item 2', list=our_list)   

        other_list = List.objects.create()
        Item.objects.create(text='not this one', list=other_list)
              
              
        #using Django built in testsS
        response = self.client.get('/lists/%d/' % (our_list.id))        

        #self.assertIn('Item 1', response.content.decode())
        self.assertContains(response, 'Item 2')
        self.assertContains(response, 'Item 1')
        self.assertNotContains(response, 'not this one')
        
    def test_uses_lists_template(self):
        response = self.client.get('/lists/the-only-list')       
        self.assertTemplateUsed(response, 'list.html')
        
  

class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items_to_the_database(self):
        first_list = List()
        first_list.save()
        first_item = Item()
        first_item.text = 'Item the first'
        first_item.list = first_list
        first_item.save()
        
        second_item = Item()
        second_item.text = 'Second Item'
        second_item.list = first_list
        second_item.save()
        # need to make migrations for this to work
        # `python manage.py makemigrations`
        
        first_item_from_db = Item.objects.all()[0]
        self.assertEqual(first_item_from_db.text, 'Item the first')
        self.assertEqual(first_item_from_db.list, first_list)
        
        second_item_from_db = Item.objects.all()[1]
        self.assertEqual(second_item_from_db.text, 'Second Item')
        self.assertEqual(second_item_from_db.list, first_list)