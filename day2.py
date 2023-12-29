# import input data
with open('day2_input.txt') as f:
    input = [x.rstrip('\n') for x in f.readlines()]

# condition given in task description
max_numbers = {'red': 12, 'green': 13, 'blue': 14}

games_sum = 0
powers_sum = 0

# looping and evaluting game by game
for game in input:
    valid = 1
    # getting game number and draws in the game
    game_number = int(game.split(':')[0].split(' ')[1])
    draws = [x.lstrip(' ').split(', ') for x in game.split(':')[1].split(';')]
    max_cubes = {'red': 0, 'green': 0, 'blue': 0 }
    # check all the draws if it is valid and also collect max cubes used per color in a game
    for draw in draws:
        for color in draw:
            count, name = color.split(' ')
            if int(count) > max_numbers.get(name):
                valid = 0
            max_cubes[name] = max(max_cubes[name], int(count)) 
    games_sum += game_number * valid
    powers_sum += max_cubes['red'] * max_cubes['green'] * max_cubes['blue']

print('Answer to part one is: {}'.format(games_sum))
print('Answer to part two is: {}'.format(powers_sum))