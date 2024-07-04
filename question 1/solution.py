"""
Problem:
    In this exercise, you're going to decompress a compressed string.
    Your input is a compressed string of the format number[string] 
        and the decompressed output form should be the string written number times.
    Other rules
        - Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa
        - One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab
        - Characters allowed as input include digits, small English letters and brackets [ ].
        - Digits are only to represent amount of repetitions.
        - Letters are just letters.
        - Brackets are only part of syntax of writing repeated substring.
        - Input is always valid, so no need to check its validity.

Examples:
3[ab] -> ababab
[ab] -> ab
[] -> 
a[]b -> ab
ab -> ab
2[a]3[b] -> aabbb

Solution:
    1. Use stack
    2. If it is a number, collect all digits and put it on stack
    3. If it is a regular character just put it on stack
    4. If closing bracket is encountered, assemble expression from word from a stack by extracting elements until open bracket
     4.1. If there were more then one word inside brackets - reverse the expression
     4.2. Push expression on the stack

Complexity:
    1. O(n^2) - worst case time complexity. It occurs when finding a closing bracket forces to go back through all stack
    2. O(n) - space complexity, using stack
"""

def decompress(input:str) -> str:
    stack = []
    index = 0

    # Go through input
    while (index < len(input)):
        char = input[index]

        if (char.isnumeric()):
            # If it is a number, collect all digits and push it to stack
            index += 1
            while (input[index] != '['):
                char += input[index]
                index += 1
            stack.append(char)
            continue
        
        if (char != ']'):
            # If it is a letter and not closing bracket, just add it to stack
            stack.append(char)
            index += 1
            continue
        
        # If it is a closing bracket, start going backwards in stack and assemble an expression inside brackets
        expression = ""
        num_of_words = 0
        while(stack[-1] != '['):
            num_of_words += 1
            expression += stack.pop()
        stack.pop()

        # Get the number of repeats for found expression (number before opening bracket)
        repeat = 1
        if (len(stack) != 0 and stack[-1].isnumeric()):
            repeat = int(stack.pop())
        word = repeat * expression
        
        # If there were more than 1 word inside brackets - reverse the assembled word
        if num_of_words > 1:
            word = word[::-1]

        stack.append(word)  # Put word on stack
        index += 1

    return "".join(stack)
    
def test():
    tests = [
        ("3[ab]", "ababab"),
        ("[ab]", "ab"),
        ("[]", ""),
        ("a[]b", "ab"),
        ("2[a]3[b]", "aabbb"),
        ("2[aaabaaab]", "aaabaaabaaabaaab"),
        ("2[2[3[a]b]]", "aaabaaabaaabaaab"),
    ]
    total = len(tests)

    right_answers = 0
    for test in tests:
        result = decompress(test[0])
        if (result != test[1]):
            print(f"Error on input {test[0]}. Expected: {test[1]}. Result: {result}")
        else:
            right_answers += 1
    print(f"Got {right_answers} out of {total}")

if __name__ == "__main__":
    test()
