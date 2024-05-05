from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse

from django.shortcuts import get_object_or_404

from classes.models import *
from classes.serializers import *


# Create your views here.