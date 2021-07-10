from django.test import TestCase
from schooling.models import Student, Course

import datetime


class StudentModelTestCase(TestCase):
    def setUp(self):
        self.today = datetime.date.today()
        self.student = Student.objects.create(
            name="Lucas Vitor",
            personal_id="123456789",
            personal_doc="12345678998",
            birthday=self.today,
            phone_number="1198882253",
        )

    def test_verifier_student_attributes(self):
        """It should gets all attributes inserted up above in student"""
        self.assertEqual("Lucas Vitor", self.student.name)
        self.assertEqual("123456789", self.student.personal_id)
        self.assertEqual("12345678998", self.student.personal_doc)
        self.assertEqual(self.today, self.student.birthday)
        self.assertEqual("1198882253", self.student.phone_number)


class CourseModelTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            course_code="255", description="Computer Science", level="B"
        )

    def test_verifier_course_attributes(self):
        """It should gets all attributes inserted up above in course"""
        self.assertEqual("255", self.course.course_code)
        self.assertEqual("Computer Science", self.course.description)
        self.assertEqual("B", self.course.level)
