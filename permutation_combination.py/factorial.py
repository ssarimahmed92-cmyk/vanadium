def fact(x):
        if x == 0 or x == 1:
            return 1
        else:
            for i in range(1, x):
                x = x * i
            return x
            print(x)
    