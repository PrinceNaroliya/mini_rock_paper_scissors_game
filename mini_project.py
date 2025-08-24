import random

print('---Rock Paper Scissor---')

user_win = 0
comp_win = 0

user_input = input('Enter yes if you want to play this game: ')

if user_input == 'yes':
    while True:
        option = ['rock', 'paper', 'scissor']

        user = input('Enter a option (rock/paper/scissor or exit): ').lower()
        comp = random.choice(option)

        if user == 'exit':
            print("Game Over. Bye!")
            break

        print(f"Computer chose: {comp}")

        if user == comp:
            print("It's a Draw!")
        elif user == 'rock' and comp == 'scissor':
            print('You Win!')
            user_win += 1
        elif user == 'paper' and comp == 'rock':
            print('You Win!')
            user_win += 1
        elif user == 'scissor' and comp == 'paper':
            print('You Win!')
            user_win += 1
        elif user in option:
            print('You Lose!')
            comp_win += 1
        else:
            print("Invalid input, please choose rock/paper/scissor or exit")
else:
    print('Goodbye!')

print(f'User Win: {user_win}')
print(f'Computer Win: {comp_win}')
