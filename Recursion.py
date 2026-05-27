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