
numOfPrint = input("Enter the number: ")
convertedNum = int(numOfPrint)
result = 0
for i in range(1, convertedNum + 1) :
		if (i % 2 == 0):
			result = result - pow(i, 2)
		else:
			result = result + pow(i, 2)

print(result)






