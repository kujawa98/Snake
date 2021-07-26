class AnchorPoint:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def update(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def __eq__(self, other):
        if not isinstance(other, AnchorPoint):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.x == other.x and self.y == other.y
