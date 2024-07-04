"""
Link: https://techdevguide.withgoogle.com/resources/former-interview-question-flatten-iterators/
Problem:
    Given an iterator of iterators, implement an interleaving iterator that takes in an iterator of iterators, 
    and emits elements from the nested iterators in interleaved order. That is, 
    if we had the iterators i and j iterating over the elements [ia, ib, ic] and [ja, jb] respectively, 
    the order in which your interleaving iterator should emit the elements would be [ia, ja, ib, jb, ic].
    Your interleaving iterator should implement the Iterator interface, 
    take in the iterator of iterators in its constructor, and provide the next and hasNext methods. 
    Assume that there are no additional methods offered by the iterator.

    P.S. Original problem is in C++, but I will still do it in python, implementing __iter__ and __next__

Examples:
        [[1, 2, 3], [4, 5], [6, 7, 8, 9]] -> [1, 4, 6, 2, 5, 7, 3, 8, 9],
        [[1], [2, 3, 4], [5, 6]] -> [1, 2, 5, 3, 6, 4],
        [] -> [],
        [[1, 2], [], [3, 4]] -> [1, 3, 2, 4],
        [[], [], []] -> [],
        [[1], [2], [3]] -> [1, 2, 3],
        [[1, 2, 3], [4, 5, 6, 7], [8, 9]] -> [1, 4, 8, 2, 5, 9, 3, 6, 7],
        [[1, 2], [3], [4, 5, 6], [7, 8, 9, 10]] -> [1, 3, 4, 7, 2, 5, 8, 6, 9, 10],
        [[1, 2, 3, 4, 5]] -> [1, 2, 3, 4, 5]

Solution:
    1. Store amount of iterators that were passed to constructor
    2. Store 'current' - index of next iterator that suppose to call next() 
    3. Change 'current' index by adding 1 and taking remainder of division by amount of iterators
    4. Once iterator is exhausted, add its' index to done[] list

Complexity:
    1. O(n) time complexity for next() (since find_next_current might iterate through N elements)
    2. O(n) space complexity, since storing N iterators, and done indexes

"""

class IF:
    def __init__(self, iterators):
        self.iters = iterators
        self.amount = len(iterators)    # number of iterators
        self.current = 0 if self.amount > 0 else -1               # current iterator to print
        self.done = []                  # list of indexes of iterators that are finished

    def __iter__(self):
        return self
    
    def __find_next_current__(self):
        if (self.amount == 0):
            return -1
        
        # Find next current 
        nextCurrent = (self.current + 1) % self.amount
        while (self.done.count(nextCurrent) != 0):
            nextCurrent = (nextCurrent + 1) % self.amount
        self.current = nextCurrent
    
    def __next__(self):
        if (self.current == -1):
            raise StopIteration
        
        try:
            value = next(self.iters[self.current])
            self.__find_next_current__()
            return value
        except:
            self.done.append(self.current)
            if (len(self.done) == self.amount):
                raise StopIteration
            
            self.__find_next_current__()
            return self.__next__()

def test(tests):
    total = len(tests)
    right_answers = 0
    for test in tests:
        inArrays = test[0]
        input = [iter(arr) for arr in inArrays]
        expected = test[1]

        myIf = IF(input)
        myIfIter = iter(myIf)

        actual = []
        for x in myIfIter:
            actual.append(x)
        
        if actual != expected:
            print(f"Error on input {inArrays}, expected {expected}, but got {actual}")
        else:
            right_answers += 1
    print(f"Got {right_answers} out of {total}")
        
if __name__ == '__main__':
    tests = [
        ([[1, 2, 3], [4, 5], [6, 7, 8, 9]], [1, 4, 6, 2, 5, 7, 3, 8, 9]),
        ([[1], [2, 3, 4], [5, 6]], [1, 2, 5, 3, 6, 4]),
        ([], []),
        ([[1, 2], [], [3, 4]], [1, 3, 2, 4]),
        ([[], [], []], []),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[1, 2, 3], [4, 5, 6, 7], [8, 9]], [1, 4, 8, 2, 5, 9, 3, 6, 7]),
        ([[1, 2], [3], [4, 5, 6], [7, 8, 9, 10]], [1, 3, 4, 7, 2, 5, 8, 6, 9, 10]),
        ([[i] for i in range(10)], list(range(10))),
        ([[1, 2, 3, 4, 5]], [1, 2, 3, 4, 5])
    ]
    test(tests)