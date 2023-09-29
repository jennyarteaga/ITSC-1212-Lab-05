# Problem 3

user_input = input("Enter a positive number: ")
n = int(user_input)

factorial = 1
for fact in range(n, 0, -1):
    factorial = factorial * fact
    

print(factorial)


