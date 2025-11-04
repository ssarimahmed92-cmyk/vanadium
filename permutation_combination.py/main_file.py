import permutation as p
import combination as c
n = int(input("Enter the total values: "))
r = int(input("Enter the selected values: "))
option = input("Enter p for Permutation or c for Combination: ")
if option == "p":
    print(p.per())
elif option == "c":
    print(c.com())
else:
    print("invalid option")