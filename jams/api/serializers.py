from rest_framework import serializers

from jams.models import Jam

class JamSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Jam
        fields = ('id', 'username', 'title', 'description', 'tempo', 'notes', 'bassDrumNotes', 'cymbalNotes', 'snareNotes')

  