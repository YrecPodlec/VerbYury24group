class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def create(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
class Triangle:
    def __init__(self, p1, p2, p3):
        self.point_1 = p1
        self.point_2 = p2
        self.point_3 = p3
    def perimeter(self):
        a = self.point_1.create(self.point_2)
        b = self.point_1.create(self.point_3)
        c = self.point_2.create(self.point_3)
        return int(a + b + c)
    def square(self):
        a = self.point_1.create(self.point_2)
        b = self.point_1.create(self.point_3)
        c = self.point_2.create(self.point_3)
        p = (a + b + c) / 2
        return int((p * (p - a) * (p - b) * (p - c)) ** 0.5)
treeangeles = [
    Triangle(Point(2, 4), Point(6, 8), Point(-2, 10)),
    Triangle(Point(12, 3), Point(7, 7), Point(0, -10)),
    Triangle(Point(-8, -4), Point(6, -6), Point(6, 10)),
]
i = 0
s = 0
print("Площадь: ")
for square_sq in treeangeles:
    i = i+1
    print(f"Треугольник {i}: ", square_sq.square())
print("Периметр: ")
for perim_p in treeangeles:
    s = s+1
    print(f"Треугольник {s}: ", perim_p.perimeter())