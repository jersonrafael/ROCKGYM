from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *


# Create your views here.

class clientsView(APIView):

	def get(self,request):
		model = client.objects.all()
		serializer = clientSerializer(model,many=True)
		return Response(serializer.data)


class clientView(APIView):

	def get(self,request,pk):
		model = get_object_or_404(client,id=pk)
		serializer = clientSerializer(model)
		return Response(serializer.data)

	def post(self,request):
		serializer = clientSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

	def patch(self,request,pk):
		model = get_object_or_404(client, id=pk)
		serializer = clientSerializer(model,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

	def put(self,request,pk):
		model = get_object_or_404(client, id=pk)
		serializer = clientSerializer(model,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk):
		model =get_object_or_404(client,id=pk)
		if model == False:
			model.delete()
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)