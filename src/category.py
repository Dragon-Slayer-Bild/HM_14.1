from src.product import Product


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

    def __str__(self):
        products_quantity = 0

        for product in self.__products:
            products_quantity += product.quantity
        return f"{self.name}, количество продуктов: {products_quantity} шт."

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        products_str = []
        for product in self.__products:
            product_str = f"{str(product)}\n"
            products_str.append(product_str)
        return products_str

    def middle_price(self):
        try:
            middle_product_price = sum([product.price for product in self.__products]) / len(self.__products)
            return round(middle_product_price, 2)
        except ZeroDivisionError:
            return 0
