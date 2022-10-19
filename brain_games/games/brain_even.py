import brain_games.cli
import random


player_name = brain_games.cli.welcome_user()


def main():

    win_count = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while win_count < 3:

        num = random.randint(1, 100)

        print(f'Question: {num}')

        u_key = input()

        if u_key == 'yes' and num % 2 == 0 or u_key == 'no' and num % 2 != 0:

            print('Correct!')

            win_count += 1
        elif u_key == 'no' and num % 2 == 0:

            print("'no' is wrong answer. Correct answer was 'yes'.")
            print(f"Let's try again, {player_name}!")
            quit()

        elif u_key == 'yes' and num % 2 != 0:

            print("'yes' is wrong answer. Correct answer was 'no'.")
            print(f"Let's try again, {player_name}!")
            quit()

    print('Congratulations, ' + str(player_name) + '!')
