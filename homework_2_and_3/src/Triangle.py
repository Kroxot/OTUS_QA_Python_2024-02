from homework_2_and_3.src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        if side_a + side_b < side_c or side_a + side_c < side_b or side_b + side_c < side_a:
            raise ValueError("Not Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        p = self.get_perimeter / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
