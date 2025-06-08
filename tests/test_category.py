import pytest


def test_category_class_create(first_category, first_product):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций для удобства жизни"
    )
    assert first_category.name == "Смартфоны"
    assert len(first_category.products) == 2
    assert first_category.category_count == 1
    assert first_category.product_count == 2

    assert first_category.products == [
        "Samsung Galaxy 1337 Mega Super Puper Ultra, 180000.0 руб. Остаток: 5 шт.\n",
        "Iphone 9999, 210000.0 руб. Остаток: 8 шт.\n",
    ]

    first_category.add_product(first_product)
    assert first_category.products == [
        "Samsung Galaxy 1337 Mega Super Puper Ultra, 180000.0 руб. Остаток: 5 шт.\n",
        "Iphone 9999, 210000.0 руб. Остаток: 8 шт.\n",
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n",
    ]

    assert len(first_category.products) == 3
    assert first_category.category_count == 1


def test_category_class_str(first_category, first_product):
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."


def test_category_class_add(first_product, second_product):
    assert str(first_product + second_product) == "2580000.0"


def test_category_class_setter_error(first_category):
    with pytest.raises(TypeError):
        new_product = 1
        first_category.add_product(new_product)


def test_middle_price(first_category, category_with_zero_product):
    assert first_category.middle_price() == 195000
    assert category_with_zero_product.middle_price() == 0
