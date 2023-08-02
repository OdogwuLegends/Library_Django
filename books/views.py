from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import BookSerializer, AuthorSerializer, CreateAuthorSerializer, CreateBooKSerializer
from rest_framework import status
from .models import Author, Book


# Create your views here.

#             Function-Based view

# def welcome(requests):
#     return HttpResponse("Welcome to semicolon library!")
#
#
# def my_render(request):
#     query_set = Author.objects.all()
#     return render(request, 'books/welcome.html', {"authors": list(query_set)})
#
#
# def get_by_index(request):
#     query_set = Author.objects.get(pk=1)
#     query_set = Author.objects.filter(first_name__contains="sea")
#     return render(request, 'books/welcome.html', {"authors": list(query_set)})
#
#
# def find_by_id(request, id):
#     return HttpResponse(id)

#
# @api_view()
# def book_list(request):
#     queryset = Book.objects.all()
#     serializer = BookSerializer(queryset, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

#
# @api_view()
# def author_list(request):
#     queryset = Author.objects.all()
#     serializer = AuthorSerializer(queryset, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

#
# @api_view()
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     serializer = AuthorSerializer(author)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view()
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     serializer = BookSerializer(book)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# OR
#
# @api_view()
# def book_detail(request, pk):
#     try:
#         book = Book.objects.get(Book, pk=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except:
#         return Response(status=404)
#
# users = [
#     {"name": "sheriff"},
#     {"name": "Ned"},
#     {"name": "sher"},
# ]
#
# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         queryset = Book.objects.select_related('author').all()
#         serializer = BookSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateBooKSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = CreateBooKSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         query_set = Author.objects.all()
#         serializer = AuthorSerializer(query_set, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     if request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#                            Class Based View

# class BookList(APIView):
#     def get(self, request):
#         queryset = Book.objects.select_related('author').all()
#         serializer = BookSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = CreateBooKSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookList(ListCreateAPIView):
    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class BookDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = CreateBooKSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorList(APIView):
    def get(self, request):
        query_set = Author.objects.all()
        serializer = AuthorSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateAuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuthorDetail(APIView):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = CreateAuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
