from django.http import HttpResponse

def home(request):
    return HttpResponse("Digite uma url qualquer, como: http://127.0.0.1:8000/inexistente")
