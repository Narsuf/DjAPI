from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from elections.models import Election, Party, PartyElection
from elections.serializers import ElectionSerializer, PartySerializer, PartyElectionSerializer

@csrf_exempt
def election_list(request):
    if request.method == 'GET':
        election = Election.objects.all()
        serializer = ElectionSerializer(election, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ElectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def election_detail(request, year, place, chamber_name):
    try:
        election = Election.objects.get(year=year, place=place, chamber_name=chamber_name)
    except Election.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ElectionSerializer(election)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ElectionSerializer(election, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        election.delete()
        return HttpResponse(status=204)

@csrf_exempt
def party_election_list(request, year, place, chamber_name):
    if request.method == 'GET':
        election = Election.objects.filter(year=year, place=place, chamber_name=chamber_name)
        partyElection = PartyElection.objects.filter(election=election)
        serializer = PartyElectionSerializer(partyElection, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PartySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def party_election_detail(request, year, place, chamber_name, name):
    try:
        partyElection = PartyElection.objects.filter(year=election.year, place=election.place, chamber_name=election.chamber_name, name=party.name)
    except Party.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PartyElectionSerializer(partyElection)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PartyElectionSerializer(partyElection, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        partyElection.delete()
        return HttpResponse(status=204)

@csrf_exempt
def party_detail(request, name, color):
    try:
        party = Party.objects.get(name=name, color=color)
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