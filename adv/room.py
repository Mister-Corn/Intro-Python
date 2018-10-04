class Room:
    def __init__(self):
        self.name = {
            0: None,
            1: None,
            2: None,
            3: None
        }
        self.description = {
            0: None,
            1: None,
            2: None,
            3: None
        }
        self.error = {
            0: None,
            1: None,
            2: None,
            3: None
        }
        self.level_up = {
            0: None,
            1: None,
            2: None,
            3: None
        }
        self.direction = {
            0: {
                'n_to': None,
                's_to': None,
                'e_to': None,
                'w_to': None
            },
            1: {
                'n_to': None,
                's_to': None,
                'e_to': None,
                'w_to': None
            },
            2: {
                'n_to': None,
                's_to': None,
                'e_to': None,
                'w_to': None
            },
            3: {
                'n_to': None,
                's_to': None,
                'e_to': None,
                'w_to': None
            }
        }


    def getNextLocation(self, level, direction):
        return self.direction[level][f"{direction}_to"]


    def getLocationDetails(self, level):
        return f'\n---{self.name[level]}---\n\n{self.description[level]}'


    # def __repr__(self):
    #     return f"|Room| name: {self.name}\ndescription: {self.description}\ndirection: {self.direction}\nlevel_up: {self.level_up}\nerror: {self.error}\n"

    def __repr__(self, level=0):
        return f"|Room| direction: {self.direction[level]}\n"