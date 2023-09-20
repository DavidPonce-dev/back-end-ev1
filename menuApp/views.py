from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class MenuView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        html_content = render(request, 'menuApp/menu-view.html', context)
        return HttpResponse(html_content)