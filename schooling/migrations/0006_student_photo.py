# Generated by Django 3.1.3 on 2021-07-07 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("schooling", "0005_student_phone_number")]

    operations = [
        migrations.AddField(
            model_name="student",
            name="photo",
            field=models.ImageField(blank=True, upload_to=""),
        )
    ]