class TicTacToe:

    def __init__(self):
        self.board =['___','___','___']
        self.who_play=1

    def _check_is_triplet_winning(self, positions:list[int], player:str)->bool:
        pass

    def is_over(self) -> bool:
        raise NotImplementedError

    def state(self) -> str:
        # 'X_WON', 'O_WON', 'TIE', 'ERROR', 'XS_TURN', 'OS_TURN'
        raise NotImplementedError

    def current_player(self) -> str:
        # 'X' or 'O'
        self.who_play+=1
        if self.who_play%2==0:
            return 'X'
        else:
            return 'O'
        raise NotImplementedError

    def make_turn(self, pos:int) -> None:
        raise NotImplementedError

    def print(self):
        print(self.board[0])
        print(self.board[0])
        print(self.board[0])

def test_game():
    game = TicTacToe()
    assert not game.is_over()
    assert game.current_player() == 'X'
    assert game.state() == 'XS_TURN'
    game.make_turn(5)
    assert game.current_player() == 'O'
    assert game.state() == 'OS_TURN'
    game.make_turn(1)
    game.make_turn(2)
    game.make_turn(3)
    game.make_turn(8)
    assert game.state() == 'X_WON'

def test_tie():
    pass

# X 2 3
# 4 5 O
# 7 8 9
