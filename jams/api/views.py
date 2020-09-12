#Go to generic Views in documentaiton
#Concrete View Classes

from rest_framework.generics import ListAPIView, RetrieveAPIView
from jams.models import Jam
from .serializers import JamSerializer

class JamListView(ListAPIView):
    queryset = Jam.objects.all()
    serializer_class = JamSerializer

class JamDetailView(RetrieveAPIView):
    queryset = Jam.objects.all()
    serializer_class = JamSerializer