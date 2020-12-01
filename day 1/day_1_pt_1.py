#Day 1 pt 1

#final answer: 974304

data = []
goal = 2020 #final goal sum of problem


with open('input.txt', 'r') as file:
    data = [int(line.rstrip('\n')) for line in file]

data.sort()

counter_1 = 0
counter_2 = len(data) - 1

current_sum = 0

while current_sum != goal and counter_1 != counter_2:
    current_sum = data[counter_1] + data[counter_2]

    if current_sum < goal:
        counter_1 += 1
    elif current_sum > goal:
        counter_2 -= 1



print(f"Value 1: {data[counter_1]}")
print(f"Value 2: {data[counter_2]}")

print(f"Product: {data[counter_1] *data[counter_2]}") 








    
