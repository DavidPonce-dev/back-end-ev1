from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import random

from .models import Pais

class TablaView(View):
    def get(self, request, *args, **kwargs):
        paises = Pais.objects.all()
        context = {"paises": paises}
        html_content = render(request, "optionApp/tabla-view.html", context)
        return HttpResponse(html_content)


class LoteriaView(View):
    def get(self, request, *args, **kwargs):
        randomList = [random.randint(1, 100) for _ in range(10)]
        context = {"numerosLoteria": sorted(randomList)}
        html_content = render(request, "optionApp/loteria-view.html", context)
        return HttpResponse(html_content)
