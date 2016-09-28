from character_classes import CharacterClass

class Player:
    def __init__(self):
        self.strength = 20
        self.agility = 20
        self.endurance = 20
        self.intelligence = 20
        self.willpower = 20
        self.charisma = 20
        self.luck = 20
        ##############
        self.blade = 20
        self.blunt = 20
        self.block = 20
        self.bow = 20
        self.heavy_armor = 20
        self.light_armor = 20
        self.sneak = 20
        self.destruct = 20
        self.heal = 20
        self.regen = 20
        self.magic = 20
        self.speech = 20
        self.barter = 20

    def choose_sign(self):
        sign = input("""What is the birthsign of your character? \n
                    The Shadow
                    The Tower
                    The Warrior
                    The Thief
                    The Moon\n""").title()
        self.sign = sign
        return sign

    def calc_sign(self, sign):
        if self.sign == "The Shadow":
            self.agility += 10
        elif self.sign == "The Tower":
            self.endurance +=10
        elif self.sign == "The Warrior":
            self.strength += 10
        elif self.sign == "The Thief":
            self.luck == 10
        else:
            self.intelligence += 10

class Nord(Player):
    def __init__(self):
        super().__init__()
        self.strength += 10
        self.endurance += 10
        self.charisma -= 10
class Redgaurd(Player):
    def __init__(self):
        super().__init__()
        self.strength += 10
        self.agility += 10
        self.intelligence -= 10
class HighElf(Player):
    def __init__(self):
        super().__init__()
        self.intelligence += 10
        self.willpower += 10
        self.endurance -= 10
class DarkElf(Player):
    def __init__(self):
        super().__init__()
        self.agility += 10
        self.intelligence += 10
        self.charisma -= 10
class WoodElf(Player):
    def __init__(self):
        super().__init__()
        self.agility += 10
        self.willpower += 10
        self.strength -= 10
class Orc(Player):
    def __init__(self):
        super().__init__()
        self.strength += 15
        self.endurance += 10
        self.willpower -= 10
        self.charisma -= 5
class Argonian(Player):
    def __init__(self):
        super().__init__()
        self.agility += 10
        self.endurance += 5
        self.intelligence -= 5
class Khajit(Player):
    def __init__(self):
        super().__init__()
        self.agility += 15
        self.endurance += 5
        self.charisma -= 10


def ask(character):
    class_choice = input("""What will your character class be?\n Warrior\n Knight\n
    Spellsword\n Scout\n Archer\n Assassin\n Thief\n Sorcerer\n Mage""").title()
    return class_choice


connor = Nord()
q = ask(connor)
the_class = CharacterClass(q)
the_class.stats(connor)
the_sign = connor.choose_sign()
connor.calc_sign(the_sign)
print(connor.strength, connor.blade, connor.destruct)
