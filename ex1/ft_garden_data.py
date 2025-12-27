class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
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
