# views.py
from django.shortcuts import render, redirect
from .forms import FilmForm
from rest_framework.decorators import api_view
from .models import Film
from .serializers import FilmSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistrer le film dans la base de données
            return redirect('/')  # Rediriger vers la page d'accueil après l'ajout
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

@api_view(['POST'])
def add_film_api(request):
    serializer = FilmSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def convert_to_embed_url(url):
    """
    Convertir une URL YouTube classique en URL d'intégration (embed).
    """
    video_id = url.split('v=')[-1]
    return f'https://www.youtube.com/embed/{video_id}'

@api_view(['GET'])
def film_list(request):
    films = Film.objects.all()
    
    # Convertir chaque URL de vidéo en format d'intégration (embed)
    for film in films:
        film.video_link = convert_to_embed_url(film.video_link)

    serializer = FilmSerializer(films, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def play_film(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    return Response({'title': film.title, 'video_url': film.video_link})
