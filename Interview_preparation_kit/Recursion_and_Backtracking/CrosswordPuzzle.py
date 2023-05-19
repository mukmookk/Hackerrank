#!/bin/python3

import math
import os
import random
import re
import sys

def crosswordPuzzle(crossword, words):
    result = []
    words = words.split(";")
    
    def canPlaceHorizontally(grid, word, row, col):
        if col + len(word) > 10:
            return False
        
        for i in range(len(word)):
            if grid[row][col + i] not in ('-', word[i]):
                return False
        return True
    
    def canPlaceVertically(grid, word, row, col):
        if row + len(word) > 10:
            return False
        
        for i in range(len(word)):
            if grid[row + i][col] not in ('-', word[i]):
                return False
        return True 
    
    def backtrack(grid, words, wordIndex):
        if wordIndex == len(words):
            print(grid)
            return grid
        
        for i in range(10):
            for j in range(10):
                if grid[i][j] == '-' or grid[i][j] == words[wordIndex][0]:
                    if canPlaceHorizontally(grid, words[wordIndex], i, j):
                        newGrid = [list(row) for row in grid]
                        row, col = i, j
                        for k in range(len(words[wordIndex])):
                            newGrid[row][col] = words[wordIndex][k]
                            col = col + 1
                        res = backtrack(newGrid, words, wordIndex + 1)
                        if res:
                            return res
                    
                    if canPlaceVertically(grid, words[wordIndex], i, j):
                        newGrid = [list(row) for row in grid]
                        row, col = i, j
                        for k in range(len(words[wordIndex])):
                            newGrid[row][col] = words[wordIndex][k]
                            row = row + 1
                        res = backtrack(newGrid, words, wordIndex + 1)
                        if res:
                            return res
        
        return []
    result = backtrack(crossword, words, 0)
    return [''.join(row) for row in result]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
