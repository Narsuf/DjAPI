from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from elections.models import Election, Party, Results
from elections.serializers import ElectionSerializer, PartySerializer, ResultsSerializer

@csrf_exempt
def elections_list(request):
    if request.method == 'GET':
        elections = Election.objects.all()
        serializer = ElectionSerializer(elections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ElectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def election_list_filtered_by_place_and_chamber(request, place, chamber_name):
    if request.method == 'GET':
        elections = Election.objects.filter(place=place, chamber_name=chamber_name)
        serializer = ElectionSerializer(elections, many=True)
        return JsonResponse(serializer.data, safe=False)

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
def parties_list(request):
    if request.method == 'GET':
        parties = Party.objects.all()
        serializer = PartySerializer(parties, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PartySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def party_detail(request, name):
    try:
        party = Party.objects.get(name=name)
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

@csrf_exempt
def results_list(request, year, place, chamber_name):
    if request.method == 'GET':
        election = Election.objects.get(year=year, place=place, chamber_name=chamber_name)
        results = Results.objects.filter(election=election)
        serializer = ResultsSerializer(results, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ResultsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def results_detail(request, year, place, chamber_name, name):
    try:
        election = Election.objects.get(year=year, place=place, chamber_name=chamber_name)
        party = Party.objects.get(name=name)
        results = Results.objects.get(election=election, party=party)
    except Results.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ResultsSerializer(results)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ResultsSerializer(results, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        results.delete()
        return HttpResponse(status=204)