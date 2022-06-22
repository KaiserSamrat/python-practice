
num = int(input("Enter : "))
for x in range(num):
    value = int(input("Enter number: "))
    if(value>max):
        max = value
    if(value<min):
        min=value

print("Maximum Value is", max)
print("Minimum Value is", min)


