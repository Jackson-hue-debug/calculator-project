n = int(input("Enter the number of the points : "))
x_values = []
y_values = []
X_multiply_y = 0
X_multiply_x = 0
for i in range (n):
    x = float(input(f"Enter the value of x{i+1} : "))
    y = float(input(f"Enter the value of y{i+1} : "))
    x_values.append(x)
    y_values.append(y)
    X_multiply_x += x*x
    X_multiply_y += x*y
sum_of_x = sum(x_values)
sum_of_y = sum(y_values)
Numerator_1 = 0 
Numerator_1 = (n*X_multiply_y) - (sum_of_x*sum_of_y)
Denominator_1 = 0
Denominator_1 = (n*X_multiply_x) - (sum_of_x**2)
b = 0 
b = Numerator_1 / Denominator_1 
Numerator_2 = 0
Numerator_2 = (sum_of_y) - (b*sum_of_x)
Denominator_2 = 0
Denominator_2 = n
a = 0
a = Numerator_2 / Denominator_2 
y_of_xi = 0
Numerator_3 = 0
for i in range(n):
    y_of_xi = a + b * x_values[i]
    Numerator_3 +=( y_values[i] - y_of_xi)**2

RMSR = 0
RMSR = f"{((Numerator_3 /n)**0.5):.4f}"
print("Sum of x:",f"{sum_of_x:.1f}")
print("Sum of y:", f"{sum_of_y:.1f}")
print("Sum of x*y:",f"{X_multiply_y:.3f}")
print("Sum of x*x:",f"{X_multiply_x:.2f}")
print("Value of a : " ,f"{ a :.4f}" )
print("Value of b : " ,f"{ b :.3f}")
print("Value of y_of_xi : " , f"{y_of_xi:.3f}")
print("Value of EMSR : " , RMSR)
print("The equation of the line : y =",f"{a:.4f}","+",f"{b:.3f}","x +",RMSR)
print("The equation of the line : y =",f"{a:.4f}","+",f"{b:.3f}","x -",RMSR)