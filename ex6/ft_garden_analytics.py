class Plant:
    def __init__(self,name,height):
        self.name = name
        self.height = height

class FloweringPlant(Plant):
    def __init__(self, name, height,blooming):
        super().__init__(name, height)
        