from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from general_information.models import GeneralInformation
from general_information.serializers import GeneralInformationSerializer

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
def general_information_detail(request, pk):
    try:
        general_information = GeneralInformation.objects.get(pk=pk)
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