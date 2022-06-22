num = int(input("Enter a number: "))
n=0
while num>0:
    converted = num%10
    num = num - converted
    num = num/10
    print(int(converted),end=",")
    n = n + 1 