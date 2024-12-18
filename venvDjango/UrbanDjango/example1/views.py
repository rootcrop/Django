from django.shortcuts import render

# для представления index2 нужно наследование от
from django.views.generic import TemplateView

# Create your views here.

### views и url представляют всю логику приложения
### views создаем функции обрабатывающие логику отображения и возвращающие шаблоны отрисовки для пользователя
### url отвечает за обработку пути запроса в браузере
# 1 способ
def index(request):                                       # это функция
    return render(request, 'index.html')    # шаблон index.html берем в settings.py в TEMPLATES там список

# делаем шаблон через объект
# 2 способ
class index2(TemplateView):   # наследуемся от базового шаблона в котором своя логика
    template_name = 'index2.html'

# делаем шаблон через объект TemplateView сразу в urlpatterns
# 3 способ
# здесь ничего писать уже не нужно


