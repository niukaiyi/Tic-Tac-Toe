# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def game(arr):
    player = 'X'
    count = 0
    while check(arr):
        if count == 9:
            break
        row = None
        column = None
        while (row == None and column == None) or (row < 0 or row > 2 or column > 2 or column < 0) or arr[row][column] != 0:
            point = input(player + ' turn:')
            corArr = point.split(',')
            row = int(corArr[0]) - 1
            column = int(corArr[1]) - 1
            if row < 0 or row > 2 or column > 2 or column < 0:
                print('out of range, pls re-input')
            else:
                if arr[row][column] != 0:
                    print('have drawn on this space, pls re-input')

        if player == 'X':
            arr[row][column] = 1
            player = 'O'
        else:
            arr[row][column] = -1
            player = 'X'

        count += 1

    return arr

def check(arr):

    diag1 = 0
    diag2 = 0
    for i in range(3):
        columnRes = 0
        rowRes = 0
        for j in range(3):
            columnRes += arr[i][j]
            rowRes += arr[j][i]
        if columnRes == 3 or columnRes == -3 or rowRes == 3 or rowRes == -3:
            return False
        diag1 += arr[i][i]
        diag2 += arr[i][2-i]
    if diag1 == 3 or diag1 == -3 or diag2 == 3 or diag2 == -3:
        return False
    return True

arr = [[0 for _ in range(3)] for _ in range(3)]
arr = game(arr)
print(arr)


# X:1,1 O:1,8 O:1,2 X:2,2 O:1,3 X:3,3
# X:1,1 O:2,2 X:1,2 O:2,3 X:1,3
# X:3,1 O:3,2 X:2,2 O:3,3 X:1,3
# X:1,1 X:1,1
# X:1,1 O:1,2 X:2,2 O:3,3 X:1,3 O:3,1 X:3,2 O:2,1 X:2,3
