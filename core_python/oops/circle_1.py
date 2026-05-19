class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display_circumference(self):
        circumference = 2 * 3.14 * self.radius
        print(f"The circumference of the circle is: {circumference} units.")

    def display_area(self):
        area = 3.14 * self.radius ** 2
        print(f"The area of the circle is: {area} square units.")

new_circle = Circle(5)
new_circle.display_circumference()
new_circle.display_area()