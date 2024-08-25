from homework_2_and_3.src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(3, 4, 5, 6),
                          (3.5, 4.4, 5.5, 8),
                          ],
                         ids=["int", "float"])
def test_triangle_area_positive(side_a, side_b, side_c, area):
    r = Triangle(side_a, side_b, side_c)
    assert round(r.get_area) == area, f"Area should be {area}"


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "perimeter"),
                         [(3, 4, 5, 12),
                          (3.5, 4.4, 5.5, 13.4)],
                         ids=["int", "float"])
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.get_perimeter == perimeter, f"Perimeter should be {side_a + side_b + side_c}"


@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                         [(0, 5, 2),
                          (-1, 5.5, 2),
                          (1, 2, 4)],
                         ids=["zero value", "negative value", "not triangle"])
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
