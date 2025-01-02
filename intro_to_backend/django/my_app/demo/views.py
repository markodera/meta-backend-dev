from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    content = "<html><body>Welcome to liitle lemons</body></html>"
    return HttpResponse(content)