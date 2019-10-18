from rest_framework import serializers
from elections.models import Election, Party, Results

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('__all__')

class ResultsSerializer(serializers.ModelSerializer):
    party = PartySerializer()

    class Meta:
        model = Results
        fields = ('elects', 'votes', 'party')

class ElectionSerializer(serializers.ModelSerializer):
    results = ResultsSerializer(source='results_set', many=True)

    class Meta:
        model = Election
        fields = ('__all__')
