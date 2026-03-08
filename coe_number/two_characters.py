from itertools import combinations

def two_characters(s):
    max_len = 0
    for char_pair in combinations(set(s), 2):
        filtered = [c for c in s if c in char_pair]
        if all(filtered[i] != filtered[i+1] for i in range(len(filtered) - 1)):
            max_len = max(max_len, len(filtered))
    return max_len