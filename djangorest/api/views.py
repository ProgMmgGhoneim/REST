from django.shortcuts import render
from rest_framework import generics

from .models import Bucketlist
from .serializers import BucketlistSerializer
# Create your views here.

class CreateView(generics.CreateAPIView):
    queryset =Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
