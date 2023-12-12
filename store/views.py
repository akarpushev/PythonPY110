from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE

def products_view(request):
    if request.method == "GET":
        id = request.GET.get('id')
        if id:
            data = DATABASE[id]
        else:
            data = DATABASE

        #elif id != id in DATABASE:
         #   return HttpResponseNotFound("Данного продукта нет в базе данных")


        #else:
         #   data = DATABASE

        return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})



        # Вернуть JsonResponse с объектом DATABASE и параметрами отступов и кодировок,
        # как в приложении app_weather



def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ