from django.db.models import fields
from django.db.models.fields import files
from rest_framework import serializers
from schooling.models import Matriculation, Student, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class MatriculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriculation
        exclude = ['id']


class MatriculationListStudentCourses(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Matriculation
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()
