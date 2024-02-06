class Cylinder:
    def __init__(self, radius, height):
        self._radius = radius
        self._height = height

    def get_radius(self):
        return self._radius

    def get_height(self):
        return self._height

    def calculate_volume(self):
        return 3.14 * self._radius ** 2 * self._height

    def calculate_surface_area(self):
        return 2 * 3.14 * self._radius * (self._radius + self._height)

def main():
    # Creating an instance of the Cylinder class
    cylinder = Cylinder(radius=2, height=5)

    # Accessing methods
    print(f"Radius: {cylinder.get_radius()}")
    print(f"Height: {cylinder.get_height()}")
    print(f"Volume: {cylinder.calculate_volume()}")
    print(f"Surface Area: {cylinder.calculate_surface_area()}")

    # Attempting to set values directly (this won't work due to the lack of a setter method)
    try:
        cylinder.radius = 3  # This will raise an AttributeError
    except AttributeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
