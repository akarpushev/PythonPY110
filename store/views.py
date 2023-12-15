from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE
#from logic.services import filtering_category

def products_view(request):
    if request.method == "GET":
        if id_product := request.GET.get("id"):
            if data := DATABASE.get(id_product):
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        else:
            data = DATABASE
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        return HttpResponseNotFound("Данного продукта нет в базе данных")

#        id = request.GET.get('id')
#        if id:
#           data = DATABASE[id]
#       else:
#            data = DATABASE

        #elif id != id in DATABASE:
         #   return HttpResponseNotFound("Данного продукта нет в базе данных")
        #else:
         #   data = DATABASE
#        return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        # Вернуть JsonResponse с объектом DATABASE и параметрами отступов и кодировок,
        # как в приложении app_weather


# 1-ый вариант
# def products_page_view(request, page):
#     if request.method == "GET":
#         for data in DATABASE.values():
#             if data['html'] == page:  # Если значение переданного параметра совпадает именем html файла
#                 with open(f'store/products/{page}.html', encoding="utf-8") as f:
#                     data = f.read()
#                 return HttpResponse(data)
#
#         # TODO 1. Откройте файл open(f'store/products/{page}.html', encoding="utf-8") (Не забываем про контекстный менеджер with)
#         # TODO 2. Прочитайте его содержимое
#         # TODO 3. Верните HttpResponse c содержимым html файла
#
#         # Если за всё время поиска не было совпадений, то значит по данному имени нет соответствующей
#         # страницы товара и можно вернуть ответ с ошибкой HttpResponse(status=404)
#         return HttpResponse(status=404)

# 2-ой вариант
def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
            # То, что было ранее для обработки типа slug
            for data in DATABASE.values():
                if data['html'] == page:  # Если значение переданного параметра совпадает именем html файла
                    with open(f'store/products/{page}.html', encoding="utf-8") as f:
                        data = f.read()
                    return HttpResponse(data)
        elif isinstance(page, int):
            data = DATABASE.get(str(page))  # Получаем какой странице соответствует данный id
            if data:  # Если по данному page было найдено значение
                with open(f'store/products/{data["html"]}.html', encoding="utf-8") as f:
                    data = f.read()
                return HttpResponse(data)

                # 1. Откройте файл open(f'store/products/{data["html"]}.html', encoding="utf-8") (Не забываем про контекстный менеджер with)
                # 2. Прочитайте его содержимое
                # 3. Верните HttpResponse c содержимым html файла

        return HttpResponse(status=404)



def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ