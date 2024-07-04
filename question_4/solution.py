"""
Link: https://techdevguide.withgoogle.com/resources/former-interview-question-find-longest-word/
Problem:
    Given a string S and a set of words D, find the longest word in D that is a subsequence of S.
    Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, 
    without reordering the remaining characters.
Examples:
    S = "abppplee", D = ["able", "ale", "apple", "bale", "kangaroo"] -> "apple"

Solution:
    1. Find if string is a substring by simply going through given string once
    2. Sort D by length
    3. Go through D
    4. First word in sorted D that is substring of S - the answer

Complexity:
    1. O(n) for finding sub, and O(n) for going through D. O(n^2) for this part. Plus O(nlogn) sorting.
        So O(n^2 + nlogn)
    2. O(1) space complexity
"""

# Returns true if word is sub of string as it is described in problem
def is_sub(string: str, word: str):
    strIndex = 0
    wordIndex = 0

    while (wordIndex < len(word) and strIndex < len(string)):
        if string[strIndex] == word[wordIndex]:
            wordIndex += 1
        strIndex += 1

    return wordIndex == len(word)

def find_longest(s: str, d: list[str]):
    d = sorted(d, key=len, reverse=True)
    for word in d:
        if (is_sub(s, word)):
            return word
        
    return ""

from colorama import Fore, Back, Style, init
init()
def test(tests):
    total = len(tests)
    right_answer = 0

    for (input, expected) in tests:
        actual = find_longest(input[0], input[1])

        if (actual != expected):
            print(Back.RED, f"Error: On input {input} expected {expected}, but got {actual}")
        else:
            right_answer += 1

    if right_answer == total:
        print(Fore.GREEN, "All passed.")
    else:
        print(Fore.RED, f"Passed {right_answer} out of {total}")

if __name__ == '__main__':
    tests = [
        (("abppplee", ["able", "ale", "apple", "bale", "kangaroo"]), "apple"),
        (("abcde", ["a", "bb", "acd", "ace"]), "acd"),
        (("abc", ["def", "ghi"]), ""),
        (("abppplee", ["ale", "bpple", "apple"]), "bpple"),
        (("abcde", ["a", "b", "c"]), "a"),
        (("", ["a", "b", "c"]), ""),
        (("abcde", []), ""),
        (("abpcplea", ["ale", "apple", "monkey", "plea"]), "apple"),
        (("abcde", ["abcdef", "abcde", "abcd"]), "abcde"),
        (("abpcplea", ["plea", "aepl"]), "plea"),
        (("abppplee", ["apple", "apple"]), "apple"),
        (("abppplee", ["APPLE", "apple"]), "apple"),
        (("abcdefgh", ["abc", "bcd", "cde", "def"]), "abc"),
        (("abcdefgh", ["a", "b", "c", "defgh"]), "defgh")
    ]

    test(tests)
