counter4 = 18

count = 1
while counter4 <= 63: 
     
    #inside loop body 
    if counter4 == 63 and (count%2==0): 
        print(counter4*-1, end = "")  
    elif (count%2==0): 
        print(counter4*-1, end = ", ")
    else:  
        print(counter4, end = ", ")
      
    counter4 = counter4 + 9 
    count = count+1