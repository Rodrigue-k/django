
from django.shortcuts import render

def views_test(request):
    return render(request, "index.html")
