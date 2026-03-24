import random
import art
import game_data

score = 0

def character_profile():
    """returns a random name with description and country"""
    person = game_data.data[random.randint(0, len(game_data.data)-1)]
    return person['name'], person['follower_count'], person['description'], person['country']

def compare(character1, character2):
    name1, follower1, description1, country1 = character1
    name2, follower2, description2, country2 = character2
    if follower1 > follower2:
        print(f"{name1} has {follower1} followers")
        print(f"{name2} has {follower2} followers")
        print(f"{name1} has more followers")
        return character1
    else:
        print(f"{name1} has {follower1} followers")
        print(f"{name2} has {follower2} followers")
        print(f"{name2} has more followers")
        return character2


def am_i_correct(correct_answer, my_answer):
    if correct_answer == my_answer:
        print("You are correct!")
        global score
        score += 1
        print(f"your current score is {score}")
        return True
    else:
        print(f"You are wrong! Final score is {score}")
        return False


def playing(char1, char2):
    name1, follower1, description1, country1 = char1
    name2, follower2, description2, country2 = char2
    print(art.logo)
    print(f"Compare A: {name1}, a {description1}, from {country1}")
    print(art.vs)
    print(f"Against B: {name2}, a {description2}, from {country2}")
    #print(f"follower count A : {follower1} and follower count B : {follower2}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == 'A':
        return char1
    else:
        return char2


char1_tuple = character_profile()
char2_tuple = character_profile()
if char1_tuple == char2_tuple:
    char2_tuple = character_profile()
my_answer = playing(char1_tuple, char2_tuple)
correct = compare(char1_tuple, char2_tuple)
keep_playing = am_i_correct(correct, my_answer)

while keep_playing:
    char1_tuple = character_profile()
    char2_tuple = character_profile()
    my_answer = playing(char1_tuple, char2_tuple)
    correct = compare(char1_tuple, char2_tuple)
    keep_playing = am_i_correct(correct, my_answer)




