from rest_framework import viewsets, generics
from schooling.models import Matriculation, Student, Course
from schooling.serializer import (
    MatriculationStudentsByCourseSerialiazer,
    MatriculationSerializer,
    StudentSerializer,
    CourseSerializer,
    MatriculationStudentCoursesSerialiazer,
)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    """It shows all the students"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CoursesViewSet(viewsets.ModelViewSet):
    """It shows all courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculationsViewSet(viewsets.ModelViewSet):
    """It shows all the matriculations"""

    queryset = Matriculation.objects.all()
    serializer_class = MatriculationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculationListStudentCourses(generics.ListAPIView):
    """It shows all courses that student is matriculated in"""

    def get_queryset(self):
        queryset = Matriculation.objects.filter(student_id=self.kwargs["pk"])
        return queryset

    serializer_class = MatriculationStudentCoursesSerialiazer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculationListStudentsByCourse(generics.ListAPIView):
    """"It shows all the students matriculated in that course"""

    def get_queryset(self):
        queryset = Matriculation.objects.filter(course_id=self.kwargs["pk"])
        return queryset

    serializer_class = MatriculationStudentsByCourseSerialiazer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
