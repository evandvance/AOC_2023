inputs = './inputs/05.txt'
test = './test/05test.txt'


def memorize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

with open(inputs) as file:
    data = {item[0]: item[1].split('\n') for item in [item.split(':') for item in file.read().split('\n\n')]}

@memorize
def get_next_value(seed,map_list):
    for ele in map_list:
        ele = ele.split()
        if ele == []:
            continue
        if int(seed) in range(int(ele[1]), int(ele[1]) + int(ele[-1])):
            return int(ele[0]) + (int(seed) - int(ele[1]))
    return seed

@memorize
def map_seed(seed, data):
    r_dict = {'seed':seed}

    for key, val in data.items():
        if key == 'seeds':
            continue
        r_dict[key.replace(' map','').split('-')[-1]] = get_next_value(r_dict[key.split('-')[0]],val)
    
    return r_dict

def part_one(data):
    solved_map = [map_seed(seed,data) for seed in data['seeds'][0].split()]
    smallest = 999999999999999999999999999999999999
    for seed in solved_map:
        if seed['location'] < smallest:
            smallest = seed['location']

    return smallest

def part_two(data):
    seeds = data['seeds'][0].split()
    seed_range = [seed for seed in range(int(seeds[0]),int(seeds[0]) + int(seeds[1]))]

    for seed in range(int(seeds[2]), int(seeds[2]) + int(seeds[3])):
        if seed not in seed_range:
            seed_range.append(seed)

    solved_map = [map_seed(seed,data) for seed in seed_range]

    smallest = 999999999999999999999999999999999999
    for seed in solved_map:
        if seed['location'] < smallest:
            smallest = seed['location']

    return smallest

if __name__ == "__main__":
    # print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")