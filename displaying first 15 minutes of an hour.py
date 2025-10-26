# Program to display the first 15 minutes of any given hour

# take hour input from user
hour = int(input("Enter the hour (0–23): "))
if hour <1 or hour > 23:
    print("invalid")
else:
    # print first 15 minutes
    for minute in range(16):   # 0 to 15
        print(f"{hour:02}:{minute:02}")