from homework_2_and_3.src.Square import Square
import pytest


@pytest.mark.parametrize(("side_a", "area"),
                         [(3, 9),
                          (3.5, 12.25),
                          ],
                         ids=["int", "float"])
def test_square_area_positive(side_a, area):
    r = Square(side_a)
    assert r.get_area == area, f"Area should be {side_a * side_a}"


@pytest.mark.parametrize(("side_a", "perimeter"),
                         [(5, 20),
                          (5.5, 22)],
                         ids=["int", "float"])
def test_square_perimeter_positive(side_a, perimeter):
    r = Square(side_a)
    assert r.get_perimeter == perimeter, f"Perimeter should be {side_a * 4}"


@pytest.mark.parametrize("side_a",
                         [0, -1],
                         ids=["zero value", "negative value"])
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)
