from django.shortcuts import render
from django.views.generic import View
from django.http import HttpRequest
from .models import City

class Index(View):
    def get(self, request):
        context = {
            'title': 'sphere',
            'cities': City.objects.all()
        }
        return render(request, 'sphere/index.html', context = context)
