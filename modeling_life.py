class Physical:
    def __init__(self):
        pass

class Workout(Physical):
    def __init__(self):
        self.happiness = 5
        self.energy_consumed = 3
        self.time = 3

    def soreness(self, number):
        self.soreness = number


class Sport(Physical):
    def __init__(self):
        self.happiness = 4
        self.energy_consumed = 5
        self.time = 3
        self.soreness = 4

class Mental:
    def __init__(self):
        pass

class Sleep(Mental):
    def __init__(self, hours):
        if hours > 7:
            self.happiness = 5
        elif hours > 6:
            self.happiness = 4
        else:
            self.happiness = 2

class Diet(Mental):
    def __init__(self, rating)


gym = Workout()
gym.soreness(4)
print(gym.soreness)
