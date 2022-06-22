from cmath import log


num = int(input("Enter : "))
x=1
sum = 0

   
while x <= int(num/2):
     print(num,x)
     if(num%x==0):
        sum = sum+x
     x=x+1


if(sum==num and num>0):
    print(num, "is a perfect number")
else:
    print(num, "is not perfect number") 