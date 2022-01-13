from django.test import TestCase

from polls.models import Homework, HomeworkResult, Student, Teacher


class UserTest(TestCase):
    fixtures = ["fixture.json"]

    def test_student(self):
        student = Student.objects.get(id=1)
        self.assertEqual(student.first_name, "Lev")
        self.assertEqual(student.last_name, "Sokolov")

    def test_teacher(self):
        teacher = Teacher.objects.get(id=1)
        self.assertEqual(teacher.first_name, "Daniil")
        self.assertEqual(teacher.last_name, "Shadrin")
        self.assertEqual(teacher.homework_done.id, 1)


class HomeworkTest(TestCase):
    fixtures = ["fixture.json"]

    def test_homework(self):
        homework = Homework.objects.get(id=1)
        self.assertEqual(homework.text, "Learn OOP")
        self.assertEqual(homework.created.date().isoformat(), "2021-01-10")
        self.assertEqual(homework.deadline.days, 7)

    def test_homework_result(self):
        result = HomeworkResult.objects.get(id=1)
        self.assertEqual(result.homework.text, "Learn OOP")
        self.assertEqual(result.author.id, 1)
        self.assertEqual(result.solution, "Done")
        self.assertEqual(result.created.date().isoformat(), "2021-01-10")
