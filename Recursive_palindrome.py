def palindrom(s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return palindrom(s, l + 1, r - 1)

s = "MalayalaM"
print(palindrom(s, 0, 4))