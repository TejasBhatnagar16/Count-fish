# step 1- search for a head thorugh the matrix 
# step 2- when a head is found, look for exactly one body next to it, else
#         the head is invalid 
# step 3- when a head and a body is found, look for subsquent bodies with 
#         no bodies above or below it. 
# step 4- look for a valid tail and store the length of the fish 

def solver(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        global pond, length, breadth 
        data = list(map(str.strip, f.readlines()))
        data = list(map(str.split, data))
        length, breadth = data[0]
        pond = data[1:]
        output_dict = {}
        for i in range(int(length)):
            for j in range(int(breadth)):
                if pond[i][j] == '2':
                    if is_valid_head(j, i): 
                        fish_length = 1
                        if direction(j, i) == 'h': 
                            d = 'h'
                            for k in range(j + 1, int(breadth)): 
                                if pond[i][k] == '1' and  is_valid_body(d, k, i):
                                    fish_length += 1
                                elif pond[i][k] == '2' and is_valid_tail(d, k, i): 
                                    fish_length += 1
                                    if fish_length in output_dict:
                                        output_dict[fish_length] += 1
                                    else: 
                                        output_dict[fish_length] = 1
                                    break 
                                else: 
                                    break 
                        if direction(j, i) == 'v': 
                            d = 'v'
                            for l in range(i+1, int(length)): 
                                if pond[l][j] == '1' and is_valid_body(d, j, l):
                                    fish_length += 1
                                elif pond[l][j] == '2' and is_valid_tail(d, j, l): 
                                    fish_length += 1 
                                    if fish_length in output_dict: 
                                        output_dict[fish_length] += 1
                                    else: 
                                        output_dict[fish_length] = 1
                                    break 
                                else: 
                                    break 
        output_list = []
        for key, value in output_dict.items():
            temp = [key,value]
            output_list.append(temp)
        output_list.sort(key=lambda x: x[0])
        output_list = list(map(lambda x: [str(x[0]), str(x[1])], output_list))
        output_list = list(map(' '.join, output_list))
        output_list = '\n'.join(output_list)
        return output_list
                        
         
def is_valid_head(x, y): 
    count_h = 0
    count_v = 0
    count_total = 0
    if x == int(breadth) - 1 or y == int(length) -1:
        return False 
    if pond[y][x+1] == '2' or  pond[y][x-1] == '2' or pond[y-1][x] == '2' or pond[y+1][x] == '2':
        return False
    elif pond[y][x+1] == '1':
        count_total += 1
        count_h += 1
    elif pond[y+1][x] == '1': 
        count_total += 1
        count_v += 1
    elif pond[y][x-1] == '1':
        count_total += 1
    elif pond[y-1][x] == '1':
        count_total += 1
    return count_total == 1

def direction(x, y): 
    if pond[y][x+1] == '1':
        return 'h'
    elif pond[y+1][x] == '1': 
        return 'v'

def is_valid_body(d, x, y): 
    if x == int(breadth) - 1 or y == int(length) -1:
        return False
    if d == 'h':
        if pond[y+1][x] == '0' and pond[y-1][x] == '0':
            return True 
        else:
            return False 
    else: 
        if pond[y][x+1] == '0' and pond[y][x-1] == '0': 
            return True 
        else: 
            return False 

def is_valid_tail(d, x, y): 
    if x == int(breadth) - 1 or y == int(length) -1: 
        return False
    if d == 'h':
        if pond[y][x+1] == '0' and pond[y-1][x] == '0' and pond[y+1][x] == '0':
            return True 
        else: 
            return False 
    else: 
        if pond[y][x+1] == '0' and pond[y][x-1] == '0' and pond[y+1][x] == '0':
            return True
        else: 
            return False  

# print(solver('fish data\pub10.in'))
for i in range(1, 10):
    input_file = 'fish data\pub' + \
        '0' + str(i) + '.in'
    my_ans = solver(input_file)
    ouput_file = 'fish data\pub' + \
        '0' + str(i) + '.out'
    with open(ouput_file, 'r', encoding='utf-8') as out:
        ans = out.readlines()
        ans = list(map(str.strip, ans))
    my_ans = my_ans.split('\n')
    print(my_ans == ans)
my_ans = solver('fish data\pub10.in')
with open('fish data\pub10.out', 'r', encoding='utf-8') as f:
    ans = f.readlines()
    ans = list(map(str.strip, ans))
    my_ans = my_ans.split('\n')
    print(my_ans == ans) 