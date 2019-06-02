from django.contrib import admin

from .models import Movie, Cast, Trivia

admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(Trivia)
