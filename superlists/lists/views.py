from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from lists.models import Item

def home_page(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items' : items})
        

def new_list(request):
    new_item_text = request.POST['item_text']
    Item.objects.create(text = new_item_text)
    return redirect('/lists/the-only-list/')
        
def list_view(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items' : items})