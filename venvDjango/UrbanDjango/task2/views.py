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

def index22(request): # в html вставляем : {{ text }}
    title='my title /// '
    text='мой текст'
    context={'title': title,
             'text':text,
             }
    return render(request, 'second_task/index22.html', context)

def index31(request):   # вывод DTL
    name=' \|\ Вася /|/'
    title='index31 // django DTL: переменные'
    text='мой текст'
    list = ['aAa', 'bb', 'cc']
    len_list=len(list)
    context={'name': name,
             'text':text,
             'list':list,
             'len_list':len_list,
             'title':title,
             }
    return render(request, 'second_task/index31.html', context)

def index32(request):   # вывод dtl, css, static
    name='q'
    title='index32 // django DTL: css, static '
    text='мой текст'
    list = ['aAa', 'bb', 'cc']
    len_list=len(list)
    context={'name': name,
             'text':text,
             'list':list,
             'len_list':len_list,
             'title':title,
             }
    return render(request, 'second_task/index32.html', context)

def index33(request):   # Подключение и наследование шаблонов.
    name='q'
    title='django : Подключение и наследование шаблонов '
    text='мой текст'
    list = ['aAa', 'bb', 'cc']
    len_list=len(list)
    context={'name': name,
             'text':text,
             'list':list,
             'len_list':len_list,
             'title':title,
             }
    return render(request, 'second_task/index33.html', context)

def index333(request):   # наследование
     return render(request, 'second_task/index333.html',)