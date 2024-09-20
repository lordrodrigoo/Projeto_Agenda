from django.urls import path

from contact import views

app_name = 'contact'


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # contact (CRUD) create, read, update, delete
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    

]
