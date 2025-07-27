smallest = int(input("enter the smallest number :"))
largest = int(input("enter the largest number :"))

while(smallest):
    temp = smallest
    smallest= largest % smallest
    largest = temp

print (f" GCD is {largest}")