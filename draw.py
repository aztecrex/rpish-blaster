from sense_hat import SenseHat

sense = SenseHat()


def plot(x, y, r, g, b):
    print('x={:d}, y={:d}, r={:d}, g={:d}, b={:d}'.format(x, y, r, g, b))

class Sprite:

    def __init__(self, offsets, r = 255, g = 255, b = 255):
        self.offsets = offsets
        self.r = r;
        self.g = g;
        self.b = b;

    def put(self, x, y):
        points = {(x + ox, y + oy) for (ox, oy) in self.offsets}
        for px, py in points:
            plot(px, py, self.r, self.g, self.b)
        if hasattr(self, 'oldpoints'):
            for px, py in {(ox , oy)
                    for (ox, oy) in self.oldpoints
                    if (ox, oy) not in points}:
                plot(px, py, 0, 0, 0)
        self.oldpoints = points;


cross = Sprite([(-1,-1),(-1,1),(1,-1),(1,1)])
cross.put(3,3)
cross.put(1,3)
