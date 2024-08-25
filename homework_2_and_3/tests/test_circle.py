from homework_2_and_3.src.Circle import Circle
import pytest


@pytest.mark.parametrize(("radius", "area"),
                         [(3, 28),
                          (3.5, 38),
                          ],
                         ids=["int", "float"])
def test_circle_area_positive(radius, area):
    r = Circle(radius)
    assert round(r.get_area) == area, f"Area should be {area}"


@pytest.mark.parametrize(("radius", "perimeter"),
                         [(5, 31),
                          (5.5, 35)],
                         ids=["int", "float"])
def test_circle_perimeter_positive(radius, perimeter):
    r = Circle(radius)
    assert round(r.get_perimeter) == perimeter, f"Perimeter should be {perimeter}"


@pytest.mark.parametrize("radius",
                         [0, -1],
                         ids=["zero value", "negative value"])
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)
