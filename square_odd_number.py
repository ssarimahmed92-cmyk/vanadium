start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
i = 0
if start == end:
    print("Start and ens must not be the same! ")
elif start > end:
    print("Start should be greater than end! ")
for start in range(start, end):
    if start % 2 != 0:
        i = start * start
        print(i)
    
    
