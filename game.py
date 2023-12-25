from random import randint


class TicTacToe:
    FREE_CELL = '🔲'  # свободная клетка
    HUMAN_X = '✖'  # крестик (игрок - человек)
    COMPUTER_O = '⚪'  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = [[Cell(self.FREE_CELL) for _ in range(3)] for _ in range(3)]

    def init(self):
        self.pole = [[Cell(self.FREE_CELL) for _ in range(3)] for _ in range(3)]
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    def show(self):
        for i in self.pole:
            for v in i:
                print(v.value, end=' ')
            print()
        print()

    def __bool__(self):
        self.check_win()
        return not any([self.__is_human_win, self.__is_computer_win, self.__is_draw])

    def check_win(self):
        self.__is_draw = self.check_pole(self.FREE_CELL)
        self.__is_human_win = self.check_pole(self.HUMAN_X)
        self.__is_computer_win = self.check_pole(self.COMPUTER_O)

    def check_pole(self, val):
        if val == self.FREE_CELL:
            for i in self.pole:
                for j in i:
                    if j.value == val:
                        return False
        else:
            for row in self.pole:
                if all(v.value == val for v in row):
                    return True

            for i in range(3):
                if all(self.pole[j][i].value == val for j in range(3)):
                    return True

            if all(self.pole[i][j].value == val for i in range(3) for j in range(3) if i == j):
                return True

            if all(self.pole[i][j].value == val for i in range(3) for j in range(3) if i + j == 2):
                return True

        return False

    @property
    def is_human_win(self):
        return self.__is_human_win

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @property
    def is_draw(self):
        return self.__is_draw

    def human_go(self):
        i, j = map(int, input('Ваш ход, укажите координаты: ').split())
        self[i, j] = self.HUMAN_X

    def computer_go(self):
        self[randint(0, 2), randint(0, 2)] = self.COMPUTER_O

    def check_index(self, indx):
        for i in indx:
            if not isinstance(i, int) or i not in range(3):
                raise IndexError('некорректно указанные индексы')
        return indx[0], indx[1]

    def __getitem__(self, indx):
        i, j = self.check_index(indx)
        return self.pole[i][j].value

    def __setitem__(self, indx, value):
        i, j = self.check_index(indx)

        if self.pole[i][j]:
            self.pole[i][j].value = value
            self.check_win()
        else:
            if value == self.HUMAN_X:
                self.human_go()
            else:
                self.computer_go()


class Cell:
    def __init__(self, value='🔲'):
        self.value = value

    def __bool__(self):
        return self.value == '🔲'


game = TicTacToe()
game.init()
step_game = 0

while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
