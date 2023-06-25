#to count the number of diits in the user input


def countDigits(x):
    res=0
    while x>0:
        x= x//10
        res +=1
    return res
if __name__=='__main__':
    number=78988
    print(countDigits(number))


#3
