input1 = int(input("enter the number :"))

orignalnumber = input1

result = 0

while input1 > 0:
    digit = input1 % 10
    result = result * 10 + digit
    input1 //= 10

if orignalnumber==result :
    print(f"{orignalnumber} is a palindrome")
else :
    print(f"{orignalnumber} is not a palindrome")
