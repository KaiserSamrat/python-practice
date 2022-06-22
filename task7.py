sum= 0
count=0
for x in range(10):
    numInput = int(input())
    if(numInput%2!=0):
        sum=sum+numInput
        count=count+1
average= sum/count

print(sum)
print(average)