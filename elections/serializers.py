from rest_framework import serializers
from elections.models import GeneralInformation, Party

class GeneralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInformation
        fields = ('id','chamber_name','place','year','census','scrutinized','valid_votes','abstentions','blank_votes','null_votes')

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'name', 'elects', 'votes', 'color', 'chamber_name','place','year')