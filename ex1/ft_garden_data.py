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
        """display the infos of the plant"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """display plants information"""
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 42)
    p3 = Plant("Cactus", 15, 120)
    garden = [p1, p2, p3]
    for plant in garden:
        plant.get_info()


if __name__ == "__main__":
    main()
