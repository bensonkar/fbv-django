from rest_framework import fields, serializers
from fbvApp.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=['id','name','score']