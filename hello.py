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
    should_roll = input("Roll? (y) ")
    if should_roll.lower() != "y":
        break

    value = roll()
    if value == 1:
        print("1 rolled, F")
    else:
        current_score += value
        print("Rolled a: ", value)

    print("Your score is: ", current_score)