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
        question = f'Question: {random_number1} {op_symbol} {random_number2}'
        ans = op_function(random_number1, random_number2)

        print(question)

        u_key = input()

        if u_key == str(ans):

            print(f'Your answer: {ans}\nCorrect!')

            win_count += 1

        elif u_key != str(ans):

            print(f'Your answer: {u_key}')
            print(f'"{u_key}" is wrong ans ;(. Correct answer was "{ans}".')
            print(f"Let's try again, {player_name}!")
            quit()
    print('Congratulations, ' + str(player_name) + '!')
