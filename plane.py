from shapes import Point, Triangle
import random, os, time, math

class BinaryPlane:
    def __init__(self, size: int):
        self.size: int = size
        self.active_points: {Point} = set([])

    def add_shape(self, shape: 'Shape'):
        pass

    def add_point(self, point: Point):
        self.active_points = self.active_points | {point}

    def add_points(self, points: set[Point]):
        self.active_points = self.active_points.union(points)
        
    def __str__(self):
        matrix_representation = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for point in self.active_points:
            x = round(point.x)
            y = round(point.y)
            if 0 <= x < self.size and 0 <= y < self.size:
                matrix_representation[x][y] = 1
        result = ""
        for i in range(self.size):
            for j in range(self.size):
                result += " @" if matrix_representation[j][i] else " ."
            result += "\n"
        return result

    def pretty_print_points(self):
        points = sorted(sorted(list([Point(round(p.x), round(p.y)) for p in self.active_points]), key= lambda x: x.y))
        unique_x = set([point.x for point in points])
        result = ""
        for x in unique_x:
            y_list = [round(point.y) for point in points if point.x == x]
            result += f"X: {round(x)},\tY: {y_list}\n"
        print(result)


if __name__ == "__main__":
    size = 36
    refresh = 1/60
    duration = 5
    frames = int(duration * (1 / refresh))
    n_rotations = 3
    plane = BinaryPlane(size)
    a = Point(17, 3)
    b = Point(8, 29)
    c = Point(28, 29)
    center = Point(17, 17)
    triangle = Triangle(a, b, c)
    plane.add_points(triangle.get_points())
    plane.pretty_print_points()
    steps = [3.14 * 2 * n_rotations / frames for i in range(1, frames + 1)]
    for n in steps:
        plane = BinaryPlane(size)
        a.apply_rotation(n, center)
        b.apply_rotation(n, center)
        c.apply_rotation(n, center)
        triangle = Triangle(a, b, c)
        plane.add_points(triangle.get_points())
        print(plane)
        time.sleep(refresh)
