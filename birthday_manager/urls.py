from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name="index"),
    path('contacts/', views.Contacts.as_view(), name="contacts"),
    path('add/', views.PersonCreate.as_view(), name='add'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('found/', views.SuccessSearching.as_view(), name='found'),
    path('<int:pk>/success/', views.SuccessAdding.as_view(), name='success')
]