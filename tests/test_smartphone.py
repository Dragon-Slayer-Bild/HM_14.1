import pytest


def test_smartphone_init(first_product_smartphone):
    assert first_product_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_product_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_product_smartphone.price == 180000.0
    assert first_product_smartphone.quantity == 5
    assert first_product_smartphone.color == "Серый"
    assert first_product_smartphone.memory == 256
    assert first_product_smartphone.efficiency == 95.5
    assert first_product_smartphone.model == "S23 Ultra"


def test_smartphone_sum(first_product_smartphone, second_product_smartphone):
    assert first_product_smartphone + second_product_smartphone == 2580000.0


def test_smartphone__sum_error(first_product_smartphone, second_product_smartphone):
    with pytest.raises(TypeError):
        first_product_smartphone + 1
