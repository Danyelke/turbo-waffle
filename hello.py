import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("read that again")
    else:
        print("nummmber please")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    
    for player_index in range(players):
        print("Player", player_index + 1, "turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Roll? (y) ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("1 rolled, F")
                current_score = 0
                break
            else:
                current_score += value
                print("Rolled a: ", value)

            print("Your score is: ", current_score)

        player_scores[player_index] += current_score
        print("Your total score is:", player_scores[player_index], "\n")

max_score = max(player_scores)
winner = player_scores.index(max_score)
print("Player", winner + 1, "won, score:", max_score)