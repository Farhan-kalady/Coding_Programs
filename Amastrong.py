def amstrong(n):
    nod = len(str(n))
    num = n
    total = 0
    
    while num > 0:
        ld = num % 10
        total = total + (ld ** nod)
        num = num // 10
    return total == n

print(amstrong(153))