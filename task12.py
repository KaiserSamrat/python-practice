num = 9867
copyNum = num
count = 0

while num != 0:
    num //= 10
    count += 1

print("Total Length: " , count)

newNum = pow(10,count-1)
print(newNum)

while copyNum>0:
    converted= copyNum //newNum
    copyNum= copyNum%newNum
    newNum=newNum/10
    print(int(converted),end=",")
  
