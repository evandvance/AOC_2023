inputs = './inputs/05.txt'
test = './test/05test.txt'

with open(test) as file:
    data = {item[0]: item[1].split('\n') for item in [item.split(':') for item in file.read().split('\n\n')]}

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

@memorize
def get_next_value(seed,map_list):
    for ele in map_list:
        ele = ele.split()
        if ele == []:
            continue
        if int(seed) in range(int(ele[1]), int(ele[1]) + int(ele[-1])):
            return int(ele[0]) + (int(seed) - int(ele[1]))
    return seed

def map_seed(seed, data):
    r_dict = {'seed':seed}

    for key, val in data.items():
        if key == 'seeds':
            continue
        r_dict[key.replace(' map','').split('-')[-1]] = get_next_value(r_dict[key.split('-')[0]],val)
    
    print(f'Seed location: {r_dict['location']}')
    return r_dict

def check_smallest(solved_map, smallest):
    for seed in solved_map:
        if seed['location'] < smallest:
            smallest = seed['location']

    return smallest

def part_one(data):
    solved_map = [map_seed(seed,data) for seed in data['seeds'][0].split()]
    smallest = 999999999999999999999999999999999999
    for seed in solved_map:
        if seed['location'] < smallest:
            smallest = seed['location']

    return smallest

def part_two(data):
    smallest = 999999999999999999999999999999999999
    seeds = data['seeds'][0].split()

    #The strategy I am trying is to break the seeds up into quarters and finding the smallest in each quarter (similar to binary search)

    seed_range_one = {"start":int(seeds[0]), "half":(int(seeds[0]) + int(seeds[1]))//2, "end":int(seeds[0]) + int(seeds[1])}
    print("Seed_range_One Generated....")

    seed_range = range(seed_range_one['start'], seed_range_one["half"])
    map_1 = [map_seed(seed,data) for seed in seed_range]

    smallest = check_smallest(map_1,smallest)
    print(smallest)

    seed_range = range(seed_range_one['half'], seed_range_one["end"])
    map_2 = [map_seed(seed,data) for seed in seed_range]

    smallest = check_smallest(map_2,smallest)

    print(smallest)

    seed_range_two = {"start":int(seeds[2]), "half":(int(seeds[2]) + int(seeds[3]))//2, "end":int(seeds[2]) + int(seeds[3])}

    print("Seed_range_two Generated....")

    seed_range = range(seed_range_two['start'], seed_range_two["half"])
    map_1 = [map_seed(seed,data) for seed in seed_range]

    smallest = check_smallest(map_1,smallest)
    print(smallest)

    seed_range = range(seed_range_two['half'], seed_range_two["end"])
    map_2 = [map_seed(seed,data) for seed in seed_range]

    smallest = check_smallest(map_2,smallest)
    print(smallest)

    return smallest

if __name__ == "__main__":
    part2 = part_two(data)
    # print(f"Part one: {part_one(data)}")
    print(f"Part two: {part2}")

    with open('./answer.txt') as file:
        file.write(part2)
