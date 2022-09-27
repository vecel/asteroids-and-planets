
import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
def sin(origin_x, origin_y, x, y):
    return (origin_y - y) / dist(origin_x, origin_y, x, y)

def cos(origin_x, origin_y, x, y):
    return (origin_x - x) / dist(origin_x, origin_y, x, y)
