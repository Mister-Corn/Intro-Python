class Player:
    def __init__(self, location, name='Player'):
        self.location = location
        self.name = name
        self.freedom = 0

    def move(self, direction):
        self.location = self.location.getNextLocation(self.freedom, direction)