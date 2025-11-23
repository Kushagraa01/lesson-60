def find_lcm(num1, num2):
    if num1>num2:
        greater=num1
    else:
        greater=num2
    while True:
        if (greater % num1 == 0) and (greater % num2 == 0):
            lcm = greater
            break
        greater += 1
    return lcm

number1 = int(input("Enter the greater number(please enter integers only): "))
number2 = int(input("Enter the smaller number(please enter integers only): "))
result_lcm = find_lcm(number1, number2)
print(f"The LCM of {number1} and {number2} is {result_lcm}")