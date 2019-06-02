from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import CastForm, TriviaForm
from .models import Movie, Cast, Trivia
from django.views.generic.edit import CreateView, UpdateView


class add_movie(CreateView):
    model = Movie
    fields = ['director', 'movie_title', 'genre', 'movie_art']
    template_name = 'movies/add_movie.html'


class update_movie(UpdateView):
    model = Movie
    fields = ['director', 'movie_title', 'genre', 'movie_art']
    template_name = 'movies/update_movie.html'


def add_cast(request, movie_id):
    form = CastForm(request.POST or None)
    movie = get_object_or_404(Movie, pk=movie_id)
    if form.is_valid():
        movies_casts = movie.cast_set.all()
        for s in movies_casts:
            if s.cast_name == form.cleaned_data.get("cast_name"):
                context = {
                    'movie': movie,
                    'form': form,
                    'error_message': 'You already added this cast',
                }
                return render(request, 'movies/add_cast.html', context)
        cast = form.save(commit=False)
        cast.movie = movie
        cast.save()
        return render(request, 'movies/detail.html', {'movie': movie})
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/add_cast.html', context)


def update_cast(request, movie_id, template_name='update_cast.html'):
    form = CastForm(request.POST or None)
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.POST and form.is_valid():
        form.save()

        # Save was successful, so redirect to another page
        redirect_url = reverse('movies/detail.html')
        return redirect(redirect_url)

    return render(request, 'movies/update_cast.html', {
        'movie': movie,
        'form': form,
    })


def add_trivia(request, movie_id):
    form = TriviaForm(request.POST or None)
    movie = get_object_or_404(Movie, pk=movie_id)
    if form.is_valid():
        movies_trivias = movie.trivia_set.all()
        for t in movies_trivias:
            if t.trivia_details == form.cleaned_data.get("trivia_details"):
                context = {
                    'movie': movie,
                    'form': form,
                    'error_message': 'You already added this cast',
                }
                return render(request, 'movies/add_trivia.html', context)
        cast = form.save(commit=False)
        cast.movie = movie
        cast.save()
        return render(request, 'movies/detail.html', {'movie': movie})
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/add_trivia.html', context)


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return render(request, 'movies/index.html')


def delete_cast(request, movie_id, cast_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    cast = Cast.objects.get(pk=cast_id)
    cast.delete()
    return render(request, 'movies/detail.html', {'movie': movie})


def delete_trivia(request, movie_id, trivia_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    trivia = Trivia.objects.get(pk=trivia_id)
    trivia.delete()
    return render(request, 'movies/detail.html', {'movie': movie})


def detail(request, movie_id):

    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


def index(request):

    movies = Movie.objects.filter()
    return render(request, 'movies/index.html', {'movies': movies})
