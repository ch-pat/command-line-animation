import math

class Triangle:
    def __init__(self, a: 'Point', b: 'Point', c: 'Point'):
        self.a = a
        self.b = b
        self.c = c

    def get_points(self):
        ab_side = Segment(self.a, self.b).get_points_in_segment()
        ac_side = Segment(self.a, self.c).get_points_in_segment()
        bc_side = Segment(self.c, self.b).get_points_in_segment()
        return ab_side | ac_side | bc_side


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point X: {self.x: .2f}, Y: {self.y: .2f}"
    
    def __eq__(self, point: 'Point'):
        return self.x == point.x and self.y == point.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, point: 'Point'):
        return self.x < point.x

    def apply_rotation(self, angle: float, pivot: 'Point'):
        self.x = self.x - pivot.x
        self.y = self.y - pivot.y

        new_x = self.x * math.cos(angle) - self.y * math.sin(angle)
        new_y = self.x * math.sin(angle) + self.y * math.cos(angle)

        self.x = new_x + pivot.x
        self.y = new_y + pivot.y


class Line:
    def __init__(self, m: float, q: float):
        self.m = m
        self.q = q

    def get_y(self, x) -> int:
        return self.m * x + self.q


    def get_x(self, y) -> int:
        return (y - self.q) / self.m


    def __str__(self):
        return f"y = {self.m}x + {self.q}"

    def __repr__(self):
        return self.__str__()


class VerticalLine(Line):
    def __init__(self, x: float):
        self.x = x

    def get_y(self, x) -> int:
        return None

    def get_x(self, y) -> int:
        return self.x

    def __str__(self):
        return f"x = {self.x}"
    
    def __repr__(self):
        return self.__str__()


class HorizontalLine(Line):
    def __init__(self, y: float):
        self.y = y

    def get_y(self, x) -> int:
        return self.y

    def get_x(self, y) -> int:
        return None

    def __str__(self):
        return f"y = {self.y}"
    
    def __repr__(self):
        return self.__str__()



class Segment:
    def __init__(self, a: Point, b: Point):
        self.a: Point = a
        self.b: Point = b

    def get_line(self) -> Line:
        """Returns the Line on which the segment lives"""
        if round(self.a.x - self.b.x, 2) == 0:
            return VerticalLine(self.a.x)
        m = round((self.a.y - self.b.y) / (self.a.x - self.b.x), 2)
        if m == 0:
            return HorizontalLine(self.a.y)
        q = round(self.a.y - m * self.a.x, 2)
        return Line(m, q)
    
    def get_x_coordinates(self):
        """Returns the list of all integer x values in which the segment lives"""
        if self.a.x <= self.b.x:
            n = self.a.x
            m = self.b.x
        else:
            m = self.a.x
            n = self.b.x
        n = int(n) if n == int(n) else int(n + 1)
        m = int(m)
        return list(range(n, m + 1))

    def get_y_coordinates(self):
        """Returns the list of all integer y values in which the segment lives"""
        if self.a.y <= self.b.y:
            n = self.a.y
            m = self.b.y
        else:
            m = self.a.y
            n = self.b.y
        n = int(n) if n == int(n) else int(n + 1)
        m = int(m)
        return list(range(n, m + 1))

    def get_points_in_segment(self) -> set:
        x_coordinates = self.get_x_coordinates()
        y_coordinates = self.get_y_coordinates()
        line = self.get_line()
        result = set()
        for x in x_coordinates:
            y = line.get_y(x)
            if y is not None:
                y = round(y, 2)
                result.add(Point(x, y))
        for y in y_coordinates:
            x = line.get_x(y)
            if x is not None:
                x = round(x, 2)
                result.add(Point(x, y))
        return result




if __name__ == "__main__":
    a = Point(1,5)
    b = Point(4,7)
    c = Point(12, 1)

    tr = Triangle(a, b, c)
    print(tr.get_points())