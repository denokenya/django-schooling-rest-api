# Generated by Django 3.1.3 on 2021-07-07 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("schooling", "0003_alter_student_personal_doc")]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="matriculation",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
