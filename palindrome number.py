num = int(input("Enter a number: "))
dup = num
rev = 0
while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if(dup == rev):
    print(dup, "is a palindrome number")
else:
    print(dup, "is not a palindrome number")
