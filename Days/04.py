import re
inputs = './inputs/04.txt'
test = './test/04test.txt'

with open(test) as file:
    data = file.readlines()

def part1(data):
    return_list = []

    for i,line in enumerate(data):
        line = re.sub(f'Card {i+1}:','',line)
        line= line.split('|')
        for char in line[0].split():
            if char in line[1]:
                return_list.append(int(char))

    return return_list

def part2(data):
    pass

print(sum(part1(data)))