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
            self.luck += 5
        elif self.sign == "The Tower":
            self.endurance +=10
            self.willpower +=10
        elif self.sign == "The Warrior":
            self.strength += 10
            self.endurance += 5
        elif self.sign == "The Thief":
            self.luck == 15
        elif self.sign == "The Moon":
            self.intelligence += 10
            self.willpower +=5

    def show_stats(self):
        print("""Your attributes are:\nStrength: {}\nEndurance: {}\nAgility: {}
Intelligence: {}\nWillpower: {}\nCharisma: {}\nLuck: {}\n
        """.format(self.strength, self.endurance, self.agility, self.intelligence, self.willpower, self.charisma, self.luck))
        print("""Your stats are:\nBlade: {}\nBlock: {}\nBlunt: {}\nBow: {}
Heavy Armor: {}\nLight Armor: {}\nSneak: {}\nDestruct: {}\nHeal: {}\nSpeech: {}\nBarter: {}\n
""".format(self.blade,self.block,self.blunt,self.bow,self.heavy_armor,self.light_armor,self.sneak,self.destruct,self.heal,self.speech,self.barter))

    def focus_area(self):
        self.blade += int((self.strength + self.agility + 2)/4)
        self.block += int((self.strength + self.endurance)/4)
        self.blunt += int((self.strength * 2)/3)
        self.bow += int(((self.agility * 2)/4)+ self.luck/4)
        self.heavy_armor += int((self.strength + self.endurance)/4)
        self.light_armor += int((self.agility + self.endurance)/4)
        self.sneak += int((self.agility + self.luck)/4)
        self.destruct += int((self.intelligence + self.willpower)/4)
        self.heal += int((self.willpower * 2.5)/4)
        self.speech += int((self.charisma)/2)
        self.barter += int((self.charisma + self.luck)/3)

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
    name = input("Enter character name\n-").title()
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
    elif race == "High Elf":
        player = HighElf(name)
    elif race == "Wood Elf":
        player = WoodElf(name)
    elif race == "Argonian":
        player = Argonian(name)
    elif race == "Khajit":
        player = Khajit(name)
    return player




person = ask_name_race()

person.calc_sign(person.choose_sign())
choice = ask_class(person)
the_class = CharacterClass(choice)
the_class.stats(person)
person.focus_area()
person.show_stats()
