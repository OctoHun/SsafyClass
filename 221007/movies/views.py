from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


def index(request):
    movies = Movie.objects.all()
    context={
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = MovieForm(request.POST)
            if forms.is_valid:
                movie = forms.save(commit=False)
                movie.author = request.user
                movie.save()
                return redirect('movies:detail', movie.pk)
        else:
            forms = MovieForm()
        context = {
            'forms': forms,
        }
    else:
        return redirect('accounts:login')
    return render(request, 'movies/create.html', context)
    

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == movie.author:
            if request.method == 'POST':
                forms = MovieForm(request.POST, instance=movie)
                if forms.is_valid:
                    forms.save()
                    return redirect('movies:detail', movie.pk)
            else:
                forms = MovieForm(instance=movie)
            context = {
                'forms': forms,
                'movie': movie,
            }
        else:
            return redirect('movies:index')
    else:
        return redirect('accounts:login')
    return render(request, 'movies/update.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == movie.author:
            if request.method == 'POST':
                movie.delete()
    else:
        redirect('account:login')
    return redirect('movies:index')