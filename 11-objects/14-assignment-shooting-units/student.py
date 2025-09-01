class Unit:
    def __init__(self, health, firepower, armor):
        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError(
                "Alle waarden moeten groter of gelijk aan 0 zijn.")

        self._health = health
        self._firepower = firepower
        self._armor = armor

    @property
    def health(self):
        return self._health

    @property
    def firepower(self):
        return self._firepower

    @property
    def armor(self):
        return self._armor

    def shot_by(self, other):
        damage = other.firepower - self._armor
        if damage < 0:
            damage = 0
        self._health -= damage
        if self._health < 0:
            self._health = 0
