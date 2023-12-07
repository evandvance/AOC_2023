import re

inputs = './inputs/03.txt'
test = './test/03test.txt'

with open(inputs) as file:
    data = file.readlines()

def find_numbers(line,y):
    return_list = []
    for match in re.finditer(r'\d+',line):
        span = range(match.start()-1,match.end()+1)
        if y in span:
            return_list.append(int(match.group()))
        
    return return_list


def part1(data):
    parts = []

    for x,line in enumerate(data):
        for y,char in enumerate(line):
            if char in '*/+%&-=$@#':
                line_above = data[x-1]
                line_below = data[x+1]

                parts += find_numbers(line_above,y)
                parts += find_numbers(line,y)
                parts += find_numbers(line_below,y)

    return parts


def part2(data):
    parts = []

    for x,line in enumerate(data):
        for y,char in enumerate(line):
            if char in '*':
                temp = []
                line_above = data[x-1]
                line_below = data[x+1]

                temp += find_numbers(line_above,y)
                temp += find_numbers(line,y)
                temp += find_numbers(line_below,y)

                if len(temp) == 2:
                    parts.append(temp[0]*temp[1])


    return parts

print(sum(part1(data)))
print(sum(part2(data)))
