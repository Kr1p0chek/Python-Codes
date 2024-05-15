from django.urls import path, re_path

from manager import views

app_name = 'manager'

urlpatterns = [
    re_path('', views.manager, name='manager'),
    re_path('answer', views.answer, name='answer'),
]