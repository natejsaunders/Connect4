from connect4 import *
from basic_bot import BasicBot

board = [
    [ state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY ],
    [ state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY ],
    [ state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY ],
    [ state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY ],
    [ state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY ],
    [ state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY, state.EMPTY ]
]

bot = BasicBot(state.YELLOW)

red_go = True
while check_for_win(board) == state.EMPTY:
    print(f"{'RED' if red_go else 'YELLOW'} to go")

    if red_go:
        col = int(input("::"))
        go(state.RED, board, col)
    else:
        col = bot.take_go(board)
        go(state.YELLOW, board, col)

    display_board(board)

    red_go = not red_go

winner = check_for_win(board)

print(f"{'RED' if winner==state.RED else 'YELLOW'} wins!")