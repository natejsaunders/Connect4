from enum import Enum

state = Enum('Board State', ['RED', 'YELLOW', 'EMPTY'])

def go(color: state, board: list, column: int) -> bool:
    if len(board)!=6: return False
    if len(board[0])!=7: return False
    if column<0 or column>6: return False

    for i in range(len(board)):
        if board[i][column] != state.EMPTY:
            if i==0: return False
            board[i-1][column] = color
            return True
        if i==5:
            board[i][column] = color
            return True

    return False

def display_board(board):
    for row in board:
        print("| ", end='')
        for space in row:
            if space == state.RED:
                print("R ", end='')
            elif space == state.YELLOW:
                print("Y ", end='')
            elif space == state.EMPTY:
                print("  ", end='')
            else:
                print("ERROR PRINTING BOARD")
        print("|")
    
    print("  0 1 2 3 4 5 6")

# Checks the whole board for a win (returns a color or empty if no winner)
# This function is very ineffeicient but it doesnt matter :)
def check_for_win(board) -> state:
    directions = [ [-1,-1],[-1,0],[-1,1], [0,-1],[0,1], [1,-1],[1,0],[1,1] ]

    for c in range(len(board)):
        for r in range(len(board[c])):
            space = board[c][r]
            if space == state.EMPTY: continue

            wins = False
            for dir in directions:
                for i in range(1,4):
                    try:
                        if board[c + dir[0]*i][r + dir[1]*i] != space:
                            break
                    except IndexError:
                        break

                    if i == 3: wins = True

            if wins: return space

    return state.EMPTY
