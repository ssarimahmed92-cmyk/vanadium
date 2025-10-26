x1 = eval(input("enter a first number: "))
x2 = eval(input("enter a second number: "))

operation = input("which operation do you want to perform: ")


if operation in ("*", "multiply"):
    print("product is ", x1 * x2)
elif operation in ("+", "add"):
    print("Sum is ", x1 + x2)
elif operation in ("/", "divide"):
    print("quotient is ", x1 / x2)
elif operation in ("-", "subtract"):
    print("difference is ", x1 - x2)
elif operation in ("%", "modulus"):
    print("remainder is ", x1 % x2)
else:
    print("invalid operator")
