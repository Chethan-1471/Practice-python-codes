#palindrome number
#should be same from left to right and also right to left
#single digit also palindrome

def ispal(n):
   rev=0           #reverse=0
   temp=n          #using temp variable to store n(user input)
   while temp!=0:
       ld=temp%10     #ld-lastdigit
       rev=rev*10+ld
       temp=temp//10
   return rev==n
if __name__=='__main__':
    number=4553
    print(ispal(number))


#False


#for string
s=input("enter")
reverse=s[::-1]
if(s==reverse):
    print("pal")
else:
    print("not")