def main():
    x =  get_student()
    for i in range(1, x, 1):
        x = x * i
    print(x)


def get_student():
    x = eval(input("Enter a number: "))
    return x


main()