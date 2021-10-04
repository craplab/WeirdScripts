numamount = int(input("How many numbers do you need to check? "))
oddcount = 0
evencount = 0
for i in range(0,numamount):
    num = int(input("Enter a number: "))
    if (num % 2 == 0):
        print(str(num) + " is an even number.")
        evencount += 1
    else:
        print(str(num) + " is an odd number.")
        oddcount += 1
print("You entered " + str(evencount) + " even number(s).")
print("You entered " + str(oddcount) + " odd number(s).")
