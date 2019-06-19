

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Unsupported operand type for +: {self} and {other}',
                            self=self.__class__.__name__,
                            other=other.__class__.__name__)
        return Vector(self.x + other.x, self.y + other.y)


class Particle:
    def __init__(self, weight, position: Vector,
                 velocity: Vector, acceleration: Vector):
        self.weight = weight
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration


class Emitter:
    def __init__(self, position: Vector, direction: Vector, angle):
        self.position = position
        self.direction = direction
        self.angle = angle // 360


class Field:
    def __init__(self):
        self.emitters = []
        self.particles = []

