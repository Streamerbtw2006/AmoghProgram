num2 = input("Type in number. ")

num = int(num2)
 
if num > 1:
    for factors in range(2,num):
        print(factors)
        if num % factors == 0:
            print("Your number is composite")
            print(str(num) + " = " + str(factors) + " times " + str(num/factors))
            break

    else:
        print("Your number is prime")

else:
    print("Your number is not prime or composite")
