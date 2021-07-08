from rest_framework import status, viewsets, generics
from schooling.models import Matriculation, Student, Course
from schooling.serializer import (
    MatriculationStudentsByCourseSerialiazer,
    MatriculationSerializer,
    StudentSerializer,
    CourseSerializer,
    MatriculationStudentCoursesSerialiazer,
    StudentSerializerV2,
)
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class StudentsViewSet(viewsets.ModelViewSet):
    """It shows all the students"""

    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.version == "v2":
            return StudentSerializerV2
        else:
            return StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """It shows all courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data["id"])
            response["Location"] = request.build_absolute_uri() + id
            return response


class MatriculationsViewSet(viewsets.ModelViewSet):
    """It shows all the matriculations"""

    queryset = Matriculation.objects.all()
    serializer_class = MatriculationSerializer
    http_method_names = ["get", "post", "put", "path"]

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(MatriculationsViewSet, self).dispatch(*args, **kwargs)


class MatriculationListStudentCourses(generics.ListAPIView):
    """It shows all courses that student is matriculated in"""

    def get_queryset(self):
        queryset = Matriculation.objects.filter(student_id=self.kwargs["pk"])
        return queryset

    serializer_class = MatriculationStudentCoursesSerialiazer


class MatriculationListStudentsByCourse(generics.ListAPIView):
    """"It shows all the students matriculated in that course"""

    def get_queryset(self):
        queryset = Matriculation.objects.filter(course_id=self.kwargs["pk"])
        return queryset

    serializer_class = MatriculationStudentsByCourseSerialiazer
