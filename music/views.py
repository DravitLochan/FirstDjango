from django.http import HttpResponse
from .models import Album


def index(request):
    html = ''
    all_albums = Album.objects.all()
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href = "' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2>Details for album id " + album_id + "</h2>")