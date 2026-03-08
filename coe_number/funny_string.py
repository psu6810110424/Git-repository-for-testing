def funny_string(s):
    r = s[::-1]
    diff_s = [abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s))]
    diff_r = [abs(ord(r[i]) - ord(r[i-1])) for i in range(1, len(r))]
    return "Funny" if diff_s == diff_r else "Not Funny"