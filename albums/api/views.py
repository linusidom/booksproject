from rest_framework import generics
from albums.api.models import AlbumSerializer
from albums.models import Album
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def album_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def album_detail(request, pk):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        albums = Album.objects.filter(pk=pk)
        serializer = AlbumSerializer(albums,many=True)
        return Response(serializer.data)