from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from movie_collections.models import User, Movie, Collection
from movie_collections.serializers import UserSerializer, MovieSerializer, CollectionSerializer
from django.http import JsonResponse
import requests
from django.core.paginator import Paginator
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry



session = requests.Session()
retry = Retry(total=5, backoff_factor=0.1, status_forcelist=[ 500, 502, 503, 504 ])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


def registration(request):
    return render(request, 'registration/registration.html')


def request_count(request):
    request_count = request.session.get('request_count', 0)
    return JsonResponse({'request_count': request_count})


# def movies_list(request):
#     # Get the page number from the query string
#     page_number = request.GET.get('page', 1)

#     # Call the external API
#     url = "https://demo.credy.in/api/v1/maya/movies/"
#     auth = ("iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0", "Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1")
#     response = requests.get(url, auth=auth)
#     data = response.json()

#     # Paginate the results
#     paginator = Paginator(data['data'], 10)
#     movies = paginator.get_page(page_number)

#     return JsonResponse({
#         'count': paginator.count,
#         'next': movies.next_page_number() if movies.has_next() else None,
#         'previous': movies.previous_page_number() if movies.has_previous() else None,
#         'data': movies.object_list
#     })

def movies_list(request):
    # Create a session with retry capabilities
    session = requests.Session()
    retry = Retry(total=5, backoff_factor=0.1, status_forcelist=[ 500, 502, 503, 504 ])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # Get the page number from the query string
    page_number = request.GET.get('page', 1)

    # Call the external API
    url = "https://demo.credy.in/api/v1/maya/movies/"
    auth = ("iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0", "Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1")
    response = session.get(url, auth=auth)
    data = response.json()

    # Paginate the results
    paginator = Paginator(data['data'], 10)
    movies = paginator.get_page(page_number)

    return JsonResponse({
        'count': paginator.count,
        'next': movies.next_page_number() if movies.has_next() else None,
        'previous': movies.previous_page_number() if movies.has_previous() else None,
        'data': movies.object_list
    })


    