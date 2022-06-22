flag = False
num = int(input("Enter number: "))
  
for x in range(2, int(num/2)):
        if (num % x == 0):
            flag = False
            break
        else:
           flag = True

if(flag == True):
    print("This is a prime number")
else:
    print('Not Prime Number')


