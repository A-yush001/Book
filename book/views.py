from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions

class BookList(ListCreateAPIView):
    serializer_class=BookSerializer
    permission_classes=(permissions.IsAuthenticated,)
    def perform_created(self,serializer):
        serializer.save()


    