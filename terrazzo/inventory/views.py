from django.shortcuts import render
from .models import Category
from .models import CategoryField
import requests

# Create your views here.
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOWNjZDhkMjczMjA4Yzg3MWMzYzJjZTg1NWQ0ZDMwNTQ1NjM5MzRhNmUzNmRkYzhkYzM2MWQzNWE5YTQ5NzBmZTVhM2FjMjhmNjQ1MTAxNWQiLCJpYXQiOjE3NzMxOTYwMTEuODY3Mzg4LCJuYmYiOjE3NzMxOTYwMTEuODY3MzksImV4cCI6MjI0NjU4MTYxMS44NDM2OTIsInN1YiI6IjgiLCJzY29wZXMiOltdfQ.n6ZIN4Y5m3vgR6eUkPj3xDUYFTafodmreTORUU9ZyjXNI6KayA1crOxriSH-R3UUWepXe2cziTjl4MOPx-sk33K7UkHi7V9WTqIvqkwaYC_zVF8te2ztoSR9TXFrYALiaveHANtN8TdidrklZOG7_v54jJn4LIBTv5o4M1eVVHT9LKMl_OpFqbkUwOdjHMMePSLBbVAiztTcBr463YkoFG8y256t7ghqtlFd7xT1uuK2vyxhGnCP-Bl-x1zOSbWmwHx-1cKQPfTSkogi0PrBC4S49HBlv5a5OSetl3zd5soS3P3Q-G-g1cHgaQk1dBhY5ojQBF75cZ17s0HT4GHUCQpE-ky0Y3CtPNNeOrT1LqnYdKXr5TCUJIEbqJL1Hox-ilpZFUYv6nU02MYOHn7Gob3UDjdQo5EeaddNY-WEey0Xlo2TWVStotpRDDwfSbroKnFB3LnO0UF6KQuBAf_JA3rBWU7cikW2HPyHljqKy-jBmtIVR1odoohIsKUraPgrUHXold4qxme2WkAhMbvxjFFjTIm6RMP1Qe_Ftc8gpBzSWfqdojS5x_zuZ17JLzP1gogzNQTr9kevI-GWxeFZwIWPxfly8Df12yUozksUGulXn7WVTb95Hp_Wp8EKIF5Gfl_P6oVZJS95V_hMtz3Ip5ja_2c3jrDnR066Ps7F-6k'
api_headers = {
    'Authorization': 'Bearer ' + api_key,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

def add_category(request):
    if request.method == 'POST':
        id = request.POST.get('snipe_id')
        name = request.POST.get('name')
        type = request.POST.get('category_type')
        item_count = request.POST.get('item_count')
        print(f'Checking for {id}, {name}')
        try:
            category = Category.objects.get(snipe_id=id)
        except:
            category = None
        if category is None:
            category = Category(snipe_id=id, name=name, category_type=type, item_count=item_count)
            category.save()
    return "Thanks"

def add_fields(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        fields = request.POST.get('fields').split(',')
        for field in fields:
            category = Category.objects.get(snipe_id=category_id)
            try:
                field_test = CategoryField.objects.get(category=category, name=field)
            except:
                field_test = None
            if field_test is None:
                new_field = CategoryField(category=category, name=field)
                new_field.save()
    return "Thanks"

def category(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
        fields = category.fields.filter(display=True)
        r = requests.get(f'http://172.16.0.7/api/v1/hardware?category_id={category.snipe_id}', headers=api_headers)
        #print(r.json())
        hardware = []
        for row in r.json()['rows']:
            items = []
            for field in fields:
                f = row[field.name]
                if isinstance(f, dict):
                    item = row[field.name]['name']
                else:
                    item = row[field.name]
                items.append(item)
            hardware.append(items)
                #print(row)
            #print("hello")
            #print(hardware)
        return render(request, "category_table.html", {'category_name':category.name, 'fields': fields, 'hardware': hardware})
    except:
        return render(request, "category.html", {'category_name':"Category Not Found."})
