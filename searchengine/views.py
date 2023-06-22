from django.shortcuts import render
from .models import Restaurant
# Create your views here.

def index(request):
    if request.method=='POST':
        res = []
        items_that_matched = []
        search_term = request.POST.get('dish')
        if search_term == '':
            res = Restaurant.objects.all()
            return render(request, 'index.html', {'res': res})

        list_of_items = Restaurant.objects.values_list('restaurant_id', 'items')
        for id, dic in list_of_items:
            for key in dic.keys():
                if search_term in dic:
                    items_that_matched.append(key)
                    res.append(id)
                    break
                search_term = search_term.lower()
                if search_term in key.lower().split():
                    items_that_matched.append(key)
                    res.append(id)
                    break
        # print(items_that_matched)
        result = [Restaurant.objects.get(pk=i) for i in res]
        return render(request, 'index.html', {'res': result,'items_that_matched': items_that_matched})

    res = Restaurant.objects.all()
    return render(request, 'index.html', {'res': res})