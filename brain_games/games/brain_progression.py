import brain_games.cli
import random


player_name = brain_games.cli.welcome_user()


def main():

    win_count = 0

    print("What number is missing in the progression?")

    while win_count < 3:

        random_initial = random.randint(1, 10)
        random_prog = random.randint(1, 5)

        new_list = [random_initial]

        _count = 0

        while _count < 9:
            prev_num = new_list[_count]
            new_list.append(prev_num + random_prog)
            _count += 1

        r_num = random.choice(new_list)
        r_num_index = new_list.index(r_num)

        q_l = new_list.copy()
        q_l.insert(r_num_index, '..')
        q_l.remove(r_num)

        print("Question: ", end='')
        print(*q_l, end='\n')

        u_key = input()

        if u_key == str(r_num):
            print("Your answer is : {}\nCorrect!".format(u_key))
            win_count += 1
        elif u_key != str(r_num):
            print(f"Your answer is : {u_key}")
            print(f"{u_key} is wrong answer. Correct answer was {r_num}")
            print(f"Let's try again, {player_name}!")
            quit()

    print(f"Congratulations, {player_name}!")
