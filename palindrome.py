'''
Homework 7 Problem 2: Palindrome
Carter King
Dr. Sanders
CS 355 Advanced Algorithms
3 December 2018
Python 3
'''

'''
Complexity:
    The complexity of the Palindrome algorithm would be O(n^2) as I used two for loops to input into the array, and the function
    to calculate the string contains two whiles that cannot physically surpass n^2 iterations.
'''

import sys

'''
Function: palindrome(sequence, table, n)
 This function uses dynamic programming to find the max possible length palindrome.
 It takes a 2-D array and fills in the cells based on the max-length palindrome possible at the particular substring.
 The function returns the the top right cell which represents the maximal length palindrome for the sequence of characters
 parameters: sequence: The array of characters
             table: 2D array to utilize memoization
             n: size of the sequence of characters
 returns: table[0][n-1] - the top-right cell of the table, containing the max possible length
'''


def palindrome(sequence, table, n):
    

    for x in range(n):  # need to go through the amount of character times
        diag = 0  # To keep track of positioning as iterate diagonally
        for y in range(x + 1, n):  # Diagonal shrinks every time, so isn't alway 0 to n
            if sequence[diag] == sequence[y]:  # if equal, it's the diagonal plus 2 for the match
                table[diag][y] = table[diag + 1][y - 1] + 2
            else:
                table[diag][y] = max(table[diag + 1][y],
                                     table[diag][y - 1])  # if unequal take max of two smaller substrings
            diag += 1

    return table[0][n - 1]  # top-right corner gives the maximum length palindrome substring


'''
Function: calcString(table, n, maxSize, sequence)
 This function retraces a filled-in 2-D array, and retraces it to find the characters that make up the max length palindrome.
 parameters: table: 2D array to utilize memoization
             n: size of the sequence of characters
             maxSize: max size of the palindrome discovered from def palindrome()
             sequence: an array of the characters of the string
 returns:    maxSub: an array of the actual max-length palindrom
'''


def calcString(table, n, maxSize, sequence):
    x = 0
    a = 0
    y = n - 1
    b = maxSize - 1

    maxSub = []  # array to hold the characters in max palindrome
    for i in range(maxSize):  # initialize array just to all 0s
        maxSub.append(0)

    while (table[x][y] != 1 and table[x][y] != 0):  # a 1 or a 0 means there is one left to place or 0 left to add
        while table[x][y] == table[x + 1][y]:  # from curr pos, go down as far as possible while equal
            x += 1
        while table[x][y] == table[x][y - 1]:  # from where left-off, go left while still equal
            y -= 1
        maxSub[a] = sequence[x]  # once two whiles over, add character from the row into opposite sides of array
        maxSub[b] = sequence[x]
        x += 1  # move to the diagonal to contiue
        y -= 1
        a += 1  # move toward middle of array
        b -= 1
    if table[x][y] == 1:  # if at a 1, add char once to middle of string
        maxSub[a] = sequence[x]
    return maxSub


'''
Function: parseFile(filename)
 This function takes a .txt file of a sequence of characters and creates and array of these characters
 parameters: filename - a string of the name of the file
 returns: sequence: the array of the characters
          n: the length of the array/num. characters in the array
'''


def parseFile(filename):
    infile = open(filename, 'r')  # read the file and add elements to list
    for line in infile:
        sequence = list(line)
        n = len(sequence)
    return sequence, n  # return array of characters and the length of the array


def main():
    # Show them the default len is 1 unless they put values on the command line
    print(len(sys.argv))
    if len(sys.argv) == 2:
        fileName = sys.argv[1]
    else:
        fileName = input("Which input file would you like to use? ")
        sequence, n = parseFile(fileName)
        table = [[0 for x in range(n)] for i in range(n)]  # initializa 2-D array with 0s
        for b in range(n):
            table[b][b] = 1  # if compared one char substring to itself will return 1
        maxSize = palindrome(sequence, table, n)  # max length of a palindrome
        palString = calcString(table, n, maxSize, sequence)  # string of chars in max length palindrome
        print(maxSize)
        for x in table:
            print(x)
        palString = ''.join(palString)
        print("The longest palindrome substring is:", palString)

main()
