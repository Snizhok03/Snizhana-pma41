class Shape:
    def draw(self, x, y):
        pass  # Метод для малювання фігури на полотні.


class Circle(Shape):
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def draw(self, x, y):
        print(f"Drawing a {self.color} circle with radius {self.radius} at ({x}, {y})")


class Square(Shape):
    def __init__(self, color, side_length):
        self.color = color
        self.side_length = side_length

    def draw(self, x, y):
        print(f"Drawing a {self.color} square with side length {self.side_length} at ({x}, {y})")


class Triangle(Shape):
    def __init__(self, color, base, height):
        self.color = color
        self.base = base
        self.height = height

    def draw(self, x, y):
        print(f"Drawing a {self.color} triangle with base {self.base} and height {self.height} at ({x}, {y})")


class ShapeFactory:
    shapes = {}

    @staticmethod
    def get_shape(shape_type, color, **kwargs):
        key = (shape_type, color)
        if key not in ShapeFactory.shapes:
            if shape_type == "circle":
                ShapeFactory.shapes[key] = Circle(color, kwargs['radius'])
            elif shape_type == "square":
                ShapeFactory.shapes[key] = Square(color, kwargs['side_length'])
            elif shape_type == "triangle":
                ShapeFactory.shapes[key] = Triangle(color, kwargs['base'], kwargs['height'])
            else:
                raise ValueError("Unsupported shape type")
        return ShapeFactory.shapes[key]


class Canvas:
    def __init__(self):
        self.shapes = []

    def draw_shape(self, shape_type, color, x, y, **kwargs):
        shape = ShapeFactory.get_shape(shape_type, color, **kwargs)
        self.shapes.append((shape, x, y))

    def render(self):
        for shape, x, y in self.shapes:
            shape.draw(x, y)


if __name__ == "__main__":
    canvas = Canvas()
    canvas.draw_shape("circle", "blue", 10, 10, radius=5)
    canvas.draw_shape("square", "red", 20, 20, side_length=8)
    canvas.draw_shape("triangle", "green", 30, 30, base=6, height=4)

    canvas.render()
