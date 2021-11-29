"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Raises if homework.is_active() returns False"""

    def __init__(self, message=None):
        self.message = message


class HomeworkError(Exception):
    """Raises if HomeworkResult didn't get Homework class as argument"""

    def __init__(self, message=None):
        self.message = message


class Homework:
    """Describes Homework instance.
    text: str
    deadline: datetime.timedelta
    created: date
    method is_active: checks deadline
    method is_valid: checks match by attributes
    """

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return self.deadline > datetime.datetime.now() - self.created

    @staticmethod
    def is_valid(other) -> bool:
        return hasattr(other, "text") and hasattr(other, "deadline")


class HomeworkResult:
    """Describes homework result.
    author: Student
    homework: Homework
    solution: str
    created: datetime
    """

    def __init__(self, author, homework, solution: str):
        if not isinstance(homework, Homework):
            raise HomeworkError("You gave a not Homework object")
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()

    @staticmethod
    def is_valid(other) -> bool:
        return hasattr(other, "solution") and hasattr(other, "homework")


class User:
    """Describes base class for Student and Teacher.
    first_name: name
    last_name: surname
    """

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(User):
    """Describes Student instance.
    first_name: name
    last_name: surname
    method do_homework: returns Homework if in deadline,
    raises DeadLineError if homework.is_active is False
    """

    def do_homework(self, homework, solution: str) -> HomeworkResult:
        """Returns an instance of the HomeworkResult class"""

        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError("You are late")


class Teacher(User):
    """Describes Teacher instance.
    first_name: name
    last_name: surname
    methods:
    create_homework: creates Homework instance
    check_homework: True if HomeworkResult.solution > 5 symbols
    reset_results: Pops result of homework. Clears all dict if arg is none
    """

    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """Creates Homework instance"""
        return Homework(text, deadline)

    @staticmethod
    def check_homework(result) -> bool:
        """Checks the homework result"""

        if len(result.solution) > 5:
            Teacher.homework_done[result.homework].add(result)
            return True
        return False

    @staticmethod
    def reset_results(homework=None) -> None:
        """Pops result of homework. Clears all dict if argument is none"""

        if homework:
            Teacher.homework_done.pop(homework, None)
        else:
            Teacher.homework_done.clear()


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
