
from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns=[
    path('home',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('list_item/',views.list_item,name='list_item'),
    path('add_item/',views.add_item,name='add_item'),
    path('<id>/delete_view',views.delete_view,name='delete_view'),
    path('stock_detail/<id>/', views.stock_detail, name="stock_detail"),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),]