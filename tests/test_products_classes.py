from src.products_classes import Product


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
