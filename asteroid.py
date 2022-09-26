
from circle import Circle

DEFAULT_COLOR = (200, 200, 200)
DEFAULT_X, DEFAULT_Y = 30, 30
DEFAULT_RADIUS = 15
DEFAULT_MASS = 10

class Asteroid(Circle):

    def __init__(
        self, 
        color = DEFAULT_COLOR, 
        x = DEFAULT_X, 
        y = DEFAULT_Y, 
        radius = DEFAULT_RADIUS, 
        mass = DEFAULT_MASS) -> None:

        Circle.__init__(self, color, x, y, radius)
        self.mass = mass
