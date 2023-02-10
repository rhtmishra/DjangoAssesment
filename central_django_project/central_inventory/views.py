from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import status
from .serializer import SiteSerializer, IAPSerializer, SwitchSerializer, OrderSerializer
from central_inventory.models import *

# def index(request):
#     return HttpResponse("Here I am at views")
class site_list(APIView):
    def get(self, request, format=None):
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        sites = request.data
        serializer = SiteSerializer(data=sites)
        if serializer.is_valid():
            serializer.save()
            return Response('sites successfully added')
        return Response("Not workiing")

    def put(self, request, format=None):
        pk = request.query_params.get('site_id', None)
        if pk:
            site = Site.objects.get(pk=pk)
            serializer = SiteSerializer(instance=site, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response('sites Updated')
            else :
             return Response('Serializer Invalid')
        else:
            return Response('Key is Invalid')
    
    def patch(self, request, format=None):
        pk = request.query_params.get('site_id', None)
        if pk:
            site = Site.objects.get(pk=pk)
            serializer = SiteSerializer(instance=site, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response('sites Updated Partially')
        

    def delete(self, request, format=None):
        pk = request.query_params.get('site_id', None)
        site = Site.objects.get(pk=pk).delete()
        return Response('sites Deleted')
