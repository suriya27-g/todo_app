from django.shortcuts import render, redirect
from .models import List_View

# Create your views here.
def top(request):
    return render(request, 'list_app/top.html')

def list_view(request):
    if request.method == 'POST':
        x = request.POST['item']
        new_item = List_View(items = x)
        new_item.save()
        return redirect('list_view')
    else:
        list_items = List_View.objects.all()
        context = {'list_items': list_items}
        return render(request, 'list_app/list_view.html', context)    

def delete(request,i):
    y = List_View.objects.get(id= i)
    y.delete()
    return redirect('list_view')