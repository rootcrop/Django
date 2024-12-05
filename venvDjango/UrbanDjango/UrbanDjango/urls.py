"""
URL configuration for UrbanDjango project. The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.2/topics/http/urls/   Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))           """
from django.contrib import admin
from django.urls import path

# from task4.views import *         # импортируем все
from task4.views import index00     # главная страница // заглушка // объектное представление # views.py : class index00(TemplateView): template_name = 'third_task/index00.html'
from task4.views import platform    # platform // магазин
from task4.views import games       # shop
from task4.views import basket      # basket

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index00.as_view(template_name='third_task/index00.html')),     # главная страница // заглушка
    path('platform', platform.as_view()),            #
    path('shop', games),
    path('basket', basket.as_view()),
    ]

'''
from example1.views import index    #1 способ #главная страница index это функция, которую нужно импортировать
from example1.views import index2   #2 способ #уже как класс
from django.views.generic import TemplateView   #3 способ: из views импортировать TemplateView и создавать класс сразу в urlpatterns

from task2.views import index11     # вывод html
from task2.views import index22     #
from task2.views import index31     # вывод DTL
from task2.views import index32     # вывод dtl, css, static
from task2.views import index33     # Подключение и наследование шаблонов
from task2.views import index333     # Подключение и наследование шаблонов

from task3.views import index00     # главная страница // заглушка
from task3.views import index01     # магазин
from task3.views import index02
from task3.views import index03

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index00.as_view(template_name='third_task/index00.html')),     # главная страница // заглушка
    path('platform', index01.as_view() ),                                   # домашняя страница магазина
    path('shop', index02),
    path('basket', index03.as_view()),
    path('1', index11.as_view() ),  # вывод html
    path('2', index22 ),            #
    path('3', index),               # index это функция, которую нужно импортировать
    path('31', index31),            # django DTL: переменные, условия, циклы
    path('32', index32),            # DTL. css, static
    path('33', index33),            # Подключение и наследование шаблонов // include
    path('333', index333),          # Подключение и наследование шаблонов.
    path('4', index2.as_view()),    # это уже не функция, а класс, поэтому нужен метод as_view
    path('5', TemplateView.as_view(template_name='index3.html')),   # способ без views.py, с созданием объекта сразу же
]
'''