import color
from data import data
import random
from art import logo, vs, lose, correct


def get_random_account():
    return random.choice(data)


def get_form(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f'''|--------------------------|
   |Name          {name}        
   |Description   {description} 
   |Country       {country}     
   |--------------------------|'''


print(logo)

score = 0
game_should_continue = True
account_one = get_random_account()
while game_should_continue:
    account_two = get_random_account()
    if account_one == account_two:
        account_two = get_random_account()
    print(f"A: {color.YELLOW}{get_form(account_one)}{color.END}")
    print(vs)
    print(f"B: {color.PURPLE}{get_form(account_two)}{color.END}")

    letter = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_value = account_one["follower_count"]
    b_value = account_two["follower_count"]
    if (a_value > b_value and letter == 'a') or (b_value > a_value and letter == 'b'):
        score += 1
        print(correct)
        print(f'{color.LIGHT_GREEN}Your score is {score}{color.END}')
        if a_value > b_value:
            account_one = account_one
        else:
            account_one = account_two
    else:
        print(lose)
        print(f"{color.LIGHT_RED}Your score was {score}{color.END}")
        game_should_continue = False
