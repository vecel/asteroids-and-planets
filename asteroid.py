
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
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_x = 0
        self.acceleration_y = 0
        self.force_x = 0
        self.force_y = 0
        self.collide = False

    def set_acceleration(self, acc_x, acc_y):
        self.acceleration_x = acc_x
        self.acceleration_y = acc_y

    def set_velocity(self, vel_x, vel_y):
        self.velocity_x = vel_x
        self.velocity_y = vel_y

    def update(self):

        if self.collide:
            return

        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y

        self.x += self.velocity_x
        self.y += self.velocity_y