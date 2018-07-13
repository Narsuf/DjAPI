from rest_framework import serializers
from elections.models import GeneralInformation

class GeneralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInformation
        fields = ('id','chamber_name','place','year','census','scrutinized','valid_votes','abstentions','blank_votes','null_votes')