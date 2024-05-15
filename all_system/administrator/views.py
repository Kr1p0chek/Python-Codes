from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Employes
from .forms import NewEmployeeForm
from django.views.decorators.csrf import csrf_exempt

def employees(request):
    employees_list = Employes.objects.all()  # Получаем список всех жалоб
    page = request.GET.get('page', 1)  # Получаем номер страницы из запроса

    paginator = Paginator(employees_list, 10)  # Создаем Paginator, 10 жалоб на страницу

    try:
        employes = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        employes = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        employes = paginator.page(paginator.num_pages)

    return render(request, 'admintor/employees.html', {'employes': employes})


def dobavlenie(request):
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            # Получаем значение должности из формы
            positionk = form.cleaned_data.get('positionj', 'manager')
            # Преобразуем текстовое значение в булевое
            if (positionk == 'administrator'):
                is_admin = True
            else:
                is_admin = False
            print(is_admin)
            # Создаём новый объект модели с булевым значением
            new_entry = Employes(
                name=form.cleaned_data['name'],
                positionj=is_admin,
                login=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
                email_telephone=form.cleaned_data['email_telephone']
            )
            print(new_entry.positionj)
            # Сохраняем объект в базе данных
            new_entry.save()
            return redirect('admintor/employees')  # Перенаправление на страницу успеха
        else:
            positionk = form.cleaned_data.get('positionj', 'manager')
            # Преобразуем текстовое значение в булево
            is_admin = positionk == 'administrator'
            # Если форма не валидна, создайте объект вручную
            new_entry = Employes(
                name=form.cleaned_data.get('name', 'сотрудник'), # Значение по умолчанию, если поле пустое
                positionj=is_admin,
                login=form.cleaned_data.get('login', 'newemployee'),
                email_telephone=form.cleaned_data.get('email_telephone', ''),
                password=form.cleaned_data.get('password', 'qwerty12345')
            )
            new_entry.save()
            return redirect('admintor/employees') # Перенаправление на страницу успеха
    else:
        form = NewEmployeeForm()
        return render(request, 'admintor/add_employee.html', {'form': form})
