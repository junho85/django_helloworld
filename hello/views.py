from django.http import HttpResponse

def hello(request):
        return HttpResponse("Hello world")

def index(request):
        return HttpResponse("Home page")
