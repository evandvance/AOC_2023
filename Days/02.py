import re
from datetime import datetime

with open('./inputs/02.txt') as file:
    data = file.readlines()

def part1(line_of_data:str) -> list:
    #It appears I am a big fan of making the least efficient program
    list_of_possible_games = []
    max_color = {
        'red':12,
        'green':13,
        'blue':14
    }


    for i,line in enumerate(line_of_data):
        #removes whitesplaces and formats the line into a list of lists where the outer list is is one game and the nested lists are draws
        game = [x.split(',') for x in ''.join(line.split()).replace(f'Game{i+1}:','').split(';')] 
        valid_game = True
        for draw in game:
            for item in draw:
                if int(re.sub(r'\D','',item)) > max_color[re.sub(r'[0-9]','',item)]:
                    valid_game = False
                    break
        if valid_game:
            list_of_possible_games.append(i+1)
            
    return list_of_possible_games


def part2(line_of_data:str) -> list:
    #It appears I am a big fan of making the least efficient program
    list_of_powers = []

    for i,line in enumerate(line_of_data):
        #removes whitesplaces and formats the line into a list of lists where the outer list is is one game and the nested lists are draws
        game = [x.split(',') for x in ''.join(line.split()).replace(f'Game{i+1}:','').split(';')] 
        power_dict = {'red': 0,'blue' :0,'green': 0}

        for draw in game:
            for item in draw:
                if int(re.sub(r'\D','',item)) > power_dict[re.sub(r'[0-9]','',item)]:
                    power_dict[re.sub(r'[0-9]','',item)] = int(re.sub(r'\D','',item))

        temp = 1
        for num in power_dict.values():
            temp *= num

        list_of_powers.append(temp)

    return list_of_powers

start_time = datetime.now()
print(sum(part1(data)))
print(sum(part2(data)))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))