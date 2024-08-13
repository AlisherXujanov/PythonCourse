# It may help for this assignment to be slightly familiar with with the card game Pokemon, but it's not necessary. The key element of the game that we are simulating here is that a creature can be "trained", which enhances some its capabilities (health, defense, attack, etc.) If trained enough, a creature can "evolve" into a different creature.

# The class Pokemon is provided below. Each instance describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create.

# Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are different.

# For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a lot of different moves!".

# Then create an instance of this class with the name as "Belle". Assign this instance to the variable p1. The hidden test that runs when you submit your assignment will invoke your .action() method and check that it returns the correct string.

class Pokemon(object):
    attack = 12        # The "baseline" attack,...
    defense = 10        # defense, and...
    health = 15        # health scores for new Pokemon instances
    # The "type" (like 'Normal', 'Water', 'Fire', etc.) helps determine how effective certain moves will be
    p_type = "Normal"

    # When we "train", this is how much we increment our attack,...
    attack_boost = 3
    defense_boost = 2   # defense, and...
    health_boost = 5   # health

    evolution_threshold = 10  # How many times we need to train before we "evolve"

    def __init__(self, name, level=5):
        self.name = name   # The name for this *instance*
        # The starting level for this instance (the initial underscore signals that it is a private variable)
        self._level = level

    @property
    def level(self):  # *GETTER* for the 'level' property
        return self._level

    @level.setter
    def level(self, value):  # *SETTER* for the 'level' property, ensuring that it is at least 1
        if value < 1:
            raise ValueError("Level must be greater than or equal to 1")
        self._level = value

    def train(self):
        # Increment attack, defense, and health levels
        self.attack_up()
        self.defense_up()
        self.health_up()

        self.level = self.level + 1  # Increment the level

        # Did we "evolve" on this step?
        evolved = (self.level % self.evolution_threshold == 0)

        # Return a tuple with the current level and whether we evolved
        return self.level, evolved

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)


class Grass_Pokemon(Pokemon):
    attack = 15  # base levels for grass pokemon
    defense = 14
    health = 12
    p_type = "Grass"

    attack_boost = 2  # when we "train", how much to increment by
    defense_boost = 3
    health_boost = 6

    evolution_threshold = 12  # How many times we need to train before we "evolve"

    def action(self):
        return f"{self.name} knows a lot of different moves!"

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def train(self):
        if self.level >= 10:
            self.attack_up()
        self.defense_up()
        self.health_up()

        self.level = self.level + 1  # Increment the level

        # Did we "evolve" on this step?
        evolved = (self.level % self.evolution_threshold == 0)

        # Return a tuple with the current level and whether we evolved
        return self.level, evolved


# YOUR CODE HERE
p1 = Grass_Pokemon("Belle")
p1.action = lambda: f"{p1.name} knows a lot of different moves!"
print(p1.action())
print(p1.moves())
print(p1.p_moves)

# Modify the `Grass_Pokemon` subclass so that, when trained, the attack strength for `Grass_Pokemon` instances increases * only * if they are at level 10 or higher. This means that if they transition from level `9` to level `10`, their `attack` should ** not ** increase. If they transition from `10` to `11`, their `attack` should increment by `attack_boost`. Do not change anything in the parent `Pokemon` class .

# To test, create an instance of `Grass_Pokemon` with the `name` as `"Bulby"`. Assign the instance to the variable `p2`. Create another instance of the `Grass_Pokemon` class with the name set to `"Pika"` and assign that instance to the variable `p3`. Then, use `Grass_Pokemon` methods to train the `p3` `Grass_Pokemon` instance until it reaches at least level 10.


# YOUR CODE HERE
p2 = Grass_Pokemon("Bulby")
p3 = Grass_Pokemon("Pika")


# Now, suppose different Pokemon types have strengths against other types. For example, "Water" Pokemon are strong against "Fire" Pokemon. Along with the `Pokemon` parent class , we have also provided several subclasses. We also added a `strong_vs` class variable to track which types of Pokemon this type is strong against.

# - **Grass ** is strong against * Water*
# - **Fire ** is strong against * Normal * and *Grass*
# - **Water ** is strong against * Fire*
# - **Normal ** is not strong against any type


# Write two methods in the `Pokemon` parent class that will be inherited by the subclasses:

# - `is_strong_vs(self, opponent)`: accepts an `opponent`, which is a `Pokemon` instance. It should return `true` if type `p_type` of `opponent` is in `self.strong_vs` and `false` otherwise
# - `is_weak_vs(self, opponent)`: accepts an `opponent`, which is a `Pokemon` instance. It should return `true` if the ** opponent ** is strong against `self` (you probably want to reference `opponent.is_strong_vs`)

class Pokemon():
    attack = 12        # The "baseline" attack,...
    defense = 10        # defense, and...
    health = 15        # health scores for new Pokemon instances
    # The "type" (like 'Normal', 'Water', 'Fire', etc.) helps determine how effective certain moves will be
    p_type = "Normal"

    # When we "train", this is how much we increment our attack,...
    attack_boost = 3
    defense_boost = 2   # defense, and...
    health_boost = 5   # health

    evolution_threshold = 10  # How many times we need to train before we "evolve"

    strong_vs = []

    def __init__(self, name, level=5):
        self.name = name  # The name for this *instance*
        # The starting level for this instance (the initial underscore signals that it is a private variable)
        self._level = level

    @property
    def level(self):  # *GETTER* for the 'level' property
        return self._level

    @level.setter
    def level(self, value):  # *SETTER* for the 'level' property, ensuring that it is at least 1
        if value < 1:
            raise ValueError("Level must be greater than or equal to 1")
        self._level = value

    def train(self):
        # Increment attack, defense, and health levels
        self.attack_up()
        self.defense_up()
        self.health_up()

        self.level = self.level + 1  # Increment the level

        # Did we "evolve" on this step?
        evolved = (self.level % self.evolution_threshold == 0)

        # Return a tuple with the current level and whether we evolved
        return self.level, evolved

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

    def is_strong_vs(self, opponent):
        return opponent.p_type in self.strong_vs

    def is_weak_vs(self, opponent):
        return opponent.is_strong_vs(self)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    attack_boost = 2
    defense_boost = 3
    health_boost = 6

    p_type = "Grass"

    strong_vs = ["Water"]


class Fire_Pokemon(Pokemon):
    p_type = "Fire"

    strong_vs = ["Grass", "Normal"]


class Water_Pokemon(Pokemon):
    p_type = "Water"

    strong_vs = ["Fire"]


# YOUR CODE HERE
p = Pokemon("p")
g = Grass_Pokemon("g")
f = Fire_Pokemon("f")
w = Water_Pokemon("w")

print(p.is_strong_vs(g))