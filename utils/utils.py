from colorama import Fore, Back, Style, init

init()

def test(func, tests):
    total = len(tests)
    right_answer = 0

    for (input, expected) in tests:
        actual = func(input)

        if (actual != expected):
            print(Back.RED, f"Error: On input {input} expected {expected}, but got {actual}")
        else:
            right_answer += 1

    if right_answer == total:
        print(Fore.GREEN, "All passed.")
    else:
        print(Fore.RED, f"Passed {right_answer} out of {total}")