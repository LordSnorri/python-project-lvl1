import brain_games.cli
import random

player_name = brain_games.cli.welcome_user()


def prime_check(number):
    flag = 0
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                flag = 1
                return flag
        return flag


def main():

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    win_count = 0

    while win_count < 3:

        random_number = random.randint(2, 100)

        print('Question: ' + str(random_number))

        user_input = input()

        if prime_check(random_number) == 0 and user_input == 'yes':
            print('Correct!')
            win_count += 1
        elif prime_check(random_number) == 0 and user_input == 'no':
            print("'no' is wrong answer. Correct answer was 'yes'.")
            print(f"Let's try again, {player_name}!")
            quit()
        elif prime_check(random_number) == 1 and user_input == 'no':
            print('Correct!')
            win_count += 1
        elif prime_check(random_number) == 1 and user_input == 'yes':
            print("'yes' is wrong answer. Correct answer was 'no'.")
            print(f"Let's try again, {player_name}!")
            quit()

    print('Congratulations, ' + str(player_name) + '!')
