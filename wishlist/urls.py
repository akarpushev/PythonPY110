from django.urls import path

from .views import wishlist_view, wishlist_add_json, wishlist_del_json, wishlist_json

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist_view, name='wishlist'),
    path('wishlist/api/add/', wishlist_add_json),
    path('wishlist/api/del/', wishlist_del_json),
    path('wishlist/api/', wishlist_json),
]