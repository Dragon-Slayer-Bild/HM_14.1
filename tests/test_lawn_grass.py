import pytest


def test_lawn_grass_init(first_product_lawn_grass):
    assert first_product_lawn_grass.name == "Газонная трава"
    assert first_product_lawn_grass.description == "Элитная трава для газона"
    assert first_product_lawn_grass.price == 500.0
    assert first_product_lawn_grass.quantity == 20
    assert first_product_lawn_grass.country == "Россия"
    assert first_product_lawn_grass.germination_period == "7 дней"
    assert first_product_lawn_grass.color == "Зеленый"


def test_lawn_grass_sum(first_product_lawn_grass, second_product_lawn_grass):
    assert first_product_lawn_grass + second_product_lawn_grass == 16750.0


def test_smartphone_sum_error(first_product_lawn_grass, second_product_lawn_grass):
    with pytest.raises(TypeError):
        first_product_lawn_grass + 1
