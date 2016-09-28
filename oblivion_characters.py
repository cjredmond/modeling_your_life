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
        self.speech = 20
        self.barter = 20

    def choose_sign(self):
        sign = input("""What is the birthsign of your character? \n
The Shadow\nThe Tower\nThe Warrior\nThe Thief\nThe Moon\n""").title()
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

    def show_stats(self):
        print("""Your attributes are:\nStrength: {}\nEndurance: {}\nAgility: {}
Intelligence: {}\nWillpower: {}\nCharisma: {}\nLuck: {}\n
        """.format(self.strength, self.endurance, self.agility, self.intelligence, self.willpower, self.charisma, self.luck))
        print("""Your stats are:\nBlade: {}\nBlock: {}\nBlunt: {}\nBow: {}
Heavy Armor: {}\nLight Armor: {}\nSneak: {}\nDestruct: {}\nHeal: {}\nSpeech: {}\nBarter: {}\n
""".format(self.blade,self.block,self.blunt,self.bow,self.heavy_armor,self.light_armor,self.sneak,self.destruct,self.heal,self.speech,self.barter))

class Nord(Player):
    def __init__(self,name):
        super().__init__()
        self.strength += 10
        self.endurance += 10
        self.charisma -= 10
        self.name = name
class Redgaurd(Player):
    def __init__(self,name):
        super().__init__()
        self.strength += 10
        self.agility += 10
        self.intelligence -= 10
        self.name = name
class HighElf(Player):
    def __init__(self,name):
        super().__init__()
        self.intelligence += 10
        self.willpower += 10
        self.endurance -= 10
        self.name = name
class DarkElf(Player):
    def __init__(self,name):
        super().__init__()
        self.agility += 10
        self.intelligence += 10
        self.charisma -= 10
        self.name = name
class WoodElf(Player):
    def __init__(self,name):
        super().__init__()
        self.agility += 10
        self.willpower += 10
        self.strength -= 10
        self.name = name
class Orc(Player):
    def __init__(self,name):
        super().__init__()
        self.strength += 15
        self.endurance += 10
        self.willpower -= 10
        self.charisma -= 5
        self.name = name
class Argonian(Player):
    def __init__(self,name):
        super().__init__()
        self.agility += 10
        self.endurance += 5
        self.intelligence -= 5
        self.name = name
class Khajit(Player):
    def __init__(self,name):
        super().__init__()
        self.agility += 15
        self.endurance += 5
        self.charisma -= 10
        self.name = name
class Imperial(Player):
    def __init__(self,name):
        super().__init__()
        self.endurance +=10
        self.charisma +=10
        self.willpower -= 10


def ask_class(character):
    class_choice = input("""What will your character class be?\nWarrior\nKnight
Spellsword\nScout\nArcher\nAssassin\nThief\nSorcerer\nMage\n""").title()
    return class_choice

def ask_name_race():
    name = input("Enter character name").title()
    race = input("Enter your characters race, Orc, Nord, Imperial, Redgaurd, Dark Elf, High Elf, Wood Elf, Argonian, or Khajit.\n-").title()
    if race == "Orc":
        player = Orc(name)
    elif race == "Nord":
        player = Nord(name)
    elif race == "Imperial":
        player = Imperial(name)
    elif race == "Redgaurd":
        player = Redgaurd(name)
    elif race == "Dark Elf":
        player = DarkElf(name)
    elif player == "High Elf":
        player = HighElf(name)
    elif player == "Wood Elf":
        player = WoodElf(name)
    elif player == "Argonian":
        player = Argonian(name)
    elif player == "Khajit":
        player = Khajit(name)
    return player




thing = ask_name_race()
thing.calc_sign(thing.choose_sign())
choice = ask_class(thing)
the_class = CharacterClass(choice)
the_class.stats(thing)

thing.show_stats()
