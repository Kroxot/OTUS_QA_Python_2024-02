from homework_2_and_3.src.Rectangle import Rectangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [(3, 5, 15),
                          (3.5, 5.5, 19.25),
                          ],
                         ids=["int", "float"])
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area, f"Area should be {side_a * side_b}"


@pytest.mark.parametrize(("side_a", "side_b", "perimeter"),
                         [(3, 5, 16),
                          (3.5, 5.5, 18)],
                         ids=["int", "float"])
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter == perimeter, f"Perimeter should be {(side_a + side_b) * 2}"


@pytest.mark.parametrize(("side_a", "side_b"),
                         [(0, 5),
                          (-1, 5.5)],
                         ids=["zero value", "negative value"])
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
