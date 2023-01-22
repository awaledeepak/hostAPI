from django.shortcuts import render
from rest_framework import generics 
from .models import Book
from library.serializers import BookSerializer
from rest_framework.filters import SearchFilter

# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    filter_backends = [SearchFilter]
    search_fields = ['id'] 
    

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book
    serializer_class = BookSerializer 
    
    
