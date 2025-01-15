class TicTacToe:

    def __init__(self):
        self.board =[["1","2","3"],
                     ["4","5","6"],
                     ["7","8","9"]]
        self.who_play=1
        self.player='X'
        self.what_print=""
        self.playing= True

    def _check_is_triplet_winning(self,player:str)->bool:
        if ((self.board[0][0]==player and self.board[0][1]==player and self.board[0][2]==player)
                or (self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player)
                or (self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player)
                or (self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player)
                or (self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player)
                or (self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player)
                or (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player)
                or (self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player)) :
            return True
        return False
    def is_over(self) -> bool:
        return  not  self.playing

    def state(self) -> str:
        # 'X_WON', 'O_WON', 'TIE', 'ERROR', 'XS_TURN', 'OS_TURN'
        if self._check_is_triplet_winning('X'):
            self.what_print="X_WON"
            self.playing=not self.playing
        elif self._check_is_triplet_winning('O'):
            self.what_print="O_WON"
            self.playing=not self.playing


    def current_player(self) -> str:
        # 'X' or 'O'
        self.who_play+=1
        if self.who_play%2==0:
            self.player='X'
            return 'X'
        else:
            self.player="O"
            return 'O'

    def make_turn(self, pos:int) -> None:
        raise NotImplementedError

    def print(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[3])

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
