
from django.urls import path , include
from . views import *

urlpatterns = [
    path('' , home , name = "isms_dashboard"),

    # category
    path('category_dashboard' , category_dashboard , name = 'category_dashboard'),
    path('new_category' , new_category , name = 'new_category'),
    path('view_category/<int:id>' , view_category , name = 'view_category'),
    path('update_category/<int:id>' , update_category , name = 'update_category'),

    # item
    path('item_dashboard' , item_dashboard , name = 'item_dashboard'),
    path('new_item' , new_item , name = 'new_item'),
]


