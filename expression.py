# Expression Solver Program

def solve_expression(a, b):
    return (a - b) + (a * b)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

result = solve_expression(a, b)

print("The result of (a - b) + (a * b) is: " + str(result))
