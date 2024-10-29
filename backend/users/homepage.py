from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Bienvenue sur Learn and Films!")

