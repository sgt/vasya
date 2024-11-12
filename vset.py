class VSetList:
    def __init__(self):
        self.state = []

    def add(self, x: int) -> None:
        """
        O(n)
        optimal O(1)
        """
        if x not in self.state:
            self.state.append(x)

    def len(self) -> int:
        """
        O(1)
        """
        return len(self.state)

    def contains(self, x: int) -> bool:
        """
        O(n)
        optimal O(1)
        """
        return x in self.state


def test_vset_list():
    vs = VSetList()
    assert vs.len() == 0
    vs.add(1)
    assert vs.len() == 1
    assert vs.contains(1)
    assert not vs.contains(2)
    vs.add(2)
    assert vs.contains(2)
    assert vs.len() == 2
    vs.add(1)
    assert vs.len() == 2


def h(x:int) -> int:
    return x % 100


# h(1024) -> 24
# h(100) -> 0
# h(101) -> 1
# h(102) -> 2
# h(103) -> 3
# 0..99
