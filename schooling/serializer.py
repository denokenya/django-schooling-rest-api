from rest_framework import serializers
from schooling.models import Matriculation, Student, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class MatriculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriculation
        exclude = ["id"]


class MatriculationStudentCoursesSerialiazer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source="course.description")
    period = serializers.SerializerMethodField()

    class Meta:
        model = Matriculation
        fields = ["course", "period"]

    def get_period(self, obj):
        return obj.get_period_display()


class MatriculationStudentsByCourseSerialiazer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source="student.name")

    class Meta:
        model = Matriculation
        fields = ["student_name"]


class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "phone_number", "photo"]
