def read_input():
    input_type = input().rstrip()
    if input_type == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == "F":
        file_path = input().rstrip()
        with open(file_path, "r") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    prime = 10000000007
    p_len, txt_len = len(pattern), len(text)
    base, base_pow = 256, pow(256, p_len-1, prime)
    p_hash, txt_hash = 0, 0
    occurrences = []
    
    for i in range(p_len):
        p_hash = (base * p_hash + ord(pattern[i])) % prime
        txt_hash = (base * txt_hash + ord(text[i])) % prime
    
    for i in range(txt_len - p_len + 1):
        if p_hash == txt_hash and pattern == text[i:i + p_len]:
            occurrences.append(i)
        if i < txt_len - p_len:
            txt_hash = (base * (txt_hash - ord(text[i]) * base_pow) + ord(text[i + p_len])) % prime
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
