from django.shortcuts import render
from django.views.generic import View
from django.http import HttpRequest

class Index(View):
    def get(self, request):
        return render(request, 'sphere/index.html')