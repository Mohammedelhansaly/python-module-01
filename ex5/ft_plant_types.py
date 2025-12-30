class Plant:
    """represent a plant in garden
        atributtes:
        name:str => name of the plant,
        height:int => height of the plant in cm
        age:int => age of the plant in days
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialize a new plant instance"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm,"
              f" {self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.trunk_diameter * 1.5:.0f}"
              f"square meters of shade")

    def info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm,"
              f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def describe_nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}.")

    def info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm,"
              f"{self.age} days, {self.harvest_season} harvest")


def main() -> None:
    print("=== Garden Plant Types ===\n")
    f1 = Flower("Rose", 25, 30, "red")
    f2 = Flower("Tulip", 15, 20, "yellow")

    t1 = Tree("Oak", 500, 1825, 50)
    t2 = Tree("Maple", 400, 1500, 40)

    v1 = Vegetable("tomato", 58, 25, "summer", "C")
    v2 = Vegetable("potato", 42, 50, "winter", "E")

    flowers = [f1, f2]
    trees = [t1, t2]
    vegetables = [v1, v2]

    for flower in flowers:
        flower.info()
        flower.bloom()
        print("\n")

    for tree in trees:
        tree.info()
        tree.produce_shade()
        print("\n")

    for vegetable in vegetables:
        vegetable.info()
        vegetable.describe_nutrition()
        print("\n")


if __name__ == "__main__":
    main()
