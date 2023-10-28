from rest_framework import generics

from .models import User
from .serializers import ModelSerializer


class ModelListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ModelSerializer
