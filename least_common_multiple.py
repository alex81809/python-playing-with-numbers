# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# determine which number is greater
if num1 > num2:
    greater = num1
else:
    greater = num2

# keep incrementing 'greater' until it's divisible by both numbers
while True:
    if (greater % num1 == 0) and (greater % num2 == 0):
        lcm = greater
        break
    greater += 1

print(f"The LCM of {num1} and {num2} is: {lcm}")
