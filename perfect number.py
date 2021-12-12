num = int(input("Enter a number: "))
Sum = 0
for i in range(1, num):
    if(num % i == 0):
        Sum = Sum + i
if (Sum == num):
    print(num, "is a perfect number" )
else:
    print(num, "is not a perfect number")
