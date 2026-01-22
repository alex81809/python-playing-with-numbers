# program to find hcf/gcd 

# enter 2 numbers 
numberLargest = int(input("Enter Largest number: "))
numberSmallest = int(input("Enter Smallest number: "))

# using eucliden algorithms 
while (numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore 

print("HCF is: ", numberLargest)
