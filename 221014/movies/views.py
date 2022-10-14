from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MovieForm(request.POST)
            if form.is_valid:
                movie = form.save(commit=False)
                movie.user_id = request.user
                movie.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm()
        context = {
            'form': form,
        }
        return render(request, 'movies/create.html', context)
    return redirect('accounts:login')


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    form = CommentForm()
    comments = Comment.objects.filter(movie_id=pk)
    context = {
        'movie': movie,
        'form': form,
        'comments': comments
    }
    return render(request, 'movies/detail.html', context)


def update(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        if request.user == movie.user_id:
            if request.method == 'POST':
                form = MovieForm(request.POST, instance=movie)
                if form.is_valid:
                    form.save()
                    return redirect('movies:detail', pk)
            else:
                form = MovieForm(instance=movie)
            context = {
                'form': form,
                'movie': movie
            }
            return render(request, 'movies/update.html', context)
    return redirect('accounts:login')


def delete(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        if request.user == movie.user_id:
            movie.delete()
            return redirect('movies:index')
    return redirect('accounts:login')


def comments_create(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user_id = request.user
            comment.movie_id = movie
            comment.save()
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')


def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        if request.user == movie.user_id:
            comment = Comment.objects.get(pk=comment_pk)
            comment.delete()
    return redirect('movies:detail', movie_pk)
        