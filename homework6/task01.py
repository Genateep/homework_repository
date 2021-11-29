"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Adds methods to the class that return count of created instances
    and reset the counter
    """

    def __new__(cls, *args, **kwargs):
        cls.counter += 1
        return super(type(cls), cls).__new__(cls)

    def get_created_instances(cls) -> int:
        return cls.counter

    def reset_instances_counter(cls) -> int:
        c = cls.counter
        cls.counter = 0
        return c

    setattr(cls, "__new__", staticmethod(__new__))
    setattr(cls, "counter", 0)
    setattr(cls, "get_created_instances", classmethod(get_created_instances))
    setattr(cls, "reset_instances_counter", classmethod(reset_instances_counter))

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
