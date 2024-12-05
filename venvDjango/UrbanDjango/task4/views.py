from django.shortcuts import render

from django.views.generic import TemplateView

class index00(TemplateView):   # объектное представлениме
    template_name = 'fourth_task/index00.html'

class platform(TemplateView):
    template_name = 'fourth_task/platform.html'

def games(request):             # функциональное представление
    #game1='Atomic Heart; game2='CyberPunk'; game3='PayDay'
    #context={'game1': game1, 'game2':game2,'game3':game3, }
    # вместо передачи нескольких значений будет передаваться один единый список из этих значений
    #context={'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 77"] }
    context = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 77"]}
    return render(request, 'fourth_task/games.html', context)

class basket(TemplateView):     # объектное представлениме
    template_name = 'fourth_task/basket.html'