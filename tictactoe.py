class TicTacToe:

    def __init__(self):
        self.board =['___','___','___']
        self.who_play=1

    def is_over(self) -> bool:
        raise NotImplementedError

    def state(self) -> str:
        # 'X_WON', 'O_WON', 'TIE', 'ERROR'
        raise NotImplementedError

    def current_player(self) -> str:
        # 'X' or 'O'
        self.who_play+=1
        if self.who_play%2==0:
            return 'X'
        else:
            return 'O'
        raise NotImplementedError

    def make_turn(self, x: int, y: int ,who: str) -> None:
        self.board[y][x]=who

    def print(self):
        print(self.board[0])
        print(self.board[0])
        print(self.board[0])

if __name__ == '__main__':
    game = TicTacToe()

    while not game.is_over():
        game.print()
        # спрашиваем ход текущего игрока
        a=game.current_player()
        print("Ход игрока " + a)
        x, y = input()
        game.make_turn(x, y,a)

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
