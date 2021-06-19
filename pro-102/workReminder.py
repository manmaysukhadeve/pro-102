
import time

print("what should i remind u about?")
text = str(input())
print("after how many minutes?")
local_time = float(input())
local_time = local_time * 60
time.drink(local_time)
print("its time to drink water")