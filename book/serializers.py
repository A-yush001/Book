from rest_framework.serializers import ModelSerializer
from .models import Book

class BookSerializer( ModelSerializer):

    class Meta:
        model=Book

        fields=['name','number','email','date']