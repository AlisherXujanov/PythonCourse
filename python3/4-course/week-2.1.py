# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================
# It may help for this assignment to be slightly familiar with with the card game Pokemon, but it's not necessary. The key element of the game that we are simulating here is that a creature can be "trained", which enhances some its capabilities (health, defense, attack, etc.) If trained enough, a creature can "evolve" into a different creature.

# The class Pokemon is provided below. Each instance describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create.

# Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are different.

# For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a lot of different moves!".

# Then create an instance of this class with the name as "Belle". Assign this instance to the variable p1. The hidden test that runs when you submit your assignment will invoke your .action() method and check that it returns the correct string.

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
# Modify the `Grass_Pokemon` subclass so that, when trained, the attack strength for `Grass_Pokemon` instances increases * only * if they are at level 10 or higher. This means that if they transition from level `9` to level `10`, their `attack` should ** not ** increase. If they transition from `10` to `11`, their `attack` should increment by `attack_boost`. Do not change anything in the parent `Pokemon` class.

# To test, create an instance of `Grass_Pokemon` with the `name` as `"Bulby"`. Assign the instance to the variable `p2`. Create another instance of the `Grass_Pokemon` class with the name set to `"Pika"` and assign that instance to the variable `p3`. Then, use `Grass_Pokemon` methods to train the `p3` `Grass_Pokemon` instance until it reaches at least level 10.


# assert isinstance(p2, Grass_Pokemon), "p2 is not the correct type"
# assert isinstance(p3, Grass_Pokemon), "p3 is not the correct type"

# assert p2.__str__() == "Pokemon name: Bulby, Type: Grass, Level: 5", "p2 does not have the correct value"
# assert p3.level >= 10, "p3 does not have the correct level; only train to level 10"
# assert p3.attack_up() >= 17, "p3 does not have the correct attack value at level 10"
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
# Now, suppose different Pokemon types have strengths against other types. For example, "Water" Pokemon are strong against "Fire" Pokemon. Along with the `Pokemon` parent class , we have also provided several subclasses. We also added a `strong_vs` class variable to track which types of Pokemon this type is strong against.

# - **Grass ** is strong against * Water*
# - **Fire ** is strong against * Normal * and *Grass*
# - **Water ** is strong against * Fire*
# - **Normal ** is not strong against any type


# Write two methods in the `Pokemon` parent class that will be inherited by the subclasses:

# - `is_strong_vs(self, opponent)`: accepts an `opponent`, which is a `Pokemon` instance. It should return `true` if type `p_type` of `opponent` is in `self.strong_vs` and `false` otherwise
# - `is_weak_vs(self, opponent)`: accepts an `opponent`, which is a `Pokemon` instance. It should return `true` if the ** opponent ** is strong against `self` (you probably want to reference `opponent.is_strong_vs`)


# p1 = Grass_Pokemon('Belle')
# print(p1)

# assert isinstance(p2, Grass_Pokemon), "p2 is not the correct type"
# assert isinstance(p3, Grass_Pokemon), "p3 is not the correct type"

# assert p2.__str__() == "Pokemon name: Bulby, Type: Grass, Level: 5", "p2 does not have the correct value"
# assert p3.level >= 10, "p3 does not have the correct level; only train to level 10"
# assert p3.attack_up() >= 17, "p3 does not have the correct attack value at level 10"
# =====================================================================================
# =====================================================================================


class Pokemon():
    attack  = 12        # The "baseline" attack,...
    defense = 10        # defense, and...
    health  = 15        # health scores for new Pokemon instances
    p_type  = "Normal"  # The "type" (like 'Normal', 'Water', 'Fire', etc.) helps determine how effective certain moves will be

    attack_boost  = 3   # When we "train", this is how much we increment our attack,...
    defense_boost = 2   # defense, and...
    health_boost  = 5   # health

    evolution_threshold = 10 # How many times we need to train before we "evolve"

    strong_vs = []

    def __init__(self, name, level = 5):
        self.name  = name  # The name for this *instance*
        self._level = level # The starting level for this instance (the initial underscore signals that it is a private variable)

    @property
    def level(self): # *GETTER* for the 'level' property
        return self._level

    @level.setter
    def level(self, value): # *SETTER* for the 'level' property, ensuring that it is at least 1
        if value < 1:
            raise ValueError("Level must be greater than or equal to 1")
        self._level = value

    def train(self):
        # Increment attack, defense, and health levels
        self.attack_up()
        self.defense_up()
        self.health_up()

        self.level   = self.level + 1 # Increment the level

        evolved = (self.level % self.evolution_threshold == 0) # Did we "evolve" on this step?
        
        return self.level, evolved # Return a tuple with the current level and whether we evolved

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
    attack  = 15
    defense = 14
    health  = 12
    attack_boost  = 2
    defense_boost = 3
    health_boost  = 6
    p_type    = "Grass"
    strong_vs = ["Water"]



class Fire_Pokemon(Pokemon):
    p_type    = "Fire"
    strong_vs = ["Grass", "Normal"]


class Water_Pokemon(Pokemon):
    p_type    = "Water"
    strong_vs = ["Fire"]