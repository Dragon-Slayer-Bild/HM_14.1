import pytest

from src.product import Product


def test_product_class_create(first_product, second_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_product_class_new_product_add(product_dict):
    product = Product.new_product(product_dict)

    assert product.name == "HUAWEY"
    assert product.price == 25600


def test_product_class_new_price_update(product_dict):
    product = Product.new_product(product_dict)

    product.price = 1337
    assert product.price == 1337

    product.price = -99
    assert product.price == 1337

    product.price = 0
    assert product.price == 1337


def test_product_class_str(first_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Iphone 15", "512GB, Gray space", 210000.0, 0)


def test_product_add_without_quantity():
    with pytest.raises(TypeError):
        Product("Iphone 15", "512GB, Gray space", 210000.0)
