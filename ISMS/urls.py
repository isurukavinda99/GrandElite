
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
    path('view_item/<int:id>' , view_item , name = 'view_item'),
    path('update_item/<int:id>' , update_item , name = 'update_item'),
    path('delete_item/<int:id>', delete_item , name='delete_item'),
    path('generate_item_report', generate_item_pdf, name ='generate_item_pdf'),

    #suppler
    path('suppler_dashboard' , suppler_list , name='suppler_list'),
    path('new_suppler' , new_suppler , name = 'new_suppler'),
    path('view_suppler/<int:id>' , view_suppler , name = 'view_suppler'),
    path('update_suppler/<int:id>' , update_suppler , name = 'update_suppler'),
    path('delete_suppler/<int:id>' , delete_suppler , name = 'delete_suppler'),
]

