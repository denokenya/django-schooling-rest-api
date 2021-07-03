"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from schooling.models import Matriculation
from django.contrib import admin
from django.urls import path, include
from schooling.views import (
    MatriculationsViewSet,
    StudentsViewSet,
    CoursesViewSet,
    MatriculationListStudentCourses,
    MatriculationListStudentsByCourse,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("students", StudentsViewSet, basename="Students")
router.register("courses", CoursesViewSet, basename="Courses")
router.register("matriculations", MatriculationsViewSet, Matriculation)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("students/<int:pk>/matriculations", MatriculationListStudentCourses.as_view()),
    path(
        "courses/<int:pk>/matriculations", MatriculationListStudentsByCourse.as_view()
    ),
]
