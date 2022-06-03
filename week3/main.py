import random
game = ['R', 'S', 'P']
# Where R = rock, S = scissors and P = paper
cpu = random.choice(game)
print('Welcome to the Rock, Paper and Scissors game!!!!, make your choice, R for Rock, P for Paper and S for Scissors')
user = (input('R, S or P: ')).upper()
# print(user)    
# print(cpu)
while user == cpu:
    print('It\'s a tie! Repeat game')
    user = (input('R, S or P: ')).upper()
    cpu =  random.choice(game)    
if user == 'R' and cpu == 'S':
    print('Player wins Player(Rock): CPU(Scissors)')
elif user == 'S' and cpu == 'P':
    print('Player wins, Player(Scissors): CPU(Paper)')
elif user == 'P' and cpu == 'R':
    print('Player wins, Player(Paper): CPU(Rock)')
elif user == 'S' and cpu == 'R':
    print('The computer wins, Player(Scissors): CPU(Rock)')
elif user == 'P' and cpu == 'S':
    print('The computer wins, Player(Paper): CPU(Scissors)')
elif user == 'R' and cpu == 'P':
    print('The computer wins, Player(Rock): CPU(Paper)')
else: 
    print('That\'s not a valid input')

input('Press the enter key to exit.')
