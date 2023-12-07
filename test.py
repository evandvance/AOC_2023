import re
def find_numbers(line,y):
    # 467..114..
    return_list = []
    for match in re.finditer(r'\d+',line):
        span = range(match.start()-1,match.end()+1)
        if y in span:
            return_list.append(match.group())
        
    return return_list

print(find_numbers('467..114..',4))
