#day 1 pt 2

#final answer 2138320800

with open('input.txt', 'r') as file:
    layers = [line.rstrip('\n') for line in file]

#print(layers)

width = len(layers[0])

height = len(layers)

right = [1, 3, 5, 7, 1]
down  = [1, 1, 1, 1, 2]

trees = []


for i in range(len(right)):

    x = right[i]
    y = down[i]

    tree_count = 0

    for count, layer in enumerate(range(0, height, y)):


        current_layer = layers[layer]

        x_coord = (x * count) % width
        
        if layers[layer][x_coord] == '#':
            tree_count += 1

    trees.append(tree_count)
            

print(trees)

total = 1

for tree in trees:
    total *= tree

print(f"Total: {total}")
    

    

    
