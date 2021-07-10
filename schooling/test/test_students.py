from rest_framework.test import APITestCase
from schooling.models import Student
from django.urls import reverse
from rest_framework import status

import datetime


class CoursesTestCase(APITestCase):
    def setUp(self):
        self.list_urls = reverse("Students-list")
        self.student_1 = Student.objects.create(
            name="Gabriel Ahnzalm",
            personal_id="458235628",
            personal_doc="07696905058",
            birthday=datetime.date.today(),
            phone_number="1195684265",
        )
        self.student_2 = Student.objects.create(
            name="Alexia Gokdwan",
            personal_id="145968257",
            personal_doc="41716548071",
            birthday=datetime.date.today(),
            phone_number="1185462565",
        )

    def test_request_get_all_students(self):
        """"It should get all students at the GET HTTP request"""
        response = self.client.get(self.list_urls)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_a_student(self):
        """"It should create a new student at the database"""
        data = {
            "name": "Lucas Cicco",
            "personal_id": "123456789",
            "personal_doc": "41142765059",
            "birthday": datetime.date.today(),
            "phone_number": "11947016590",
        }
        response = self.client.post(self.list_urls, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete_a_student(self):
        """"It should delete a student"""
        response = self.client.delete("/students/1/")
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_request_update_a_student(self):
        """"It should update an existent student"""
        data = {
            "name": "Gabriel Iwsasy",
            "personal_id": "589542645",
            "personal_doc": "22239256001",
            "birthday": datetime.date.today(),
            "phone_number": "1195684265",
        }
        response = self.client.put("/students/1/", data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
