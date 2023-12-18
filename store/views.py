from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE
from logic.services import filtering_category

def products_view(request):
    if request.method == "GET":
        if id_product := request.GET.get("id"):
            if data := DATABASE.get(id_product):
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
            return HttpResponseNotFound("Данного продукта нет в базе данных")
        else:
            data = DATABASE
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        # return HttpResponseNotFound("Данного продукта нет в базе данных")

        # Обработка фильтрации из параметров запроса
    if category_key := request.GET.get("category"):  # Считали 'category'
        if ordering_key := request.GET.get("ordering"):  # Если в параметрах есть 'ordering'
            if request.GET.get("reverse") in ('true', 'True'):  # Если в параметрах есть 'ordering' и 'reverse'=True
                data = filtering_category(DATABASE, category_key, ordering_key, reverse=True)
                # TODO Провести фильтрацию с параметрами
            else:
                data = filtering_category(DATABASE, category_key, ordering_key, reverse=False)
                # TODO Провести фильтрацию с параметрами
        else:
            data = filtering_category(DATABASE, category_key, ordering_key)
            # TODO Провести фильтрацию с параметрами
        # В этот раз добавляем параметр safe=False, для корректного отображения списка в JSON
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False,
                                                                 'indent': 4})

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