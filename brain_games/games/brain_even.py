import brain_games.cli
import random


player_name = brain_games.cli.welcome_user()


def main():

    win_count = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')


    while win_count < 3:

        random_number = random.randint(1, 100)

        print(f'Question: {random_number}')

        user_input = input()        

        if user_input == 'yes' and random_number % 2 == 0 or user_input == 'no' and random_number % 2 != 0:
            
            print('Correct!')
            
            win_count += 1
        elif user_input == 'no' and random_number % 2 == 0:# or user_input == 'yes' and random_number % 2 != 0:  
            
            print(f"'no' is wrong answer. Correct answer was 'yes'\nLet's try again, {player_name}!")

            quit()

        elif user_input == 'yes' and random_number % 2 != 0:

            print(f"'yes' is wrong answer. Correct answer was 'no'\nLet's try again, {player_name}!")  

            quit()   


    print('Congratulations, ' + str(player_name) + '!')