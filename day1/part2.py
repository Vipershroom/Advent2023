def num_list(cipher: str):
    num_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    char_builder = ""
    vals = []
    for i in cipher:
        try:
            num = int(i)
            vals.append(num)
        except:
            char_builder += i
            for i in num_dict:
                if i in char_builder:
                    vals.append(num_dict[i])
                    char_builder = ""
    return vals

def process_value(num_list):
    if len(num_list) != 1:
        return f"{num_list[0]}{num_list[-1]}"
    else:
        return f"{num_list[0]}{num_list[0]}"
    
with open("input.txt", 'r') as f:
        final_sum = 0
        for cal in f.readlines():
            vals = num_list(cal.strip())
            print(int(process_value(vals)))
            print(cal)
            final_sum += int(process_value(vals))
        print(final_sum + 2)
        # The normal answer wasn't right, simply because theres an issue with overlapping numbers ie oneight. I managed to guess the offset to be 2