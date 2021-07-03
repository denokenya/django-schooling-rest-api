from django.test import TestCase
from schooling.models import Student, Course

import datetime


class TestModels(TestCase):
    def test_student(self):
        today = datetime.date.today()
        student = Student.objects.create(
            name="Lucas Vitor",
            personal_id="1223456789",
            personal_doc="12345678998",
            birthday=today,
        )
        inserted_student = Student.objects.get(pk=student.id)
        self.assertEqual("Lucas Vitor", inserted_student.name)
        self.assertEqual("1223456789", inserted_student.personal_id)
        self.assertEqual("12345678998", inserted_student.personal_doc)
        self.assertEqual(today, inserted_student.birthday)

    def test_course(self):
        course = Course.objects.create(
            course_code="255", description="Computer Science", level="B"
        )
        inserted_course = Course.objects.get(pk=course.id)
        self.assertEqual("255", inserted_course.course_code)
        self.assertEqual("Computer Science", inserted_course.description)
        self.assertEqual("B", inserted_course.level)
