from django import test
from django.test import TestCase
from schooling.models import Student
from schooling.serializer import StudentSerializer

import datetime


class StudentSerializerTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            name="Lucas Vitor",
            personal_id="123456789",
            personal_doc="12345678998",
            birthday=datetime.date.today(),
            phone_number="1198882253",
        )
        self.serializer = StudentSerializer(instance=self.student)

    def test_verify_serialized_fields(self):
        """Test verifies the fields that are being serialized"""
        data = self.serializer.data
        print(self.student)
        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "photo",
                    "personal_id",
                    "name",
                    "birthday",
                    "phone_number",
                    "personal_doc",
                ]
            ),
        )
