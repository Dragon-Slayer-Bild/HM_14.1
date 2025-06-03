class Product:
    """Класс для предсталения продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер, который возвращает цену продукта"""

        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price == self.__price or new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_dict: dict):
        """класс-метод для создания нового продукта из словаря"""

        return cls(**product_dict)

    # Читаемый вывод объекта
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            summ = self.price * self.quantity + other.price * other.quantity
            return summ
        raise TypeError
