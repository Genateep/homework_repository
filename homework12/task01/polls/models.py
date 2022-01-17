from django.db import models


class Homework(models.Model):
    db_table = "homeworks"

    text = models.TextField(unique=True)
    created = models.DateTimeField()
    deadline = models.DurationField()

    def __str__(self):
        return self.text


class HomeworkResult(models.Model):
    db_table = "homework_results"

    homework = models.ForeignKey(
        "Homework",
        to_field="text",
        on_delete=models.CASCADE
    )
    author = models.ForeignKey("Student", on_delete=models.CASCADE)
    solution = models.CharField(max_length=50)
    created = models.DateTimeField()

    def __str__(self):
        return self.solution


class User(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(User):
    db_table = "students"


class Teacher(User):
    db_table = "teachers"
    homework_done = models.ForeignKey(
        "HomeworkResult",
        on_delete=models.CASCADE
    )
