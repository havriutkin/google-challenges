"""
Problem:
Imagine an island that is in the shape of a bar graph. 
When it rains, certain areas of the island fill up with rainwater to form lakes. 
Any excess rainwater the island cannot hold in lakes will run off the island to the west or east and drain into the ocean.

Given an array of positive integers representing 2-D bar heights, 
design an algorithm (or write a function) that can compute the total volume (capacity) of water 
that could be held in all lakes on such an island given an array of the heights of the bars. 
Assume an elevation map where the width of each bar is 1.

Example: 
Given [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2], return 15 (3 bodies of water with volumes of 1,7,7 yields total volume of 15)
"""
from utils import utils

def getVolume(heights: list[int]) -> int:
    if (len(heights) <= 2):
        return 0

    leftMaxHeights = [-1] * len(heights)
    rightMaxHeights = [-1] * len(heights)
    volumes = [0] * len(heights)

    i = 1
    j = len(heights) - 2
    while(i < len(heights)):
        leftMaxHeights[i] = heights[i - 1] if heights[i - 1] > leftMaxHeights[i - 1] else leftMaxHeights[i - 1]
        rightMaxHeights[j] = heights[j + 1] if heights[j + 1] > rightMaxHeights[j + 1] else rightMaxHeights[j + 1]
        i += 1
        j -= 1
    
    for i in range(len(heights)):
        minSideLevel = leftMaxHeights[i] if leftMaxHeights[i] < rightMaxHeights[i] else rightMaxHeights[i]
        if minSideLevel > heights[i]:
            volumes[i] = minSideLevel - heights[i]

    result = 0
    for volume in volumes:
        result += volume
    
    return result
        
if __name__ == '__main__':
    tests = [
        ([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2], 15),
        ([5, 1, 5], 4),
        ([5, 1, 6], 4),
        ([5, 1, 2, 5], 7),
        ([], 0),
        ([4], 0),
        ([4, 4, 4, 4], 0),
        ([4, 4, 4, 5], 0),
        ([5, 4, 4, 5], 2),
        ([1, 2, 3, 4], 0),
        ([4, 3, 2, 1], 0),
        ([4, 3, 2, 1, 2, 3, 4], 9)
    ]

    utils.test(getVolume, tests)
