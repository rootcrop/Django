from django.shortcuts import render

# для представления index2 нужно наследование от
from django.views.generic import TemplateView

# Create your views here.

### views и url представляют всю логику приложения
### views создаем функции обрабатывающие логику отображения и возвращающие шаблоны отрисовки для пользователя
### url отвечает за обработку пути запроса в браузере

# 1 способ
#def index11(request):                                       # это функция
#    return render(request, 'index11.html')    # шаблон index.html берем в settings.py в TEMPLATES там список

# делаем шаблон через объект
# 2 способ
#class index22(TemplateView):   # наследуемся от базового шаблона в котором своя логика
#    template_name = 'index22.html'

# делаем шаблон через объект TemplateView сразу в urlpatterns
# 3 способ
# здесь ничего писать уже не нужно

#def index11(request):   # функциональное представлениме
#    return render(request, 'second_task/index11.html')    #

class index11(TemplateView):   # объектное представлениме
    template_name = 'second_task/index11.html'

def index22(request):                                       #
    title='my title /// '
    text='мой текст'
    context={'title': title,
             'text':text,
             }
    return render(request, 'second_task/index22.html', context)    #
