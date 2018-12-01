from rest_framework import serializers
from elections.models import Election, Party, PartyElection

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = ('year', 'name', 'place', 'chamber_name', 'total_elects', 'scrutinized', 'valid_votes', 'abstentions', 'blank_votes', 'null_votes')

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('name', 'color')

class PartyElectionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PartyElection
        fields = ('elects', 'votes', 'party', 'election')