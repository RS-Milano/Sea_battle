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

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def show_field(self):
        print()
        for i, j in zip(self.player.show_field(), self.computer.show_field()):
            print(i + " " * 10 + j)
        print()

player_field = Playing_field("player")
computer_field = Playing_field("computer")
game = Game(player_field, computer_field)
game.show_field()