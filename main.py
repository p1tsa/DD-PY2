import doctest
from typing import Union
# TODO Написать 3 класса с документацией и аннотацией типов


class Gun:
    def __init__(self, damage: int, magazine: int, bullet_count: int):
        """
        Создание объекта "Оружие"

        :param damage: урон оружия
        :param magazine: магазин патронов (вместимость магазина)
        :param bullet_count: текущее кол-во патронов в оружии

        Пример:
        >>> ak = Gun(85, 30, 15)
        """
        if not (isinstance(damage, int) and isinstance(bullet_count, int) and isinstance(magazine, int)):
            raise TypeError("Атрибуты оружия должны быть типа int")
        if (damage < 0) or (bullet_count < 0) or (magazine < 0):
            raise ValueError("Атрибуты оружия не могут быть отрицательными")
        if bullet_count > magazine:
            raise ValueError("Патронов не может быть больше вместимости магазина")

        self.damage = damage
        self.magazine = magazine
        self.bullet_count = bullet_count

    def reload(self) -> None:
        """
        Функция, которая перезаряжает оружие

        :return: None, функция лишь меняет атрибуты объекта

        Пример:
        >>> ak = Gun(85, 30, 15)
        >>> ak.reload()
        """
        self.bullet_count = self.magazine

    def remove_bullets(self) -> None:
        """
        Функция, которая вынимает все патроны из оружия

        :return: None, функция лишь меняет атрибуты объекта

        Пример:
        >>> ak = Gun(85, 30, 15)
        >>> ak.remove_bullets()
        """
        self.bullet_count = 0

    def increase_damage(self, value: int) -> None:
        """
        Функция, которая увеличивает урон оружия

        :return: None, функция лишь меняет атрибуты объекта
        :param value: на сколько необходимо увеличить урон оружия
        :raise ValueError: невозможно увеличить урон оружия на отрицательную величину

        Пример:
        >>> ak = Gun(85, 30, 15)
        >>> ak.increase_damage(15)
        >>> ak.damage
        100
        """
        if not isinstance(value, int):
            raise TypeError("Кол-во увеличиваемого урона может быть только типа int")
        if value < 0 :
            raise ValueError("Невозможно увеличить урон оружия на отрицательную величину")
        self.damage+=value


class Actor:
    def __init__(self, name: str, age: int, oscar: bool):
        """
        Создание объекта "Актер"

        :param name: Имя актера
        :param age: Возраст актера
        :param oscar: Означает, выйграл ли данный актер оскар или нет

        Пример:
        >>> gosling = Actor("Gosling", 43, False)
        """
        if not isinstance(name, str):
            raise TypeError("Атрибут name должен быть типа str")
        if not isinstance(age, int):
            raise TypeError("Атрибут age должен быть типа int")
        if not isinstance(oscar, bool):
            raise TypeError("Атрибут oscar должен быть типа bool")

        if age < 0:
            raise ValueError("Возраст актера не может быть отрицательным")

        self.name = name
        self.age = age
        self.oscar = oscar

    def getting_older(self) -> None:
        """
        Функция, увеличивающая возраст актера на 1 год

        :return: None, функция лишь меняет атрибуты объекта

        Пример
        >>> gosling = Actor("Gosling", 43, False)
        >>> gosling.getting_older()
        """
        self.age+=1

    def give_oscar(self) -> None:
        """
        Функция, присваивающая актеру оскар (атрибут oscar становится True)

        :return: None, функция лишь меняет атрибуты объекта

        Пример:
        >>> gosling = Actor("Gosling", 43, False)
        >>> gosling.give_oscar()
        """
        self.oscar = True


class Student:
    def __init__(self, name: str, is_studying: bool, course: int):
        """
        Создание объекта "Студент"

        :param name: Имя студента
        :param is_studying: Указатель, учится ли сейчас студент в университете
        :param course: Показывает либо текущий курс студента, либо тот курс на котором от отчислился

        Пример:
        >>> student = Student("Oleg", True, 3)
        """
        if not isinstance(name, str):
            raise TypeError("Атрибут name должен быть типом str")
        if not isinstance(is_studying, bool):
            raise TypeError("Атрибут is_studying должен быть типом bool")
        if not isinstance(course, int):
            raise TypeError("Атрибут course должен быть типом int")

        if course < 0 or course > 5:
            raise ValueError("Введите корректный курс")

        self.name = name
        self.is_studying = is_studying
        self.course = course

    def transfer(self, course: int) -> None:
        """
        Функция, переводящая студента на другой курс

        :return: None, функция лишь меняет атрибуты объекта
        :course: Курс, на который предпологается перевести студента

        Пример
        >>> student = Student("Oleg", True, 3)
        >>> student.transfer(2)
        >>> student.course
        2
        """
        if course < 0 or course > 5:
            raise ValueError("Введите корректный курс")

        self.course = course

    def expel(self) -> None:
        """
        Функция, отчисляющая студента(

        :return: None, функция лишь меняет атрибуты объекта

        Пример:
        >>> student = Student("Oleg", True, 3)
        >>> student.expel()
        >>> student.is_studying
        False
        """
        self.is_studying = False


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
