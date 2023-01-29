
print("Welcome")

# gets number of times to loop
loop_count = input("Number of lines:")

output = []

# 'gets coordinates via inputs
for list in range(int(loop_count)):
    x1 = input("Enter X1:")
    y1 = input("Enter Y1:")
    x2 = input("Enter X2:")
    y2 = input("Enter Y2:")

# finds slope
    dx = float(x1) - float(x2)
    dy = float(y1) - float(y2)
    m = float(dy) / float(dx)

# find y intercept
    b = int(y1) - (m * int(x1))

# create equation string
    equation = f"y = {m} x + {b}"
    output.append(equation)

# print all equations
print("---------------------------------------------")
print(output)