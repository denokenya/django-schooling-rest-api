# flake8: noqa

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from faker import Faker
import random
from validate_docbr import CPF
from schooling.models import Student, Course


def create_new_students(quantity_of_students):
    fake = Faker("en_US")
    Faker.seed(10)
    for _ in range(quantity_of_students):
        personal_doc = CPF()
        name = fake.name()
        personal_id = "{}{}{}{}".format(
            random.randrange(10, 99),
            random.randrange(100, 999),
            random.randrange(100, 999),
            random.randrange(0, 9),
        )
        personal_doc = personal_doc.generate()
        birthday = fake.date_between(start_date="-18y", end_date="today")
        student = Student(
            personal_doc=personal_doc,
            personal_id=personal_id,
            name=name,
            birthday=birthday,
        )
        student.save()


def create_new_courses(quantity_of_courses):
    Faker.seed(10)
    for _ in range(quantity_of_courses):
        course_code = "{}{}-{}".format(
            random.choice("ABCDEF"), random.randrange(10, 99), random.randrange(1, 9)
        )
        descriptions = [
            "Python basics",
            "Python intermidiate",
            "Python advanced",
            "Python for data science",
            "Python/React",
        ]
        description = random.choice(descriptions)
        descriptions.remove(description)
        level = random.choice("BIA")
        course = Course(course_code=course_code, description=description, level=level)
        course.save()


create_new_students(200)
create_new_courses(5)
