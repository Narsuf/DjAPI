from rest_framework import serializers
from elections.models import Election, Party, Results

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = ('id', 'year', 'name', 'place', 'chamber_name', 'total_elects', 'scrutinized', 'valid_votes', 'abstentions', 'blank_votes', 'null_votes')

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('name', 'color')

class ResultsSerializer(serializers.ModelSerializer):
    party = PartySerializer()

    class Meta:
        model = Results
        fields = ('id', 'elects', 'votes', 'party', 'election')
