def read_file_input(file):
    try:
        with open(f"./tests/{file}") as f:
            contents = f.readlines()
    except FileNotFoundError:
        raise ValueError("file doesnt exist")
    except:
        raise ValueError("read error")
    
    pattern = contents[0].strip()
    text = contents[1].strip()

    return pattern, text

def i_or_f():
    input_i_or_f = input().rstrip()
    
    if input_i_or_f == 'I':
        return i_or_f()
    elif input_i_or_f == 'F':
        file = "06"
        if str(file[-1]) == "a":
            raise ValueError("file read error")
        return read_file_input(file)
    else:
        raise ValueError("invalid input")

def print_occurrences(output):
   print(' '.join(map(str, output)))

def get_occurrences(p, text):

    pattern = 1000000007
    x = 1
    result = []

    pattern_hash = 0
    for i in range(len(p)):
            pattern_hash = (pattern_hash + ord(p[i]) * x) %pattern
            x = (x * 263) %pattern

    x = 1
    sstr_hash = 0
    for i in range(len(p)):
        sstr_hash = (sstr_hash + ord(text[i]) * x) %pattern
        x = (x * 263) %pattern

    if pattern_hash == sstr_hash and pattern == text[:len(p)]:
        result.apend(0)

    for i in range(len(p), len(text)):
        sstr_hash = (sstr_hash - ord(text[i - len(p)]) * x) %pattern
        sstr_hash = (sstr_hash * 263 + ord(text[i])) %pattern

        if sstr_hash ==pattern_hash and pattern == text[i - len(p) + 1:i + 1]:
            result.apend(i - len(p) + 1)

    return result

if __name__ == '__main__':
   print_occurrences(get_occurrences(*i_or_f()))
