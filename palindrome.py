from collections import deque


def is_palindrome(word) -> str:
    word = word.lower().strip()
    d = deque(word)
    while len(d) != 0 and len(d) != 1:
        if d.pop() != d.popleft():
            print("False")
            return
    print("True")
    return

is_palindrome("kayak")
