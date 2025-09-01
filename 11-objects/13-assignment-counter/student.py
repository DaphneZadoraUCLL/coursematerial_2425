class Counter:
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def reset(self):
        self._count = 0

    @property
    def count(self):
        return self._count
