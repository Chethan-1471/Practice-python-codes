def small(n,input):
    num=[]
    for x in n:
        if x<input:
            num.append(x)
    return num
input=int(input("enter"))
n=[10,20,30,40,60,80]
print(small(n,input))

#enter60
#[10, 20, 30, 40]
