from Util import Util
import math

day = "06"

def calc_win_cons(max_time, record):
    speed = 1
    max_time -= 1

    while max_time > speed:
        distance = speed * max_time
        if distance > record:
            return max_time - speed + 1
        speed += 1
        max_time -= 1

@Util.time_me
def part_one(data):
    return math.prod([calc_win_cons(t,w) for t,w in data])

@Util.time_me
def part_two(data):
    time = int(''.join(data[0]))
    record = int(''.join(data[1]))
    return calc_win_cons(time,record)

if __name__ == "__main__":
    test = False
    input_file = './test/{}test.txt'.format(day) if test else './inputs/{}.txt'.format(day)

    with open(input_file) as file:
        data = [x[1].strip().split() for x in [item.split(':') for item in [x.strip() for x in file.readlines()]]]

    part_one_data = [[int(t),int(data[1][i])]for i,t in enumerate(data[0])]

    # calc_win_cons(30,200)
    print(part_one(part_one_data)) #Instant 393120
    print(part_two(data)) #4.610965 sec 36872656 Somehow every subsequent time ive run this its taken longer