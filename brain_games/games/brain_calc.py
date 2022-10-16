import brain_games.cli
import operator
import random


player_name = brain_games.cli.welcome_user()


def main():

    win_count = 0

    print("What is the result of the expression?")


    while win_count < 3:

        OPERATORS = [
            ('+', operator.add),
            ('-', operator.sub),
            ('*', operator.mul)
            ]
 
        random_number1 = random.randint(1, 100)
        random_number2 = random.randint(1, 100)
        op_symbol, op_function = random.choice(OPERATORS)
        question = '{} {} {}'.format(random_number1, op_symbol, random_number2)
        answer = op_function(random_number1, random_number2)

        #print(answer)

        print(question)

        user_input = input()

        if user_input == str(answer):

            print('Correct!')

            win_count += 1

        elif user_input != str(answer):

            print(f'Wrong!\nCorrect answer is {answer}')
            quit()    

    print('Congratilations, ' + str(player_name) + '!')

    