import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll
while True:
    players=input("Enter the number of players(1-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("must be between 2-4 players")
    else:
        print("Oh no! invalid numbers!")

print(players,"!,let's go!")

max_score = 50
player_scores = [0 for _ in range(players)]
while max(player_scores)<max_score:
    for play_idx in range(players):
        print("\nplayer",play_idx+1,"Turn has just started!\n")
        print("your total score is:",player_scores[play_idx],"\n")
        current_score=0

        while True:
            should_roll=input("would you like to roll(y)")
            if should_roll.lower()!="y":
                break
            value=roll()
            if value == 1:
                print("you roll the 1! turn down!")
                current_score=0
                break
            else:
                print("you roll a", value)
                current_score+=value
            print("your current score is:",value)

        player_scores[play_idx]+=current_score
        print("your total score is ", player_scores[play_idx])
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("player",winning_idx+1,"is the winner with a score of",max_score)