from django.shortcuts import render
from common.models import Applications
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def manager(request):
    applications_list = Applications.objects.all()  # Получаем список всех жалоб
    page = request.GET.get('page', 1)  # Получаем номер страницы из запроса

    paginator = Paginator(applications_list, 10)  # Создаем Paginator, 10 жалоб на страницу

    try:
        applications = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        applications = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        applications = paginator.page(paginator.num_pages)

    return render(request, 'manag/manager.html', {'applications': applications})


def answer(request):
    return render(request, 'manag/answer.html')
