def loop(n):
    for i in range(0,n+1):
        print("First Loop")
 
    j=1
    while(j<=n+1):
        print("Second Loop ",j)
        j=j*2
 
    for i in range(0,2):
        print("Third loop")

loop(1)