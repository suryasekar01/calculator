def add(va1, va2):
	return va1 + va2
def subtract(va1, va2):
	return va1 - va2
def multiply(va1, va2):
	return va1 * va2
def divide(va1, va2):
	return va1 / va2
print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")
select = int(input("Select operations form 1, 2, 3, 4 :"))

va_1 = int(input("Enter first number: "))
va_2 = int(input("Enter second number: "))

if select == 1:
	print(va_1, "+", va_2, "=",
					add(va_1, va_2))

elif select == 2:
	print(va_1, "-", va_2, "=",
					subtract(va_1, va_2))

elif select == 3:
	print(va_1, "*", va_2, "=",
					multiply(va_1, va_2))

elif select == 4:
	print(va_1, "/", va_2, "=",
					divide(va_1, va_2))
else:
	print("Invalid input")
