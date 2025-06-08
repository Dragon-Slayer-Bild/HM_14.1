import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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

@pytest.fixture
def category_with_zero_product():
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    return category1

@pytest.fixture
def first_product_smartphone():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    return smartphone1


@pytest.fixture
def second_product_smartphone():
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    return smartphone2


@pytest.fixture
def first_product_lawn_grass():
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    return grass1


@pytest.fixture
def second_product_lawn_grass():
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    return grass2
