cache_for_find = {}


def find_cached(nums: list[int], value: int) -> int:
    if value in cache_for_find:
        return cache_for_find[value]
    i = find(nums, value)
    cache_for_find[value] = i
    return i


def find(nums: list[int], value: int) -> int:
    """
    Возвращает индекс элемента, равного value. Если элемент не найден, возвращает -1.
    """
    for i, n in enumerate(nums):
        if n == value:
            return i

    return -1


def test_find():
    assert find([20, 1, 8, 153], 8) == 2
    assert find([20, 1, 8, 153], 18) == -1
    assert find([], 18) == -1


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
