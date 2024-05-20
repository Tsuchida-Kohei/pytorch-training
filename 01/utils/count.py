from .function import add

def count_word(s, c):
    ans = 0
    for i in range(len(s)):
        if s[i] == c:
            ans = add(ans, 1)
    return ans