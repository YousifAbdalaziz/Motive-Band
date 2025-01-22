from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def pro(request):
    return render(request, 'main.html')