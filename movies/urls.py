from django.conf.urls import url
from movies import views


app_name = 'movies'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add_movie/$', views.add_movie.as_view(), name='add_movie'),
    url(r'^(?P<movie_id>[0-9]+)/add_cast/$', views.add_cast, name='add_cast'),
    url(r'^(?P<movie_id>[0-9]+)/add_trivia/$', views.add_trivia, name='add_trivia'),
    url(r'^(?P<movie_id>[0-9]+)/delete_cast/(?P<cast_id>[0-9]+)/$',
        views.delete_cast, name='delete_cast'),
    url(r'^(?P<movie_id>[0-9]+)/update_cast/$',
        views.update_cast, name='update_cast'),
    url(r'^(?P<movie_id>[0-9]+)/delete_trivia/(?P<trivia_id>[0-9]+)/$',
        views.delete_trivia, name='delete_trivia'),
    url(r'^(?P<pk>[0-9]+)/update_movie/$', views.update_movie.as_view(), name='update_movie'),
    url(r'^(?P<movie_id>[0-9]+)/delete_movie/$', views.delete_movie, name='delete_movie'),
]
