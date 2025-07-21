# Flyweight Interface
class Shape:
    def draw(self, x, y):
        pass

# Concrete Flyweight
class Circle(Shape):
    def __init__(self, color):
        self.color = color

    def draw(self, x, y):
        print(f"Drawing a {self.color} circle at ({x}, {y})")

# Flyweight Factory
class ShapeFactory:
    def __init__(self):
        self.circle = {}

    def get_circle(self, color):
        if color not in self.circle:
            self.circle[color] = Circle(color)
        return self.circle[color]

# Client Code
class DrawingApp:
    def __init__(self, shape_factory):
        self.shape_factory = shape_factory
        self.shapes = []

    def add_circle(self, color, x, y):
        circle = self.shape_factory.get_circle(color)
        self.shapes.append((circle, x, y))

    def draw_shapes(self):
        for shape, x, y in self.shapes:
            shape.draw(x, y)

# Application
if __name__ == "__main__":
    shape_factory = ShapeFactory()

    drawing_app = DrawingApp(shape_factory)
    drawing_app.add_circle("Red", 10, 10)
    drawing_app.add_circle("Blue", 20, 20)
    drawing_app.add_circle("Red", 30, 30)

    drawing_app.draw_shapes()
