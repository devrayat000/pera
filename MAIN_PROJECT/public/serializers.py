from asyncio import Task
from dataclasses import field
from rest_framework import serializers


from .models import announcements, assignments, class_tests, helpwewant


class announcementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = announcements
        fields = '__all__'

class assignmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = assignments
        fields = '__all__'

class classtestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = class_tests
        fields = '__all__'

class helpwewantSerializer(serializers.ModelSerializer):
    class Meta:
        model = helpwewant
        fields = '__all__'


# class DemoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Demo 
#         fields = '__all__'