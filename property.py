class Circle:
    def __init__(self, radius):
        self._radius = radius  # Prefixing with '_' to indicate it as a protected attribute

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

def main():
    # Creating an instance of the Circle class
    circle = Circle(radius=3)

    # Accessing properties (using the methods as if they were attributes)
    print(f"Radius: {circle.radius}")
    print(f"Diameter: {circle.diameter}")
    print(f"Circumference: {circle.circumference}")
    print(f"Area: {circle.area}")

    # Attempting to set values directly (this won't work due to the property decorator)
    try:
        circle.radius = 5  # This will raise an AttributeError
    except AttributeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
