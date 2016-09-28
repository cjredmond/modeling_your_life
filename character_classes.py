class CharacterClass:
    def __init__(self, choice):
        self.choice = choice

    def stats(self, character):
        if self.choice == "Warrior":
            character.blade +=10
            character.block +=10
            character.heavy_armor +=10
            character.blunt +=5
        elif self.choice == "Knight":
            character.blade +=10
            character.heavy_armor +=10
            character.speech +=10
            character.heal +=10
        elif self.choice == "Spellsword":
            character.blade += 10
            character.heal += 10
            character.destruct +=10
            character.heavy_armor +=5
        elif self.choice == "Scout":
            character.light_armor +=10
            character.sneak +=10
            character.speech +=10
            character.blade +=5
        elif self.choice == "Archer":
            character.bow += 15
            character.light_armor +=10
            character.sneak += 10
        elif self.choice == "Assassin":
            character.sneak += 15
            character.bow += 10
            character.speech += 10
        elif self.choice == "Thief":
            character.sneak += 10
            character.barter +=10
            character.light_armor +=10
            character.blade += 5
        elif self.choice == "Sorcerer":
            character.destruct += 15
            character.heal += 10
            character.light_armor +=10
        else:
            character.destruct+=20
            character.heal +=15
