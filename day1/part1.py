def num_list(cipher):
    vals = []
    for i in cipher:
        try:
            num = int(i)
            vals.append(num)
        except:
            continue
    return vals

def process_value(num_list):
    if len(num_list) != 1:
        return f"{num_list[0]}{num_list[-1]}"
    else:
        return f"{num_list[0]}{num_list[0]}"

file = 'input.txt'

with open("input.txt", 'r') as f:
        final_sum = 0
        for cal in f.readlines():
            vals = num_list(cal.strip())
            print(int(process_value(vals)))
            print(cal)
            final_sum += int(process_value(vals))
        print(final_sum)
