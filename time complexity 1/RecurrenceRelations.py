def myfunction1(n):
    if(n<=0):
        return
    for i in range (0,n+1):
        print("Codingal")
    myfunction1(n//2)
    myfunction1(n//3)

def myfunction2(n):
    if(n<=1):
        return
    print("Codingal1")
    myfunction2(n-1)


myfunction1(2)
myfunction2(4)