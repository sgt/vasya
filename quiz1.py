def swap(nums: list[int], i1: int, i2: int) -> None:
    """Меняет местами два элемента внутри списка."""
    temp = nums[i1]
    nums[i1] = nums[i2]
    nums[i2] = temp

def bin_find(nums : list[int], num : int) -> int:
    """
    Для отсортированного списка, возвращает индекс элемента, равного value. Если элемент не найден, возвращает -1.

    Сложность: O(log n)
    """
    left = 0
    right = len(nums) - 1
    while left<=right:
        mid = (left + right) // 2
        if num > nums[mid]:
            left = mid + 1
        elif num < nums[mid]:
            right = mid - 1
        elif num == nums[mid]:
            return mid
    return -1

def sort(nums: list[int]) -> None:
    pass


def find(nums: list[int], value: int) -> int:
    """
    Возвращает индекс элемента, равного value. Если элемент не найден, возвращает -1.

    Сложность: O(n)
    """
    for i, n in enumerate(nums):
        if n == value:
            return i

    return -1


def test_find():
    find = bin_find
    assert find([20, 1, 8, 153], 8) == 2
    assert find([20, 1, 8, 153], 153) == 3
    assert find([20, 1, 8, 153], 18) == -1
    assert find([], 18) == -1


def two_sum_linear(nums: list[int], target: int) -> list[int]:
    """
    список чисел -> получить число по индексу
    словарь (ключ: ... значение:...)

    nums[1000]

    nums (A: 2394801948FDFADG)
    len(nums) = 4

    A[i] = A+i
    A[0] = A+0
    A[1] = A+1
    A[2] = A+2
c
    операция A[i] имеет сложность O(1)



СЛОВАРЬ
    d[k]

    """



def two_sum(nums: list[int], target: int) -> list[int]:
    """
    leetcode #1

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    О(1) -- константная сложность
    O(n) -- линейная сложность
    O(n^2) -- квадратная
    O(log2 n)

    log2 1 = 0
    log2 2 = 1
    log2 1024 = 10
    log2 2048 = 11

    O(n * log n)
    """
    for i1 in range(len(nums)):
        for i2 in range(i1 + 1, len(nums)):
            if nums[i1] + nums[i2] == target:
                return [i1, i2]


def test_two_sum():
    two_sum = two_sum_linear
    assert frozenset(two_sum([2, 7, 11, 15], 9)) == frozenset([0, 1])
    assert frozenset(two_sum([3, 2, 4], 6)) == frozenset([1, 2])
    assert frozenset(two_sum([3, 3], 6)) == frozenset([0, 1])


def is_palindrome(x: int) -> bool:
    """
    leetcode #9

    Given an integer x, return true if x is a palindrome, and false otherwise.

    задача со звездочкой: решить чисто математически, без превращения числа в строку
    """
    a = 0
    c = len(str(x))
    for num in range(c):
        num += 1
        b = x % 10
        a += b * (10 ** (c - num))
        x = x // 10

    return a


def is_two(n: int) -> bool:
    return n == 2


def is_pal(x: int) -> bool:
    return str(x) == reversed(str(x))


def test_is_palindrome():
    assert is_palindrome(121)
    assert not is_palindrome(-121)
    assert not is_palindrome(10)


def longest_common_prefix(strs: list[str]) -> str:
    """
    leetcode #14

    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    """
    str = ""
    equ = False
    for a in strs:
        if len(str) < len(a):
            str = a
            equ = False
        elif len(str) == len(a):
            equ = True
    if not equ:
        return str
    else:
        return ""


def test_longest_common_prefix():
    assert "fl" == longest_common_prefix(["flower", "flow", "flight"])
    assert "" == longest_common_prefix(["dog", "racecar", "car"])
    assert "" == longest_common_prefix([""])


def length_of_longest_substring(s: str) -> int:
    """
    leetcode #3

    Given a string s, find the length of the longest substring without repeating characters.
    """
    raise NotImplementedError("Not implemented yet")


def test_length_of_longest_substring():
    assert length_of_longest_substring("abcabcbb") == 3  # "abc"
    assert length_of_longest_substring("bbbbb") == 1  # "b"
    assert length_of_longest_substring("pwwkew") == 3  # "wke"
