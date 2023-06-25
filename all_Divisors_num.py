def printDivisor(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end=" ")
printDivisor(25)

#efficient solution
def printDivisor(n):
    i=1
    while(i*i<=n):
        if(n%i==0):
            print(i)
            if(i!=n/i):
                print(n//i,end=" ")
        i+=1
printDivisor(25)

#this proram prints in sorted order
def printDivisores(n):
    i=1
    while(i*i<n):
        if(n%i==0):
            print(i,end=" ")
        i+=1
    while(i>=1):
        if(n%i==0):
            print(n//i,end=" ")
        i-=1
printDivisores(100)

"""
1 5 25 1
25.0 5
1 3 5.0 15.0 """