from dataclasses import dataclass

@dataclass
class Food:
    name: str
    category: str
    calories: int
    quantity: int = 0  # Default quantity is set to 0

    def calculate_total_calories(self) -> int:
        return self.calories * self.quantity if self.quantity > 0 else 0

def main():
    # Creating instances of the data class
    chicken = Food(name="Chicken", category="Meat", calories=335, quantity=2)
    asparagus = Food(name="Asparagus", category="Vegetable", calories=20, quantity=5)
    apples = Food(name="Apples", category="Fruit", calories=95, quantity=3)
    mashed_potatoes = Food(name="Mashed Potatoes", category="Side Dish", calories=150, quantity=1)

    # Accessing attributes and the additional function of the data class
    print(f"{chicken.name} - Total Calories: {chicken.calculate_total_calories()}")
    print(f"{asparagus.name} - Total Calories: {asparagus.calculate_total_calories()}")
    print(f"{apples.name} - Total Calories: {apples.calculate_total_calories()}")
    print(f"{mashed_potatoes.name} - Total Calories: {mashed_potatoes.calculate_total_calories()}")

if __name__ == "__main__":
    main()
