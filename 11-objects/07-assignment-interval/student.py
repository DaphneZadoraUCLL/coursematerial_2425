class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def is_empty(self):
        return self.lower > self.upper

    def contains(self, value):
        return self.lower <= value <= self.upper

    def overlaps_with(self, other):
        if self.is_empty() or other.is_empty():
            return False

        if (self.contains(other.lower) or
            self.contains(other.upper) or
            other.contains(self.lower) or
                other.contains(self.upper)):
            return True

        return False
