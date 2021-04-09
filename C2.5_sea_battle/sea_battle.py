class Playing_field:
    def __init__(self, name):
        self.name = name
        self.playing_field = [[" " for i in range(6)] for j in range(6)]

    def show_field(self):
        separator = "-----------------------------"
        yield " " * 12 + self.name + " " * 11
        yield " " * 4 + "| " + " | ".join(list(map(str, list(range(1, 7))))) + " |"
        yield separator
        for i, line in enumerate(self.playing_field):
            yield f"| {i + 1} | {' | '.join(line)} |"
            yield separator

class Ship:
    def __init__(self, length, direction):
        self.length = length
        self.direction = direction

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def show_field(self):
        print()
        for i, j in zip(self.player.show_field(), self.computer.show_field()):
            print(i + " " * 10 + j)
        print()

    @staticmethod
    def greeting():
        print("\n    Hi! This is a sea battle game.\n\
    You have to play with the computer.\n\
    The playing field is 6 by 6 cells.\n\
    Each player places 7 ships on the field:\n\
    1 ship three-cell ■ ■ ■\n\
    2 ships two-cell ■ ■\n\
    4 ships unicellular ■")
        result = input("    Ready for play? (Y/N): ").lower()
        if result == "y":
            return True
        else:
            return False

    def player_field_creation(self):
        pass

    def play_game(self):
        print(self.greeting())
            
            

player = Playing_field("player")
computer = Playing_field("computer")
game = Game(player, computer)
game.play_game()



# Ships can not be located in adjacent cells.