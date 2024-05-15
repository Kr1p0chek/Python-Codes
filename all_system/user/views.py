from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ApplicationForm, FileForm
from common.models import Applications, Files

def index(request):
    return render(request, 'user/index.html')

def user(request):
    return render(request, 'user/user.html') 

def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user/user.html')  # Перенаправление на страницу успеха
        else:
            # Если форма не валидна, создайте объект вручную
            application = Applications(
                application_text=form.cleaned_data.get('application_text', ''),
                prop_solution=form.cleaned_data.get('prop_solution', ''),
                name=form.cleaned_data.get('name', 'anonim'),  # Значение по умолчанию, если поле пустое
                email=form.cleaned_data.get('email', '')
            )
            application.save()
            return render(request, 'user/user.html')  # Перенаправление на страницу успеха
    else:
        form = ApplicationForm()
        return render(request, 'user/user_application.html', {'form': form})
    

def view(request):
    return render(request, 'user/user_view.html')
