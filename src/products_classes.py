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

        name = product_dict.get("name")
        description = product_dict.get("description")
        price = product_dict.get("price")
        quantity = product_dict.get("quantity")

        return cls(name, description, price, quantity)

    # #Читаемый вывод объекта
    # def __repr__(self):
    #     return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    """Класс для предсталения категории"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        self.product_count += 1

    @property
    def products(self):
        products_str = []
        for product in self.__products:
            product_str = f"{product.name}, {product.price} руб. Остаток: {self.product_count} шт.\n"
            products_str.append(product_str)
        return products_str


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(category1.products)
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
#     print(category1.products)
#     print(category1.product_count)
#
#     new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
#     print(new_product.name)
#     print(new_product.description)
#     print(new_product.price)
#     print(new_product.quantity)
#
#     new_product.price = 800
#     print(new_product.price)
#
#     new_product.price = -100
#     print(new_product.price)
#     new_product.price = 0
#     print(new_product.price)
