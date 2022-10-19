import brain_games.cli
import random


player_name = brain_games.cli.welcome_user()

def main():

    win_count = 0

    print("Find the greatest common divisor of given numbers.")

    while win_count < 3:

        random_number1 = random.randint(1, 100) 
        random_number2 = random.randint(1, 100)

        print('Question: {} {}'.format(random_number1,random_number2))

        if random_number1 > random_number2:
            smaller_number = random_number2
        else: 
            smaller_number = random_number1

        for i in range(1, smaller_number + 1):
            if ((random_number1 % i == 0) and (random_number2 % i == 0)):
                gcd = i

        user_input = input()

        if user_input == str(gcd):
            print(f'Your answer: {gcd}\nCorrect!')
            win_count += 1

        else:
            print("{} is wrong answer. Correct answer was {}\nLet's try again, {}!".format(user_input, gcd, player_name))
            quit()
        
    print('Congratulations, {}!'.format(str(player_name)))

        


