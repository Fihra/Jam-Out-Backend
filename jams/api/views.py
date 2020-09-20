from jams.models import Jam
from .serializers import JamSerializer

from rest_framework import viewsets

class JamViewSet(viewsets.ModelViewSet):
    serializer_class = JamSerializer
    queryset = Jam.objects.all()

# from rest_framework.generics import (
#     ListAPIView, 
#     RetrieveAPIView,
#     CreateAPIView,
#     DestroyAPIView,
#     UpdateAPIView
# )

# class JamListView(ListAPIView):
#     queryset = Jam.objects.all()
#     serializer_class = JamSerializer

# class JamDetailView(RetrieveAPIView):
#     queryset = Jam.objects.all()
#     serializer_class = JamSerializer

# class JamCreateView(CreateAPIView):
#     queryset = Jam.objects.all()
#     serializer_class = JamSerializer

# class JamUpdateView(UpdateAPIView):
#     queryset = Jam.objects.all()
#     serializer_class = JamSerializer
    
# class JamDeleteView(DestroyAPIView):
#     queryset = Jam.objects.all()
#     serializer_class = JamSerializer        