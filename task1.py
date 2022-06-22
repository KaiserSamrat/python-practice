# # 1(b)
# counter2 = -10 
 
# # loop structure 
# while counter2 <= 20: 
     
#     #inside loop body 
#     if counter2 == 20: 
#         print(counter2, end = "")  
#     else: 
#         print(counter2, end = ", ")  
      
#     counter2 = counter2 + 5 

# #1(c)
# print("/n")
# counter3 = 18 
 
# # loop structure 
# while counter3 <= 63: 
     
#     #inside loop body 
#     if counter3 == 63: 
#         print(counter3, end = "")  
#     else: 
#         print(counter3, end = ", ")  
      
#     counter3 = counter3 + 9 

#     counter3 = 18 
 
# # loop structure 
# print("/n")
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