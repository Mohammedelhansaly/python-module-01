class Plant:
    """represent a plant in garden
        atributtes:
        name:str => name of the plant,
        height:int => height of the plant in cm
        age:int => age of the plant in days
    """
    def __init__(self, name:str, height:int, age:int) -> None:
        """initialize a new plant instance"""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm_per_day:int) -> None:
        """increase the plant height"""
        self.height += cm_per_day

    def age_in_day(self, days:int) -> None:
        """increase the plant age"""
        self.age += days

    def get_info(self) -> None:
        """display the plant infos"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def grow_this_week(plants:list[Plant]) -> None:
    
    """Simulate one week of growth for multiple plants"""
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()

    for plant in plants:
        plant.age_in_day(6)
        plant.grow(6)
    print("=== Day 7 ===")
    for plant in plants:
        plant.get_info()
    print("Growth this week: +6cm")


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    plants = [p1]
    grow_this_week(plants)
