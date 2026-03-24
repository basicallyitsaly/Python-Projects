# Insert art
import art
import random

my_cards = []
computer_cards = []
def eleven_exists(the_list):
    n = 11
    if sum(the_list) > 21:
        if n in the_list:
            where_n = my_cards.index(n)
            the_list[where_n] = 1
            print(the_list)
        else:
            print(the_list)
    else:
        print(the_list)

def draw(the_list):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    draw_random = random.choice(cards)
    the_list.append(draw_random)

    return the_list

def compare_cards(list1, list2):
    eleven_exists(my_cards)
    eleven_exists(computer_cards)

    distance_from_21 = 0
    my_sum = sum(my_cards)
    computer_sum = sum(computer_cards)
    #print(my_sum)
    #print(computer_sum)

    if my_sum > 21:
        print("You lose!")
    if my_sum <= 21:
        my_sum = my_sum - 21
        computer_sum = computer_sum - 21
        #print(my_sum)
        #print(computer_sum)
        if my_sum > computer_sum:
            print("You win!")
        elif my_sum < computer_sum:
            print("You lose!")
        elif my_sum == computer_sum:
            print("its a draw")


run_game = True
while run_game :
    will_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'.")
    if will_play == 'y':
        print(art.logo)
        print("Playing Blackjack")

        draw(my_cards)
        draw(my_cards)
        print(f"My current hand is {my_cards}. Total = {sum(my_cards)}")

        draw(computer_cards)
        draw(computer_cards)
        computer_cards_display = []
        computer_cards_display += computer_cards
        computer_cards_display[-1] = "*"
        print(f"Computer's hand is {computer_cards_display}")


        will_pull = input("Do you want to pull another card? Type 'y' or 'n'.")
        if will_pull == 'y':
            draw(my_cards)
            if sum(computer_cards) < 19:
                draw(computer_cards)
            print(f"My cards are :{my_cards}. Total : {sum(my_cards)}")
            print(f"The computer's cards are : {computer_cards}")
            compare_cards(my_cards, computer_cards)
            run_game = False
        else:
            print(f"My cards are :{my_cards}")
            print(f"The computer's cards are : {computer_cards}. Total : {sum(computer_cards)}")
            compare_cards(my_cards, computer_cards)
            print("Thank you for playing")
            run_game = False


    elif will_play == 'n':
        print("Thank you. See you next time!")
        run_game = False
    else:
        print("That's not a valid input. Try again.")

