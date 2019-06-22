list = []

n = 0
i = 0
sum = 0
while n < 10:
    if n ==0:
       num = input("Enter a number")

    elif n == 9:
        num = input("Enter the last number")
   
    else:
       num = input("Enter another number")
   
    list.append(num)
    n =n + 1


for i in list:
   sum += i

print ("Sum of numbers is " + str(sum))

