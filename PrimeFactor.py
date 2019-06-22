import math 

num2 = input("Type in number. ")

num = int(num2)

pmlist = []

yn = 1
 
if yn == 1:
    sqnum = math.sqrt(num)
    for factors in range(2,num):
        
        if num % factors == 0:
            num = num/factors
            pmlist.append(factors)
            print("factors just detected " + str(factors) + ". Updated number " + str(num))
            
        elif num == factors:
            pmlist.append(factors)
            pmlist.append(num)

        elif type(sqnum) == int:
            pmlist.append(sqnum)
            pmlist.append(sqnum)

        else:
            yn = 0
           
for x in pmlist:
    print(x)
