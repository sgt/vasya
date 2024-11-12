class TicTacToe:

    def __init__(self):
        self.board = ........

    def is_over(self) -> bool:
        raise NotImplementedError

    def state(self) -> str:
        # 'X_WON', 'O_WON', 'TIE', 'ERROR'
        raise NotImplementedError

    def current_player(self) -> str:
        # 'X' or 'O'
        raise NotImplementedError

    def make_turn(self, x: int, y: int) -> None:
        pass

    def print(self):
        print("..O")
        print(".X.")
        print("...")

if __name__ == '__main__':
    game = TicTacToe()

    while not game.is_over():
        game.print()
        # спрашиваем ход текущего игрока
        print("Ход игрока " + game.current_player())
        x, y = input()
        game.make_turn(x, y)

    match game.state():
        case 'X_WON':
            print("победил крестик")
        case 'O_WON':
            print("победил нолик")
        case 'TIE':
            print("ничья")
        case 'ERROR':
            print("невозможное состояние игры")
        case _:
            print("непонятный результат")
