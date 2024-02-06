from dataclasses import dataclass

@dataclass
class Food:
    name: str
    category: str
    calories: int

def main():
    # Creating instances of the data class
    chicken = Food(name="Chicken", category="Main Dish", calories=335)
    asparagus = Food(name="Asparagus", category="Vegetable", calories=20)
    apples = Food(name="Apples", category="Fruit", calories=95)
    mashed_potatoes = Food(name="Mashed Potatoes", category="Side Dish", calories=150)

    # Accessing attributes of the data class
    print(f"{chicken.name} is a {chicken.category} with {chicken.calories} calories.")
    print(f"{asparagus.name} is a {asparagus.category} with {asparagus.calories} calories.")
    print(f"{apples.name} are a {apples.category} with {apples.calories} calories.")
    print(f"{mashed_potatoes.name} are a {mashed_potatoes.category} with {mashed_potatoes.calories} calories.")

if __name__ == "__main__":
    main()
