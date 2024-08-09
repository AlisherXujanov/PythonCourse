class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return "{} knows a lot of different moves!".format(self.name)


p1 = Grass_Pokemon('Belle')
print(p1)
# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================


class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level += 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack += self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense += self.defense_boost
        return self.defense

    def health_up(self):
        self.health += self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def train(self):
        # Only allow training if the level is less than 10
        if self.level < 10:
            self.update()
            if self.level >= 10:
                self.attack_up()
            self.defense_up()
            self.health_up()
            self.level += 1
            if self.level % self.evolve == 0:
                return self.level, "Evolved!"
            else:
                return self.level
        else:
            return "Cannot train: level 10 reached."


p2 = Grass_Pokemon("Bulby")
p3 = Grass_Pokemon("Pika")
print(p2)
print(p3)

# Train p3
while p3.level < 10:
    print(p3.train())
# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================
class Pokemon(object):
    base_attack = 12
    base_defense = 10
    base_health = 15
    p_type = "Normal"
    strong_vs = []

    def __init__(self, name, level=5):
        self.name = name
        self.level = level
        self.update()

    def train(self):
        self.level += 1
        if self.level >= self.evolve:
            return self.level, "Evolved!"
        else:
            return self.level

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def is_strong_vs(self, opponent):
        return opponent.p_type in self.strong_vs

    def is_weak_vs(self, opponent):
        return opponent.is_strong_vs(self)

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}, Attack: {}, Defense: {}, Health: {}".format(
            self.name, self.p_type, self.level, self.attack, self.defense, self.health
        )
        
        
        
class Grass_Pokemon(Pokemon):
    base_attack = 15
    base_defense = 14
    base_health = 12
    p_type = "Grass"
    strong_vs = ["Water"]

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 10

        # Initialize base stats with overrides
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.health = self.base_health

    def train(self):
        result = super().train()
        if self.level > 10:  # Only increase attack if level is greater than 10
            self.attack += self.attack_boost
        return result

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return "{} knows a lot of different moves!".format(self.name)


class Fire_Pokemon(Pokemon):
    base_attack = 18
    base_defense = 12
    base_health = 14
    p_type = "Fire"
    strong_vs = ["Normal", "Grass"]

    def update(self):
        self.health_boost = 5
        self.attack_boost = 4
        self.defense_boost = 3
        self.evolve = 10

        # Initialize base stats with overrides
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.health = self.base_health

    def train(self):
        super().train()


class Water_Pokemon(Pokemon):
    base_attack = 14
    base_defense = 15
    base_health = 16
    p_type = "Water"
    strong_vs = ["Fire"]

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

        # Initialize base stats with overrides
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.health = self.base_health

    def train(self):
        super().train()


class Normal_Pokemon(Pokemon):
    base_attack = 10
    base_defense = 10
    base_health = 10
    p_type = "Normal"
    strong_vs = []  # Normal type is not strong against any type

    def update(self):
        self.health_boost = 5
        self.attack_boost = 2
        self.defense_boost = 2
        self.evolve = 10

        # Initialize base stats with overrides
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.health = self.base_health

    def train(self):
        super().train()


# Test implementation
grass = Grass_Pokemon("Chlorophyll")
fire = Fire_Pokemon("Flamey")  # Correctly using Fire_Pokemon without underscore
water = Water_Pokemon("Aquatic")
normal = Normal_Pokemon("Norman")

# Print out the Pokémon to check their details
print(grass)
print(fire)
print(water)
print(normal)

# Test is_strong_vs and is_weak_vs methods
print(grass.is_strong_vs(water))  # Expected output: True
print(fire.is_strong_vs(normal))  # Expected output: True
print(water.is_strong_vs(fire))  # Expected output: True
print(normal.is_strong_vs(grass))  # Expected output: False

print(grass.is_weak_vs(water))  # Expected output: False
print(fire.is_weak_vs(normal))  # Expected output: False
print(water.is_weak_vs(fire))  # Expected output: False
print(normal.is_weak_vs(grass))  # Expected output: False
