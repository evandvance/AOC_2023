import re
inputs = './inputs/04.txt'
test = './test/04test.txt'

with open(inputs) as file:
    data = file.readlines()

def part1(data):
    return_score = 0

    for i,line in enumerate(data):
        score = 0
        line = re.sub(f'Card {i+1}:','',line)
        line = line.split('|')
        for char in line[0].split():
            temp = line[1].split()
            if char in temp:
                if score == 0:
                    score += 1
                else:
                    score *= 2
        return_score += score

    return return_score

def part2(data):
    cards = []

    for i,line in enumerate(data):
        score = 0
        line = re.sub(f'Card {i+1}:','',line)
        line = line.split('|')
        for char in line[0].split():
            temp = line[1].split()
            if char in temp:
                score += 1
        cards.append(score) 

    temp = [1 for x in cards]
    for i, score in enumerate(cards):
            for j in range(score):
                temp[i+j+1] += temp[i]

    return sum(temp)

print(part1(data))
print(part2(data))