from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('savebook/', views.savebook, name='LibraryOverview'),
    path('addbook/', views.addbook, name='addbook'),
    path('showbooks/', views.showbooks, name='showbooks'),
    path('displaybooks/', views.displaybooks, name='displaybooks'),
    path('deletedbooks/', views.deletedbooks, name='deletedbooks'),
    path('deletebooks/', views.deletebooks, name='deletebooks'),
    path('updatedbooks/', views.updatedbooks, name='updatedbooks'),
    path('updatebooks/', views.updatebooks, name='updatebooks'),
    path('bookupdate/', views.bookupdate, name='bookupdate'),

]
