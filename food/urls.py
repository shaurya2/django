from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

#Namespacing
app_name='food'

urlpatterns = [
    #path('', views.index,name='index'),
    path('',views.IndexClassView.as_view(),name='index'),
    path('item/',views.item,name='item'),
   # path('<int:item_id>/',views.details,name='details'),
    path('<int:pk>/',views.DetaislView.as_view(),name='detail'),
    #Add item
   # path('add',views.create_item,name='create_item'),
    path('add',views.CreateItem.as_view(),name='create_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.item_delete,name='item_delete'),
    



]
