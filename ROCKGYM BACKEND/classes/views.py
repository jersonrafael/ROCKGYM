from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *


# Create your views here.

class classesView(APIView):
	def get(self,request):
		model = classes.objects.all()
		serializer = classesSerializer(model, many=True)
		return Response(serializer.data)


class classView(APIView):
	def get(self,request,pk):
		model = get_object_or_404(classes,id=pk)
		serializer = classesSerializer(model)
		return Response(serializer.data)

	def post(self,request):
		serializer = classesSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

	def patch(self,request,pk):
		model = get_object_or_404(classes, id=pk)
		serializer = classesSerializer(model,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

	def put(self,request,pk):
		model = get_object_or_404(classes, id=pk)
		serializer = classesSerializer(model,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk):
		model =get_object_or_404(classes,id=pk)
		if model == False:
			model.delete()
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class plainsView(APIView):
	def get(self,request):
		model = plains.objects.all()
		serializer = plainsSerializer(model,many=True)
		return Response(serializer.data,status=HTTP_200_OK)

class plainView(APIView):
	
	def get(self,request,pk):
		model = get_object_or_404(plains,id=pk)
		serializer = plainsSerializer(model)
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	def post(self,request):
		serializer = plainsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

	def patch(self,request,pk):
		model = get_object_or_404(plains,id=pk)
		serializer = plainsSerializer(model,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

	def put(self,request,pk):
		model = get_object_or_404(plains, id=pk)
		serializer = classesSerializer(model,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk):
		model =get_object_or_404(plains,id=pk)
		if model == False:
			model.delete()
			return Response(status=status.HTTP_200_OK)
		else:
			print("Deleted")
			return Response(status=status.HTTP_400_BAD_REQUEST)