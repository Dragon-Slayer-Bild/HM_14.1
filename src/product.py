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
        if isinstance(other, Product):
            summ = self.price * self.quantity + other.price * other.quantity
            return summ
        else:
            raise ValueError("Невозможно сложить объекты разных типов")


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

