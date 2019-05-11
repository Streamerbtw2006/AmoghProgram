
num = input ("enter NUMBER)
num = int(num, 10)

fact = 1

if num < 0:
   print("Can't be negative")
elif num == 0:
   print("Ans 0")
else:
   for i in range(1,num + 1):
       fact = fact*i
   print("The factorial of",num,"is",fact)
