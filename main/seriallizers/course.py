from rest_framework import serializers
from main.models import Course

class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор представление модели Course"""
    class Meta:
        model = Course
        fields = '__all__'