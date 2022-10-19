import brain_games.cli
import random


player_name = brain_games.cli.welcome_user()

def main():

    win_count = 0

    print("What number is missing in the progression?")

    while win_count < 3:

        random_initial = random.randint(1,10)
        
        random_prog = random.randint(1,5)
        
        new_list = [random_initial]
        
        _count = 0

        while _count < 9:
            prev_num = new_list[_count]
            new_list.append(prev_num + random_prog)
            _count += 1
        
        random_number = random.choice(new_list)
        random_number_index = new_list.index(random_number)

        q_list = new_list.copy()
        new_q_list = q_list.insert(random_number_index, '..')
        new_q_list = q_list.remove(random_number)
       

        print("Question: {0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(q_list[0],q_list[1],q_list[2],q_list[3],q_list[4],q_list[5],q_list[6],q_list[7],q_list[8],q_list[9]))

        user_input = input()

        if user_input == str(random_number):
            print("Your answer is : {}\nCorrect!".format(user_input))
            win_count += 1
        elif user_input != str(random_number):
            print("Your answer is : {}\n{} is wrong answer. Correct answer was {}\nLet's try again, {}!".format(user_input,user_input,random_number,player_name))
            quit()

    print(f"Congratulations, {player_name}!")

    



