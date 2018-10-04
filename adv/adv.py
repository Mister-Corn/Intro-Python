from player import Player
from rms import rooms as myRooms
from jankyhelpers import importRoomsFromMyFile


debug = True
rooms = {}


def handleInput(input):
    valid_directions = {
        'n': 'n',
        's': 's',
        'e': 'e',
        'w': 'w'
    }

    cmds = input.lower().split(' ')
    if len(cmds) == 1:
        cmd = cmds[0]
        print(f"cmd: {cmd}")
        if cmd in valid_directions:
            player.move(cmd)

def initializeGameWithPlayer(player):
    def handleInput(input):
        valid_directions = {
            'n': 'n',
            's': 's',
            'e': 'e',
            'w': 'w'
        }

        cmds = input.lower().split(' ')
        if len(cmds) == 1:
            cmd = cmds[0]
            print(f"cmd: {cmd}")
            if cmd in valid_directions:
                player.move(cmd)
    
    return {
        'handleInput': handleInput
    }


def main():
    importRoomsFromMyFile(myRooms, rooms)

    if debug:
        # for room in rooms:
        #     print(f"{room}: {rooms[room]}")
        print(rooms['overlook'].direction[0]['s_to'])

    # Initialize Player and Game
    player = Player(rooms['outside'], 'tester') #input('What is your name?\n')
    handleInput = initializeGameWithPlayer(player)['handleInput']

    # Input Loop
    while True:
        print(player.location.getLocationDetails(player.freedom))
        cmds = input('\n>>>')
        if cmds == 'q':
            break
        else:
            handleInput(cmds)


main()