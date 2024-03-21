class Car:
    def __init__(self, brand:str, price:int):
        """
        Инициализируем атрибуты для базового класса Car
        Атрибут brand является protected чтобы пользователь не мог бы его изменить
        Также есть атрибут price, который означает цену автомобиля,
        данный атрибут может изменяться пользователем
        """
        self._brand = brand
        if not isinstance(price, int):
            raise TypeError('Цена автомобиля должна быть типа int')
        if price < 0:
            raise ValueError('Цена автомобиля должна быть положительной')
        self.price = price

    @property
    def brand(self) -> str:
        """
        Реализовываем getter для атрибута brand
        Так как нам необходимо чтобы данный атрибут не мог изменить пользователь,
        то setter мы реализовывать не будет
        """
        return self._brand

    def __str__(self):
        """
        Магический метод __str__ выводит понятные для пользователя характеристики об объекте
        """
        return f"Машина марки {self.brand}, стоимостью {self.price}$"

    def __repr__(self):
        """
        Магический метод __repr__ выводит более детальное описание конкретного объекта с указанием
        значений его атрибутов
        """
        return f"{self.__class__.__name__}(brand ={self._brand!r}, price = {self.price!r})"

    def price_up(self, increase:float) -> None:
        """
        Данный метод отвечает за увеличение цены автомобиля
        Он будет наследоваться и не будет перегружаться для дочернего класса
        так как его реализация подходит для любого автомобиля
        """
        if increase < 0 :
            raise ValueError('Можно увеличить цену только на положительное значение')
        self.price += increase

    def price_low(self, decrease: float) -> None:
        """
        Такой же метод, отвечающий за уменьшение цены автомобиля
        Предполагается, что пользователь лишь вводит стоимость, на которую хочет увеличить или уменьшить цену автомобиля
        """
        if decrease < 0:
            raise ValueError('Можно уменьшить цену только на положительное значение')
        self.price -= decrease


class TruckCar(Car):
    def __init__(self, brand:str, price:float, max_weight: int):
        """
        Мы перегружаем метод __init__ для того чтобы ввести новый атрибут
        max_weight - максимальная грузоподъемность машины
        """
        super().__init__(brand, price)
        self._max_weight = max_weight

    @property
    def max_weight(self) -> int:
        """
        Устанавливаем getter для атрибута max_weight
        """
        return self._max_weight

    @max_weight.setter
    def max_weight(self, max_weight: int) -> None:
        """
        Устанавливаем setter для атрибута setter
        Также проверяем чтобы введенное пользователем значение соответствовало бы нашим требованиям
        """
        if not isinstance(max_weight, int):
            raise TypeError('Максимальная грузоподъемность должна быть типа int')
        if max_weight<0:
            raise ValueError('Максимальна грузоподъемность должна быть положительным числом')
        self._max_weight = max_weight

    def __repr__(self):
        """
        Перегружаем волшебный метод __repr__ так как нам
        необходимо также выводить информацию об
        уникальном для дочернего класса атрибуте
        """
        return super().__repr__() + f" max_weight = {self.max_weight}"
