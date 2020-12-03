#day 1 pt 1

#final answer 220

with open('input.txt', 'r') as file:
    layers = [line.rstrip('\n') for line in file]

#print(layers)

length = len(layers[0])


right = 3
down = 1

trees = 0

for i, layer in enumerate(layers):
    x = (right * i) % length

    if layer[x] == '#':
        trees += 1

print(trees)
    

    

    
    


