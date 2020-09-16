from rest_framework import serializers

from jams.models import Jam

class JamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jam
        fields = ('username', 'title', 'description', 'tempo', 'notes', 'bassDrumNotes', 'cymbalNotes', 'snareNotes')

  