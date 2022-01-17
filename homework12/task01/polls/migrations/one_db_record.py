from datetime import datetime, timedelta

from django.db import migrations


class Migration(migrations.Migration):

    def db_recording(apps, schema_editor):
        Homework = apps.get_model("polls", "Homework")
        HomeworkResult = apps.get_model("polls", "HomeworkResult")
        Student = apps.get_model("polls", "Student")
        Teacher = apps.get_model("polls", "Teacher")

        student = Student(first_name="Lev", last_name="Sokolov")
        homework = Homework(
            text="Learn OOP",
            deadline=timedelta(days=7),
            created=datetime.now()
        )
        result = HomeworkResult(
            homework=homework,
            author=student,
            solution="Done",
            created=datetime.now(),
        )
        teacher = Teacher(
            first_name="Daniil",
            last_name="Shadrin",
            homework_done=result
        )

        student.save()
        homework.save()
        result.save()
        teacher.save()

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(db_recording),
    ]
