#Day 1 pt 2

#answer 236430480


data = []
goal = 2020 #final goal sum of problem


with open('input.txt', 'r') as file:
    data = [int(line.rstrip('\n')) for line in file]


for i in data:
    for j in data:
        for k in data:

            if i + j + k == goal:
                print(i)
                print(j)
                print(k)
                print(i * j * k)

