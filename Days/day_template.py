from time_me import time_me
day = ""

@time_me
def part_one(data):
    pass

@time_me
def part_two(data):
    pass

if __name__ == "__main__":
    test = True
    input_file = './test/{}test.txt'.format(day) if test else './inputs/{}.txt'.format(day) 

    with open(input_file) as file:
        data = file.readlines()

    print(f'Part 1 solution: {part_one(data)}')
    print(f'Part 2 solution: {part_two(data)}')