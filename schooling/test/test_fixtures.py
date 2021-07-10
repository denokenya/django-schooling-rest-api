from django.test import TestCase
from schooling.models import Course


class FixtureDataTestCase(TestCase):

    fixtures = ["initial"]

    def test_verify_fixtures_loaded(self):
        math_course = Course.objects.get(pk=1)
        all_courses = Course.objects.all()
        self.assertEquals(math_course.course_code, "Mathematics")
        self.assertEquals(len(all_courses), 2)
