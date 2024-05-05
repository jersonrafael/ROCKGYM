from rest_framework import serializers
from .models import *

class classesSerializer(serializers.ModelSerializer):
	class meta:
		model = classes
		fields = '__all__'

class plainsSerializer(serializers.ModelSerializer):
	class meta:
		model = plains
		fields = '__all__'
