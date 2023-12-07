import re

with open('./inputs/01.txt') as file:
    data = file.readlines()

num_to_int = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def make_int(string):
    temp = ''
    for char in string:
        if char.isnumeric():
            break
        temp += char
        for num in num_to_int.keys():
            if num in temp:
                string = re.sub(temp, num_to_int[num],string,1)
                break

    temp = ''
    for char in string[::-1]:
        if char.isnumeric():
            break
        temp += char
        for num in num_to_int.keys():
            if num in temp[::-1]:
                string = re.sub(temp[::-1], num_to_int[num],string)
                break

    return string

def part1(list_of_strings):
    return_list = []
    for line in list_of_strings:
        line = re.sub(r'\D', '',line)
        return_list.append(int(line[0]+line[-1]))

    return return_list

def part2(list_of_strings):
    return_list = []
    for line in list_of_strings:
        line = make_int(line.replace('\n',''))
        line = re.sub(r'\D', '',line)
        return_list.append(int(line[0]+line[-1]))

    return return_list

print(sum(part1(data)))
print(sum(part2(data)))