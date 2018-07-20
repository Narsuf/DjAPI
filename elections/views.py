from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from elections.models import GeneralInformation, Party
from elections.serializers import GeneralInformationSerializer, PartySerializer

@csrf_exempt
def general_information_list(request):
    if request.method == 'GET':
        general_information = GeneralInformation.objects.all()
        serializer = GeneralInformationSerializer(general_information, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GeneralInformationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def general_information_detail(request, year, place, chamber_name):
    try:
        general_information = GeneralInformation.objects.get(year=year, place=place, chamber_name=chamber_name)
    except GeneralInformation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GeneralInformationSerializer(general_information)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GeneralInformationSerializer(general_information, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        general_information.delete()
        return HttpResponse(status=204)

@csrf_exempt
def party_list(request, year, place, chamber_name):
    if request.method == 'GET':
        party = Party.objects.filter(year=year, place=place, chamber_name=chamber_name)
        serializer = PartySerializer(party, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PartySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def party_detail(request, year, place, chamber_name, color):
    try:
        party = Party.objects.get(year=year, place=place, chamber_name=chamber_name, color=color)
    except Party.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PartySerializer(party)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PartySerializer(party, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        party.delete()
        return HttpResponse(status=204)
