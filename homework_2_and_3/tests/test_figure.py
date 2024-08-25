import pytest
from homework_2_and_3.src.Triangle import Triangle
from homework_2_and_3.src.Rectangle import Rectangle


def test_figure_add_area_positive():
    t = Triangle(3, 4, 5)
    r = Rectangle(3, 4)
    assert t.add_area(r) == pytest.approx(6 + 12), f"The sum of the areas should be {pytest.approx(6 + 12)}"


def test_figure_add_area_negative():
    t = Triangle(3, 4, 5)
    with pytest.raises(ValueError):
        t.add_area("Not a figure")
