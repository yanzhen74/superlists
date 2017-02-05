from django.shortcuts import redirect, render
# from django.http import HttpResponse
from lists.models import Item


def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
