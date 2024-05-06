# function to get the sin of an angle
import math
def sin(angle):
    if angle < 0:
        angle = 360 + angle
    return math.sin(math.radians(angle))

# function to get the cos of an angle
def cos(angle):
    if angle < 0:
        angle = 360 + angle
    return math.cos(math.radians(angle))

# function to get the tan of an angle
def tan(angle):
    if angle < 0:
        angle = 360 + angle
    return math.tan(math.radians(angle))
