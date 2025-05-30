class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawing a point at ({self.x}, {self.y})")


point = Point(10, 20)
point.draw()

