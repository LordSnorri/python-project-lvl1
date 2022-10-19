import brain_games.cli
import random

player_name = brain_games.cli.welcome_user()


def main():

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    win_count = 0

    while win_count < 3:

        flag = 0
        random_number = random.randint(2, 100)
        
        print('Question: ' + str(random_number))

        user_input = input()

        if random_number > 1:
            for i in range(2, int(random_number/2)+1):
                if (random_number % i) == 0:
                    flag = 1
                    break
            
            if flag == 0 and user_input == 'yes':
                print('Correct')
                win_count += 1
            elif flag == 0 and user_input == 'no':
                print(f"'no' is wrong answer. Correct answer was 'yes'\nLet's try again, {player_name}!")
                quit()
            elif flag == 1 and user_input == 'no':
                print('Correct')
                win_count += 1
            elif flag == 1 and user_input == 'yes':
                print(f"'yes' is wrong answer. Correct answer was 'no'\nLet's try again, {player_name}!")
                quit()
            
    print('Congratilations, ' + str(player_name) + '!')



