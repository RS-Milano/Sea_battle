from random import randint

class Playing_field:
    def __init__(self, name, size = 6, hide = False):
        self.name = name
        self.size = size
        self.hide = hide
        self.playing_field = [[" "] * self.size for _ in range(self.size)]
        self.busy = []
        self.ships = []

    def show_field(self):
        length = len(" " * 6 + "|  " + "  |  ".join(list(map(str, list(range(1, self.size + 1))))) + "  |")
        separator = "-" * length
        yield " " * (int(length / 2) - int(len(self.name) / 2) + 1) + self.name + " " * (int(length / 2) - int(len(self.name) / 2))
        yield " " * 6 + "|  " + "  |  ".join(list(map(str, list(range(1, self.size + 1))))) + "  |"
        yield separator
        for i, line in enumerate(self.playing_field):
            if i > 8:
                yield f"|  {i + 1} |  {'  |  '.join(line)}  |".replace("■", " ") if self.hide else f"|  {i + 1} |  {'  |  '.join(line)}  |"
            else:
                yield f"|  {i + 1}  |  {'  |  '.join(line)}  |".replace("■", " ") if self.hide else f"|  {i + 1}  |  {'  |  '.join(line)}  |"
            yield separator

    def add_ship(self, ship):
        flag = True
        for i in ship.ship_cells:
            if i in self.busy:
                flag = False
        if flag:
            self.ships.append(ship)
            for i in ship.ship_cells:
                self.busy.append(i)
                self.playing_field[i[0]][i[1]] = "■"
            for i in ship.ship_perimeter:
                if i not in self.busy:
                    self.busy.append(i)
        else:
            raise WrongShipException()
    
    def fill_the_field(self):
        ship_list = [3, 2, 2, 1, 1, 1, 1] if self.size < 10 else [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for i in ship_list:
            counter = 0
            while counter < 20:
                try:
                    new_ship = Ship(self, i)
                    self.add_ship(new_ship)
                except WrongShipException:
                    counter += 1
                else:
                    break
        if len(self.ships) == len(ship_list):
            return True
        else:
            raise FieldCreationException()

    def generate_field(self):
        while True:
            try:
                self.fill_the_field()
            except FieldCreationException:
                self.playing_field = [[" "] * self.size for _ in range(self.size)]
                self.busy = []
                self.ships = []
                continue
            else:
                break
    def take_a_shot(self, shot):
        if self.playing_field[shot[0]][shot[1]] == "o" or self.playing_field[shot[0]][shot[1]] == "X":
            raise ShootedCellException()
        else:
            for i in self.ships:
                if shot in i.ship_cells:
                    self.playing_field[shot[0]][shot[1]] = "X"
                    i.helth -= 1
                    if i.helth == 0:
                        for j in i.ship_perimeter:
                            self.playing_field[j[0]][j[1]] = "o"
                    return True
            self.playing_field[shot[0]][shot[1]] = "o"
            return False

    def check_win(self):
        counter = 0
        for i in self.ships:
            if i.helth == 0:
                counter += 1
        if counter == len(self.ships):
            return True
        else:
            return False


class Ship:
    def __init__(self, field, length):
        self.field = field
        self.length = length
        self.helth = length
        self.direction = randint(0, 1)
        self.bow_cell = (randint(0, self.field.size - self.length), randint(0, self.field.size - self.length))

    @property
    def ship_cells(self):
        result = []
        for i in range(self.length):
            if self.direction:
                result.append((self.bow_cell[0] + i, self.bow_cell[1]))
            else:
                result.append((self.bow_cell[0], self.bow_cell[1] + i))
        return result

    def hit(self, shot):
        return shot in self.ship_cells
    
    @property
    def ship_perimeter(self):
        result = []
        template = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in self.ship_cells:
            for j in template:
                cell = (i[0] + j[0], i[1] + j[1])
                if 0 <= cell[0] < self.field.size and 0 <= cell[1] < self.field.size and cell not in self.ship_cells and cell not in result:
                    result.append(cell)
        return result

class Participants:
    def __init__(self, field):
        self.field = field

    def get_move(self):
        raise NotImplementedError()

class AI(Participants):
    def get_move(self):
        return (randint(0, self.field.size - 1), randint(0, self.field.size - 1))

class Player(Participants):
    def get_move(self):
        reference = ""
        for i in range(self.field.size):
            reference += str(i + 1)
        while True:
            move = input("Your turn\nEnter the coordinates of the shot (without space, for example: 12)\n\
First digit - row number\nSecond digit - column number\n")
            if len(move) == 2 and move[0] in reference and move[1] in reference:
                move = list(map(int, list(move)))
                return tuple(map(lambda x: x - 1, move))
            else:
                print("Incorrect input!")

class SeaBattleException(Exception):
    pass

class WrongShipException(SeaBattleException):
    def __str__(self):
        return "The ship cannot be placed on the field"

class FieldCreationException(SeaBattleException):
    def __str__(self):
        return "The ship cannot be placed on the field"

class ShootedCellException(SeaBattleException):
    def __str__(self):
        return "This cell has already been shot"

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def show_field(self):
        print()
        for i, j in zip(self.player.show_field(), self.computer.show_field()):
            print(i + " " * 10 + j)
        print()

    def greeting(self):
        print(f"    Hi! This is a sea battle game.\n\
    You have to play with the computer.\n\
    The playing field is {self.player.size} by {self.player.size} cells.\n\
    Each player have 7 ships on the field:\n\
    1 ship three-cell ■ ■ ■\n\
    2 ships two-cell ■ ■\n\
    4 ships unicellular ■")
        result = input("    Ready for play? (Y/N): ").lower()
        if result == "y":
            return True
        else:
            return False

    def player_field_creation(self):
        print("Let's place your ships on the field")

    def play_game(self):
        if self.greeting():
            self.player.generate_field()
            self.computer.generate_field()
        switch = True
        while True:
            if switch:
                self.show_field()
                try:
                    move = self.computer.take_a_shot(Player(self.player).get_move())
                except SeaBattleException as e:
                    print(e)
                else:
                    if move:
                        if self.computer.check_win():
                            print("\n" + " " * 10 + "Player win!")
                            self.show_field()
                            break
                    else:
                        switch = False
            else:
                try:
                    move = self.player.take_a_shot(AI(self.computer).get_move())
                except ShootedCellException:
                    pass
                else:
                    if move:
                        if self.player.check_win():
                            print("\n" + " " * 10 + "Computer win!")
                            self.show_field()
                            break
                    else:
                        switch = True

player = Playing_field(name = "player")
computer = Playing_field(name = "computer", hide = True)
game = Game(player = player, computer = computer)
game.play_game()