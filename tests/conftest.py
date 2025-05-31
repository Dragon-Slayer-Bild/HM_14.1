import pytest
from src.product import Product
from src.category import Category

@pytest.fixture
def first_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def second_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_dict():
    product_dict = {
        "name": "HUAWEY",
        "description": "256GB," " Серый цвет, 200MP камера",
        "price": 25600,
        "quantity": 22,
    }
    return product_dict


@pytest.fixture
def first_category():
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy 1337 Mega Super Puper Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 9999", "512GB, Gray space", 210000.0, 8),
        ],
    )
    return category1
