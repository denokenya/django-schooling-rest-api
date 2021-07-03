from django.db.models import query
from rest_framework import viewsets, generics
from schooling.models import Matriculation, Student, Course
from schooling.serializer import MatriculationSerializer, StudentSerializer, CourseSerializer, MatriculationListStudentCourses


class StudentsViewSet(viewsets.ModelViewSet):
    """It shows all the students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """It shows all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class MatriculationsViewSet(viewsets.ModelViewSet):
    """It shows all the matriculations"""
    queryset = Matriculation.objects.all()
    serializer_class = MatriculationSerializer


class MatriculationListStudentCourses(generics.ListAPIView):
    """It shows all courses that student is matriculated in"""
    def get_queryset(self):
        queryset = Matriculation.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = MatriculationListStudentCourses