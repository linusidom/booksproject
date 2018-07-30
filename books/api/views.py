from rest_framework import generics
from books.api.models import BookSerializer
from books.models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def book_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def book_detail(request, pk):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        books = Book.objects.filter(pk=pk)
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)