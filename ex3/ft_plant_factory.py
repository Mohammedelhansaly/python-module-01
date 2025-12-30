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

    def get_info(self) -> None:
        """Display the plant's information in a formatted way."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    """create multiple PLant Objects ,
    store them in a list , display their information
    and print the total number of plants created"""
    print("=== Plant Factory Output ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)
    plants = [p1, p2, p3, p4, p5]

    for plant in plants:
        plant.get_info()

    print(f"\nTotal plants created: {len(plants)}")


if (__name__ == "__main__"):
    main()
