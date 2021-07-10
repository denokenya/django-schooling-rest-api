from rest_framework.test import APITestCase
from schooling.models import Course
from django.urls import reverse
from rest_framework import status


class CoursesTestCase(APITestCase):
    def setUp(self):
        self.list_urls = reverse("Courses-list")
        self.course_1 = Course.objects.create(
            course_code="CTT1",
            description="Testing course at this time CTT1",
            level="A",
        )
        self.course_2 = Course.objects.create(
            course_code="CTT2",
            description="Testing course at this time CTT2",
            level="B",
        )

    def test_request_get_all_courses(self):
        """"It should get all courses at the GET HTTP request"""
        response = self.client.get(self.list_urls)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_a_course(self):
        """"It should create a new course at the database"""
        data = {
            "course_code": "CTT2",
            "description": "Testing course at this time CTT2",
            "level": "I",
        }
        response = self.client.post(self.list_urls, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete_a_course(self):
        """"It should fail on trying to delete a course"""
        response = self.client.delete("/courses/1/")
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_request_update_a_course(self):
        """"It should update an existent course"""
        data = {
            "course_code": "CTT1",
            "description": "CTT1 is updated over this request now",
            "level": "I",
        }
        response = self.client.put("/courses/1/", data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
