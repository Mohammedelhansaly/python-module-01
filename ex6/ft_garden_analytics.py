def validate_height(height) -> bool:
    """return True if height is valid"""
    return height >= 0


def calculate_score(height) -> int:
    """return score based on height"""
    return height * 2


class Plant:
    """represents a plant in the garden"""
    def __init__(self, name, height) -> None:
        """Initialize a Plant with a name and height."""
        self.name = name
        self.height = height

    def display_info(self) -> None:
        """display plant information"""
        print(f"{self.name} : {self.height} cm", end='')


class FloweringPlant(Plant):
    """represents a flowering plant in the garden
        and inherits name and height from Plant"""
    def __init__(self, name, height, color) -> None:
        """initialize a FloweringPlant with name, height, and color"""
        super().__init__(name, height)
        self.color = color

    def display_info(self) -> None:
        """display flowering plant information including color"""
        super().display_info()
        print(f", {self.color} flowers (blooming)", end='')


class PrizeFlower(FloweringPlant):
    """"represents a prize flower in the garden
        and inherits name, height, and color from FloweringPlant"""
    def __init__(self, name, height, color, prize) -> None:
        """initialize a PrizeFlower with name, height,
            color, and prize points"""
        super().__init__(name, height, color)
        self.prize = prize

    def display_info(self) -> None:
        """display prize flower information including prize points"""
        super().display_info()
        print(f", Prize points: {self.prize}", end='')


class Garden():
    """represents a garden containing plants"""
    def __init__(self, name) -> None:
        """initialize a Garden with a name and empty plant list"""
        self.name = name
        self.plants = []

    def add_plant(self, plant) -> None:
        """add a plant to the garden"""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name} garden")

    def grow_plants(self) -> None:
        """grow all plants in the garden by 1cm"""
        for plant in self.plants:
            plant.height += 1
            print(f"{plant.name} grew 1cm")

    def display_garden(self) -> None:
        """display garden report with plant details and statistics"""
        print(f"\n=== {self.name} Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("- ", end='')
            plant.display_info()
            print()
        stats = GardenManager.GardenStats(self)
        print(
            f"\nPlants added: {stats.total_plants()}, "
            f"Total growth: {stats.total_growth()}cm"
        )
        r, f, p = stats.plant_type()
        print(f"Plant types: {r} regular, {f} flowering, {p} prize flowers")


class GardenManager():
    """represents a garden manager overseeing multiple gardens"""
    garden = []

    class GardenStats():
        """represents statistics for a specific garden"""
        def __init__(self, garden) -> None:
            """initialize GardenStats with a specific garden"""
            self.garden = garden

        def total_plants(self) -> int:
            """return total number of plants in the garden"""
            return len(self.garden.plants)

        def total_growth(self) -> int:
            """return total growth (height) of
            all plants in the garden"""
            return len(self.garden.plants)

        def plant_type(self) -> tuple:
            """return count of each plant type in the garden"""
            regular = 0
            flowring = 0
            prize = 0
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowring += 1
                else:
                    regular += 1
            return regular, flowring, prize

    @classmethod
    def add_garden(cls, garden) -> None:
        """add a garden to the manager's list"""
        cls.garden.append(garden)

    @classmethod
    def create_garden_network(cls) -> dict:
        """create a network of gardens and calculate their scores"""
        scores = {}
        for garden in cls.garden:
            score = 0
            for plant in garden.plants:
                score += calculate_score(plant.height)
                if isinstance(plant, PrizeFlower):
                    score += plant.prize
            scores[garden.name] = score
        return scores

    @classmethod
    def total_gardens(cls) -> int:
        """return total number of gardens managed"""
        return len(cls.garden)


def ft_garden_analytics() -> None:
    """analyze the garden plants"""
    print("=== Garden Management System Demo ===\n")
    g1 = Garden("Alice")
    g2 = Garden("Bob")
    gm = GardenManager()
    gm.add_garden(g1)
    gm.add_garden(g2)
    p1 = Plant("Oak Tree", 100)
    p2 = FloweringPlant("Rose", 25, "red")
    p3 = PrizeFlower("Sunflower", 50, "yellow", 10)
    g1.add_plant(p1)
    g1.add_plant(p2)
    g1.add_plant(p3)
    print("\nAlice is helping all plants grow...")
    g1.grow_plants()
    g1.display_garden()
    print()
    valid_height = (
        validate_height(p1.height) and
        validate_height(p2.height) and
        validate_height(p3.height)
    )
    print(f"Height validation test: {valid_height}")
    scores = GardenManager.create_garden_network()
    print(
        f"Garden scores - {g1.name} : "
        f"{scores[g1.name]} , {g2.name} : {scores[g2.name]}"
    )
    print(f"Total gardens managed: {GardenManager.total_gardens()}")


if (__name__ == "__main__"):
    ft_garden_analytics()
