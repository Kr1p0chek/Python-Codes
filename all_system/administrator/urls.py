from django.urls import include, path, re_path

from administrator import views

app_name = 'administrator'

urlpatterns = [
    re_path('employees', views.employees, name='employees'),
    re_path('index.html', include(('user.urls', 'user'), namespace='user')),
    path('add_employee', views.dobavlenie, name='dobavlenie'),
]