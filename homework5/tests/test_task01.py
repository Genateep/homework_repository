import datetime

from homework5.task01 import Homework, Student, Teacher


def test_homework():
    new_homework = Homework("Make hw5", 7)

    assert new_homework.text == "Make hw5"
    assert new_homework.deadline == datetime.timedelta(days=7)
    assert new_homework.is_active()


def test_teacher():
    teacher = Teacher("Daniil", "Shadrin")
    create_homework_too = teacher.create_homework
    new_homework = create_homework_too("Make hw5", 7)

    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"
    assert new_homework.is_active()


def test_student(capsys):
    student = Student("Roman", "Petrov")
    new_homework = Homework("Make Hw5", 7)
    expired_homework = Homework("Make hw4", 0)

    assert student.first_name == "Roman"
    assert student.do_homework(new_homework) is new_homework
    assert not student.do_homework(expired_homework)

    captured = capsys.readouterr()
    assert "Too late, bro" in captured.out
