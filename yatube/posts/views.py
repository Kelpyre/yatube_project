# posts/views.py

from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    description = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'description': description
    }
    return render(request, template, context)


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Лев Толстой – зеркало русской революции.'
    description = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'description': description
    }
    return render(request, template, context)
