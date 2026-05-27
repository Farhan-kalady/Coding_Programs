count = 0
def func():
    global count
    if count == 4:
        return
    print("Farhan")
    count += 1
    func()
    
print(func())    