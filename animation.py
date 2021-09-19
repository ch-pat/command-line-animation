from plane import BinaryPlane
from shapes import Triangle, Point
import time, random

class CommandLineAnimation:
    def __init__(self, 
                 plane: BinaryPlane,
                 refresh_rate: int=30,
                 animation_duration: int=5
        ):
        self.plane: BinaryPlane = plane
        self.refresh_rate: int = refresh_rate
        self.animation_duration: int = animation_duration
        self.n_frames = int(self.animation_duration * self.refresh_rate) 

    def triangle_rotation(self, triangle: Triangle, n_rotations: int=1, rotation_center: Point = None):
        if not rotation_center:
            rotation_center = Point(self.plane.size // 2, self.plane.size // 2)
        a, b, c = triangle.a, triangle.b, triangle.c
        steps = [3.14 * 2 * n_rotations / self.n_frames for i in range(1, self.n_frames + 1)]
        self.plane.add_points(triangle.get_points())
        self.plane.project_points()
        print(self.plane)
        for n in steps:
            self.plane.clean_plane()
            a.apply_rotation(n, rotation_center), b.apply_rotation(n, rotation_center), c.apply_rotation(n, rotation_center)
            triangle = Triangle(a, b, c)
            self.plane.add_points(triangle.get_points())
            self.plane.project_points()
            print(self.plane)
            time.sleep(1 / self.refresh_rate)
            


if __name__ == "__main__":
    start_time = time.time()
    plane = BinaryPlane(36)
    a = Point(random.randint(1, 35), random.randint(1, 35))
    b = Point(random.randint(1, 35), random.randint(1, 35))
    c = Point(random.randint(1, 35), random.randint(1, 35))
    center = Point(17, 17)
    triangle = Triangle(a, b, c)
    animation = CommandLineAnimation(plane)
    animation.triangle_rotation(triangle, 3, center)
    print(f"Time {time.time() - start_time}")