from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from elections.models import Election, Party, Results
from elections.serializers import ElectionSerializer, PartySerializer, ResultsSerializer, ResultsPostSerializer, ElectionPostSerializer

@csrf_exempt
def elections_list(request):
    if request.method == 'GET':
        elections = Election.objects.all()

        year = request.GET.get('year')
        if year:
            elections = elections.filter(year = year)

        place = request.GET.get('place')
        if place:
            elections = elections.filter(place = place)

        chamber_name = request.GET.get('chamberName')
        if chamber_name:
            elections = elections.filter(chamber_name = chamber_name)

        serializer = ElectionSerializer(elections, many=True)
        dataDict = {'data': serializer.data}
        return JsonResponse(dataDict, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ElectionPostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def election_detail(request, id):
    try:
        election = Election.objects.get(id = id)
    except Election.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ElectionSerializer(election)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ElectionPostSerializer(election, data=data)

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
def party_detail(request, id):
    try:
        party = Party.objects.get(id = id)
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
def results_list(request):
    if request.method == 'GET':
        results = Results.objects.all()
        serializer = ResultsSerializer(results, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ResultsPostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def results_detail(request, id):
    try:
        results = Results.objects.get(id = id)
    except Results.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ResultsSerializer(results)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ResultsPostSerializer(results, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        results.delete()
        return HttpResponse(status=204)
