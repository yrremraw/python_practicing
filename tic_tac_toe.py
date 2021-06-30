from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    for i in range(1, len(board)-1, 3):
        print(f' {board[i]} | {board[i+1]} | {board[i+2]}')

def player_input(first_player):
    allowed_mask = ['X','O']
    # [to do] find smarter way to assign player 2
    second_player = 0
    if first_player == 1:
        second_player = 2
    elif first_player == 2:
        second_player = 1
    while players[first_player] not in allowed_mask:
        players[first_player] = input(f'Player {first_player}: Do you want to be X or O? ').upper()
        if players[first_player] not in allowed_mask:
            print("Please input only allowed mask (X,O)!")
        # first player choosed their mask, assign the mask to another player
        else:
            if players[first_player] == allowed_mask[0]:
                players[second_player] = allowed_mask[1]
            else:
                players[second_player] = allowed_mask[0]
            print(f'[As Player 1 selected {players[1]}, Player 2 will use {players[2]}]')
    print(f'Player {first_player} will go first.')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    count = 0
    win_pattern = [
        [1,2,3],[4,5,6],[7,8,9], # horizontal
        [1,4,7],[2,5,8],[3,6,9], # vertical
        [1,5,9],[3,5,7]] # diagonal
    for i in win_pattern:
        for j in i:
            # print('B :',j,board[j],mark,i,count)
            if board[j] == mark:
                count += 1
            # print('A :',j,board[j],mark,i,count)
        if count == 3:
            return True
        else:
            count = 0
    return False

def choose_first():
    return(random.randint(1,2))

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    
    for i in board:
        if i == ' ':
            return False
    return True

def player_choice(board):
    current_input = -1
    while current_input not in range(1, len(board)) or not space_check(board,current_input):
        current_input = int(input(f'Pick a cell to put the mask (1-{len(board)-1}): '))
        if current_input not in range(1, len(board)):
            print(f'{current_input} is out of the board, board size is (1-{len(board)-1})')
        elif not space_check(board,current_input):
            print(f'{current_input} was already choosen, please choose another cell')
        else:
            return (current_input)

def replay():
    replay_ans = 'None'
    allowed_replay_ans = ['Yes', 'No']
    while replay_ans not in allowed_replay_ans:
        replay_ans = input(f'Would you like to replay? (Yes/No): ')
        if replay_ans.capitalize() in allowed_replay_ans:
            if replay_ans.capitalize() == 'Yes':
                return True
            else:
                return False
        else:
            print(f'Please response Yes or No only, your response was {replay_ans}')

print('Welcome to Tic Tac Toe!')
play = True

while play:
    players = {1:'', 2:''}
    board = ['#', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(board)
    got_winner = False
    current_player = choose_first()
    player_input(current_player)
    while not got_winner:
        if full_board_check(board):
            print('Board is full!')
            break
        print(f"Player {current_player}'s turn (mask = {players[current_player]})")
        position = player_choice(board)
        place_marker(board, players[current_player], position)
        display_board(board)
        got_winner = win_check(board, players[current_player])
        if got_winner:
            print(f'Congrats! Player {current_player} is the winner!')
        else:
            if current_player == 1:
                current_player = 2
            elif current_player == 2:
                current_player = 1
    play = replay()
