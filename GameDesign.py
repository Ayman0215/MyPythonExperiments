"""
# English :

# Create a row with 20 elements.
# Randomly assign each element with "coin" or "no coin".

# Ask the user for the names of the two players.
# Randomly assign the position of each player. Store that in Payer1Pos and Player2Pos
# Assign each player 5 turns and playerScore.  ===> Initiaize totalTurns to 5 and Player1Score to 0 and Player2Score to 0.
# For each turn: # Loop until totalTurns is 0
    - Ask the user input: ==> This is not correct
        ===> Who validates the input??
        - [If the user is on the edge of the row]: ==> If Payer1Pos == 19
            - [Restrict them from moving in the direction the edge is facing]. ==> If user_input is 1, ....
            - Tell them to move in the opposite direction. 
        - else if player1Pos == 0
            -- blah bla
        - [If not]:
            - Ask them to go either right or left.
    - Input which direction they want to in:  ==> Ask for Player1's input
        - Validate Input.. If input is wrong, ask user for input again !! user_input has the user input.
        - Player1Pos += user_input
        = Player1Score + coinrow[Player1Pos]
        - coinrow[Player1Pos] = 0
        - Display: coin row, Player Scores, Player positions, turns remaining for each player

    - Ask for Player2's input
        - Validate Input.. If input is wrong, ask user for input again !! user_input has the user input.
        - Player2Pos += user_input
        = Player1Score + coinrow[Player2Pos]
        - coinrow[Player2Pos] = 0
        - Display: coin row, Player Scores, Player positions, turns remaining for each player

        - [If they can]:
            - Display them moving to the next slot immediately next to them in that direction.
            - [If there is a coin there]:
                - [Collect the coin]  
                - Display the coin added to the Player1Score
            - [If there is no coin]:
                - [Continue]
        - [If they can't]:
            - Display that they cannot move in that direction.
            - Tell them to move in the opposite direction.
    - After the player's turn ends:
        - [Subtract one of their turns]:
            - [If their number of turns is less than 0 and the other player's is also 0]:
                - End game.
            - [If their number of turns is less than 0]:
                - Switch the turn to the other player.
            - [Else]:
                - Switch the turn to the other player.
    - Reduce totalTurns by 1.

# After the tunrs are completre:

    - Count the number of coins each player has: ==> not neederd
        - [If one player has more coins than the other]: ==> If Player1Score > Player2Score
            - Display that they won and the other player lost.
        - [If they tie]:
            - Display tie.
# Play game again and restart.

"""

#------------------------------------------------------------#
import random

def setup_game():
    coin_row = []
    for i in range(10):
        coin_row.append(random.choice([0, 1]))

    p1_pos = random.randint(0, 9)
    p2_pos = random.randint(0, 9)
    while p2_pos == p1_pos:
        p2_pos = random.randint(0, 9)
    return coin_row, p1_pos, p2_pos, 0, 0, 5
#------------------------------------------------------------#
def show_status(turns, coin_row, p1_pos, p2_pos, p1_score, p2_score):
    print("Turn:", 6 - turns)
    print("Coins:", coin_row)
    print(f"Player 1 at {p1_pos}, Score={p1_score}")
    print(f"Player 2 at {p2_pos}, Score={p2_score}")
    print()

def move_player(player_name, pos, other_pos, coin_row, score):
    move = input(f"{player_name} move (L/R): ").lower()
    if move == "l" and pos > 0:
        pos -= 1
    elif move == "r" and pos < len(coin_row) - 1:
        pos += 1
    else:
        print("Invalid move. You can’t go that way.")

    if pos == other_pos:
        if player_name == "Player 2":
            other_player = "Player 1"
        else:
            other_player = "Player 2"
        print(f"Same spot as {other_player }! No move made.")
    elif coin_row[pos] == 1:
        print(f"{player_name} found a coin!")
        score += 1
        coin_row[pos] = 0
    return pos, score
#------------------------------------------------------------#
def play_game():
    coin_row, p1_pos, p2_pos, p1_score, p2_score, turns = setup_game()

    print("Coin Slot Game!")
    print("Each player has 5 turns.")
    print("Move L for left or R for right.")
    print()

    while turns > 0:
        show_status(turns, coin_row, p1_pos, p2_pos, p1_score, p2_score)
        p1_pos, p1_score = move_player("Player 1", p1_pos, p2_pos, coin_row, p1_score)
        p2_pos, p2_score = move_player("Player 2", p2_pos, p1_pos, coin_row, p2_score)

        turns -= 1
        if sum(coin_row) == 0:
            print("All coins collected!")
            break

    print_results(p1_score, p2_score)

def print_results(p1_score, p2_score):
    print("Game Over!")
    print(f"Player 1 Score: {p1_score}")
    print(f"Player 2 Score: {p2_score}")

    if p1_score > p2_score:
        print("Player 1 wins!")
    elif p2_score > p1_score:
        print("Player 2 wins!")
    else:
        print("It’s a tie!")

#------------------------------------------------------------#
play_game()
#------------------------------------------------------------#