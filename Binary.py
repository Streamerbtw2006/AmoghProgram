num = input("Enter a binary number ") 
num = str(num)
finans = 0

for i in range(0,int(num) + 1):
    dig = int(str(num)[i])
    dig = int(dig) 
    powr = pow(2, i)
    ans = dig * powr
    finans = int(ans) + finans

print(finans)
