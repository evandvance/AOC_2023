from util.time_me import time_me
from util.cache_me import cache_me


def range_check(seed:int, map_range:list ) -> bool:
    if seed in range(map_range[1], map_range[1] + map_range[-1]):
            return True

def get_next_value(seed:int, map_list:list) -> int:
    for ele in map_list:
        if range_check(seed, ele):
            return ele[0] + (seed - ele[1])
    return seed

def map_seed(seed:int, data:dict) -> dict:
    r_dict = {'seed':seed}
    # del data['seeds']

    for key, val in data.items():
        if key == 'seeds':
            continue
        r_key = key.replace(' map','').split('-')[-1] #Get New Key for return dict
        prev_seed = r_dict[key.split('-')[0]]
        r_dict[r_key] = get_next_value(prev_seed,val)
    
    print(f'Seed {r_dict['seed']} location: {r_dict['location']}')
    return r_dict

def check_smallest(solved_map, smallest):
    for seed in solved_map:
        if seed['location'] < smallest:
            smallest = seed['location']

    return smallest

@time_me
def part_one(data):
    solved_map = [map_seed(seed,data) for seed in data['seeds'][0]]
    return check_smallest(solved_map, 999999999999999999999999999999)

def part_two(data):
    print('Part Two has begun.....')
    smallest = 999999999999999999999999999999999999
    seeds = data['seeds'][0]


if __name__ == "__main__":
    test = './test/05test.txt'
    inputs = './inputs/05.txt'
    with open(inputs) as file:
        data = {item[0]: [[int(y) for y in x.split()] for x in item[1].strip().split('\n')] for item in [item.split(':') for item in file.read().split('\n\n')]}

    print(part_one(data))
    # print(part_two(data))