# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:
#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

#错误+redundant code_here
def check_sudoku(a_square_list):
    a = 0
    if len(a_square_list) == (a_square_list).index(a_square_list[-1]) + 1:
        if len(a_square_list) == 2:
            for i in a_square_list[a]:
                for e in a_square_list[a + 1]:
                    if i != e:
                        if a_square_list[a].count[i] == a_square_list[a + 1].count[e] == 1:
                            return True
        if len(a_square_list) == 3:
            for i in a_square_list[a]:
                for e in a_square_list[a + 1]:
                    for c in a_square_list[a + 2]:
                        if i != e and i != c:
                            if a_square_list[a].count[i] == a_square_list[a + 1].count[e] == a_square_list[a + 2].count[
                                c]:
                                return True
        if len(a_square_list) == 4:
            for i in a_square_list[a]:
                for e in a_square_list[a + 1]:
                    for c in a_square_list[a + 2]:
                        for d in a_square_list[a + 3]:
                            if i != e and i != c and i != d:
                                if a_square_list[a].count[i] == a_square_list[a + 1].count[e] == \
                                        a_square_list[a + 2].count[c] == a_square_list[a + 3].count[d]:
                                    return True


        else:
            return False
    return False

#网络版本#1


#网络版本#2
def check_sudoku(sudlist) :
    numbers = set(range(1, len(sudlist) + 1))
    if (any(set(row) != numbers for row in sudlist) or
        any(set(col) != numbers for col in zip(*sudlist))) :
        return False
    return True


#               [1.5, 1]]

def check_sudoku(grid):
    gridSize = len(grid)    # Extract size of grid
    digit = 1    # digit start with 1
    while digit <= gridSize:  # Go through each digit
        i = 0
        while i <= (gridSize - 1):
            rowCount = 0
            colCount = 0
            j = 0
            while j <= (gridSize - 1):   # for each entry in ith row/column
                # work through the ith row
                if grid[i][j] == digit:
                    rowCount = rowCount + 1
                # work through the ith column
                if grid[j][i] == digit:
                    colCount = colCount + 1
                j = j + 1
            if not (rowCount == 1 and colCount == 1):
                return False
            i = i + 1   # next row/column
        digit = digit + 1   # next digit
    return True  # Nothing was wrong. digit appears only once per row / column.


def check_sudoku(square):
    size = len(square)     #Check_the_#_of_sub_list_in_the list
    row = 0
    while row < size:
        num = 1
        while num <= size:
            if num not in square[row]:
                return False#Check_this since at lease 1 will be in the single sublist
            num = num + 1
        row = row + 1
    #get column values
    col = 0
    mycol = []#Note when you check a list the  procedure need to be carefully managed
    while col < size:#Create an empty list and enumerate all elements into this list then creaat a standard to check it
        row = 0
        while row < size:
            mycol.append(square[row][col])
            row = row + 1
        num = 1
        while num <= size:
            if num not in mycol:
                return False
            num = num + 1
        mycol = []
        col = col + 1
    return True





print
check_sudoku(incorrect)
# >>> False

print
check_sudoku(correct)
# >>> True

print
check_sudoku(incorrect2)
# >>> False

print
check_sudoku(incorrect3)
# >>> False

print
check_sudoku(incorrect4)
# >>> False
print
check_sudoku(incorrect5)
# >>> False
#######################################
#######################################
######################################
#Loop 的Indentation和构造出现问题
#注意你构造的check diagnol:
#这里需要的是两个LOOP去check
def check_sudoku(square):
    length = len(square)
    row = 0
    test_case = 1
    while row < length and test_case < length:
        if test_case not in square[row]:
               return False
        test_case = test_case+1
        row = row+1
    col = []
    list_number = 0
    test_number = 0
    while col < length:
        col.append(square[test_number][list_number])
        if test_number + 1 in col:
            return True
        test_number = test_number + 1
        list_number = list_number + 1

    else:
        return False
