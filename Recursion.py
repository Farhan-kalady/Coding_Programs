count = 0
def func():
    global count
    if count == 4:
        return
    print("Farhan")
    count += 1
    func()
func()    

def recursion(x,n):
    if n == 0:
        return
    print(x)
    recursion(x, n-1)
    
recursion("farhan",4)    

def recu(sum, i, n):
    if i > n:
        print(sum)
        return
    recu(sum + i, i + 1, n)
recu(0,1,10)    

def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)
print(sum(10))