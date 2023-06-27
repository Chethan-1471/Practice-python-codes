 #fibonacci - A series in which next number is a sum of previous two number


#iterative method
first,secound=0,1
n=int(input("num--"))
print("fibonacci series are:")
for i in range(0,n):
    if i<=1:
        result=i
    else:
        result=first+secound
        first=secound
        secound=result
    print(result)

#recursive method

first,secound=0,1
n=int(input("num--"))
def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print("fibo series are:")
for i in range (0,n):
    print(fibonacci(i))