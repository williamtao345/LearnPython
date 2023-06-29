class Shape:
    def draw(self):
        print("draw")


class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")


point1 = Point(1, 2)
point1.draw()
point1.move()
point1.z = 0
