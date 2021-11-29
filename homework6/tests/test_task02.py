import datetime

from pytest import raises

from homework6.task02 import *


def test_user_attributes():
    oop_teacher = Teacher("Daniil", "Shadrin")
    assert oop_teacher.last_name == "Shadrin"
    good_student = Student("Lev", "Sokolov")
    assert good_student.first_name == "Lev"


def test_teacher_create_homework():
    oop_teacher = Teacher("Daniil", "Shadrin")
    oop_hw = oop_teacher.create_homework("Learn OOP", 1)
    assert Homework.is_valid(oop_hw)
    assert oop_hw.text == "Learn OOP"
    assert oop_hw.deadline == datetime.timedelta(days=1)


def test_check_homework_result_positive():
    student = Student("Lev", "Sokolov")
    homework = Homework("Learn OOP", 2)
    result = HomeworkResult(student, homework, "I have done this hw")
    assert Teacher.check_homework(result)


def test_check_homework_result_negative():
    lazy_student = Student('Roman', 'Petrov')
    homework = Homework("Learn OOP", 2)
    result = HomeworkResult(lazy_student, homework, "OOP?")
    assert not Teacher.check_homework(result)


def test_homework_error():
    with raises(HomeworkError) as e:
        HomeworkResult('??', '??', '??')
    assert e.type is HomeworkError


def test_deadline_error():
    student = Student("Lev", "Sokolov")
    homework = Homework("task", 0)
    with raises(DeadlineError) as e:
        student.do_homework(homework, "solution")
    assert e.type is DeadlineError


def test_teacher_reset_results():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student('Roman', 'Petrov')
    homework_1 = Homework("Learn OOP", 1)
    result_1 = HomeworkResult(student, homework_1, "I have done this hw")
    teacher.check_homework(result_1)
    homework_2 = Homework("Read docs", 2)
    result_2 = HomeworkResult(student, homework_2, "I have done this hw too")
    teacher.check_homework(result_2)

    assert result_1 in teacher.homework_done[homework_1]
    teacher.reset_results(homework_1)
    assert result_1 not in teacher.homework_done[homework_1]
    assert result_2 in teacher.homework_done[homework_2]
    teacher.reset_results()
    assert len(teacher.homework_done) == 0
