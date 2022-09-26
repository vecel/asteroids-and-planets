
from circle import Circle

class Planet(Circle):
    
    def __init__(self, color, x, y, radius, mass) -> None:
        Circle.__init__(self, color, x, y, radius)
        self.mass = mass
