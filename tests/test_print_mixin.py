from src.product import Product
from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone

def test_print_mixin_product(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    massage = capsys.readouterr()
    assert massage.out.strip() == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"


def test_print_mixin_lawn_grass(capsys):
    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    massage = capsys.readouterr()
    assert massage.out.strip() == "LawnGrass('Газонная трава 2', 'Выносливая трава', 450.0, 15)"


def test_print_mixin_lawn_smartphone(capsys):
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    massage = capsys.readouterr()
    assert massage.out.strip() == "Smartphone('Iphone 15', '512GB, Gray space', 210000.0, 8)"