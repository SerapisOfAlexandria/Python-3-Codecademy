print("Please enter values for X and Y")
print("-------------------------------")
print("Enter x: ")
x = input()
print("Enter y: ")
y = input()
print("Please choose an arithmetic operation\nA) Addition(+)\nB) Substraction(-)\nC) Multiplication(*)\nD) Division(/)\nC) Check Remainder(%)")
arithmetic_operation = input(str())
if arithmetic_operation == "A":
	print(int(x) + int(y))
elif arithmetic_operation == "B":
	print(int(x) - int(y))
elif arithmetic_operation == "C":
	print(int(x) * int(y))
elif arithmetic_operation == "D":
	print(float(x) / float(y))
elif arithmetic_operation == "E":
	print(int(x) % int(y))






