from rest_framework.test import APITestCase
from schooling.models import Student, Course, Matriculation
from django.urls import reverse
from rest_framework import status

import datetime


class MatriculationsTestCase(APITestCase):
    def setUp(self):
        self.list_urls = reverse("Matriculations-list")
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

    def test_request_get_all_matriculations(self):
        """"It should get all matriculations at the GET HTTP request"""
        response = self.client.get(self.list_urls)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_a_matriculation(self):
        """"It should fail on trying to delete a matriculation"""
        response = self.client.delete("/matriculations/1/")
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
