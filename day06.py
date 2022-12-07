def distinct(n, s=input()):
    return next(i for i in range(n, len(s)) if len(set(s[i - n : i])) == n)


print(*(distinct(n) for n in (4, 14)))  # 1640 3613
