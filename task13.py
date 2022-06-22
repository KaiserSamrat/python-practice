num = int(input('Enter num: '))
space = ""
count=0
for x in range(1, num+1):
       if num % x == 0:
            count = count+1
            if  x!=num:
                space+=str(x)+", "
            else:
                space+=str(x)

print(space)
print("Total", count, "divisors")