from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie, Genre
import random


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres
    }
    return render(request, 'movies/index.html',context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_genres = movie.genres.all()
    context = {
        'movie':movie,
        'genres':movie_genres
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request,recommend_pk):
    # 평점
    # 장르 선택 랜덤 10개

    # 그냥 아 Um.. o..h... Ayeah~~! 랜덤
    if recommend_pk==1:
        nums=random.sample(range(1,101), 10)
        r_movies = []
        for num in nums:
            r_movies.append(Movie.objects.get(pk=num))
    elif recommend_pk==2:
        r_movies=Movie.objects.order_by('-vote_average')[:10]
    elif recommend_pk==3:
        r_movies=Movie.objects.order_by('-release_date')[:10]

    context = {
        'r_movies' : r_movies
    }
    return render(request, 'movies/recommended.html', context)