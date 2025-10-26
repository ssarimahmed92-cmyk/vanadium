import time
import os

frames = ["(-_-)", "(o_o)", "(O_O)", "(o_o)", "(-_-)"]

for i in range(10):
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print(frame)
        time.sleep(0.3)
