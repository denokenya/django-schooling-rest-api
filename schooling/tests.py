from django.test import TestCase
from schooling.models import Student, Course

import datetime


class TestModels(TestCase):
    def test_student(self):
        today = datetime.date.today()
        student = Student.objects.create(
            name="Lucas Vitor",
            personal_id="123456789",
            personal_doc="12345678998",
            birthday=today,
            phone_number="1198882253",
        )
        student_1 = Student.objects.get(pk=student.id)
        self.assertEqual("Lucas Vitor", student_1.name)
        self.assertEqual("123456789", student_1.personal_id)
        self.assertEqual("12345678998", student_1.personal_doc)
        self.assertEqual(today, student_1.birthday)
        self.assertEqual("1198882253", student_1.phone_number)

    def test_course(self):
        course = Course.objects.create(
            course_code="255", description="Computer Science", level="B"
        )
        course_1 = Course.objects.get(pk=course.id)
        self.assertEqual("255", course_1.course_code)
        self.assertEqual("Computer Science", course_1.description)
        self.assertEqual("B", course_1.level)
