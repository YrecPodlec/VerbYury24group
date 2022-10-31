class Point:
    def __init__(self, x, y):
        self._y = y
        self._x = x

    @property
    def xy(self):
        return self._x, self._y

class Figures:
    def __init__(self, points):
        self._area = None
        self._points = points
        self._update_area()
        pass

    def _update_area(self):
        print("Area update")
        pass

    @property
    def area(self):
        return self._area

    def __le__(self, second):
        return self.area <= second.area

    def __ge__(self, second):
        return self.area >= second.area

    def __eq__(self, second):
        return self.area > second.area

    def __ne__(self, second):
        return self.area < second.area

    def __gt__(self, second):
        return self.area == second.area

class Triangle(Figures):
    # def __init__(self, points):
    #     super().__init__(self, points)

    def _update_area(self):
        print("Area update")
        return super()._update_area()

class Trueangle(Figures):
    def _update_area(self):
        print("Area update")
        return super()._update_area()

a = Triangle(((1,2),(2,3),(2,2)))
b = Trueangle(((1,2),(2,3),(2,2),(2,1)))