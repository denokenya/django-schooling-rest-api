from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from schooling.models import Student, Course, Matriculation
from django.urls import reverse
from rest_framework import status

import datetime


class MatriculationsTestCase(APITestCase):
    def setUp(self):
        self.list_urls = reverse("Matriculations-list")
        self.user = User.objects.create_user("c3po", password="123456")
        self.student = Student.objects.create(
            name="Gabriel Ahnzalm",
            personal_id="458235628",
            personal_doc="07696905058",
            birthday=datetime.date.today(),
            phone_number="1195684265",
        )
        self.course = Course.objects.create(
            course_code="CTT1",
            description="Testing course at this time CTT1",
            level="A",
        )
        self.matriculation = Matriculation.objects.create(
            student=Student(self.student.id), course=Course(self.course.id), period="A"
        )

    def test_delete_a_matriculation(self):
        """"It should fail on trying to delete a matriculation"""
        self.client.force_authenticate(self.user)
        response = self.client.delete("/matriculations/1/")
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
