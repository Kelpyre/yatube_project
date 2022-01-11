from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    discription = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'discription': discription
    }
    return render(request, template, context)


def group_posts(request, slug):
    return HttpResponse(f'Группа постов {slug}')


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Лев Толстой – зеркало русской революции.'
    discription = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'discription': discription
    }
    return render(request, template, context)
