import random

def input_human_play(input=input):
    play = input('rock, paper, or scissors?')
    while not is_valid_play(play):
        return play
    
def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']

def generate_computer_play():
    return random.choice(['rock', 'paper', 'scissors'])

def evaluate_game(human, computer):
    if human == computer:
        return 'tie'
    elif human == 'rock':
        if computer == 'paper':
            return 'computer'
        else:
            return 'human'
    else:
        if computer == 'rock':
            return 'computer'
        else:
            return 'human'


def main(input=input):
    human = input_human_play(input)
    computer = generate_computer_play()

# pred tim : human = input('rock, paper or scissors? ')

#while human not in ['rock', 'paper', 'scissors']:
#    human = input('rock, paper or scissors? ')

# pred tim : computer = random.choice(['rock', 'paper', 'scissors'])

    print(computer)
    game = evaluate_game(human, computer)
    if game == 'tie':
        print('it is a tie')
    else:
        print(f'{game} won')

#    if human == computer:
#        print('it\'s a tie!')
#    elif human == 'rock' and computer == 'paper':
#        print('computer won!')
#    elif human == 'paper' and computer == 'rock':
#        print('human won!')
#    elif human == 'scissors' and computer == 'rock':
#        print('computer won!')
#    elif human == 'rock' and computer == 'scissors':
#        print('human won!')
    
    
if __name__ == '__main__':
    main()    
     
