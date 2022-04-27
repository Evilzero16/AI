import numpy as np
def find_neighbours(landscape, current_state):
    neighbours = []
    i, j = current_state
    
    if i != 0 and j != 0:
        neighbours.append(landscape[i-1][j-1])
        neighbours.append(landscape[i-1][j])
        neighbours.append(landscape[i-1][j+1])
        neighbours.append(landscape[i][j-1])
        neighbours.append(landscape[i][j+1])
        neighbours.append(landscape[i+1][j-1])
        neighbours.append(landscape[i+1][j])
        neighbours.append(landscape[i+1][j+1])
    
    elif i == 0 and j == 0:
        neighbours.append(landscape[i+1][j+1])
        neighbours.append(landscape[i+1][j])
        neighbours.append(landscape[i][j+1])
    
    elif i == 0:
        neighbours.append(landscape[i+1][j+1])
        neighbours.append(landscape[i+1][j])
        neighbours.append(landscape[i][j+1])
        neighbours.append(landscape[i+1][j-1])
        neighbours.append(landscape[i][j-1])
        
    elif j == 1:
        neighbours.append(landscape[i+1][j+1])
        neighbours.append(landscape[i+1][j])
        neighbours.append(landscape[i][j+1])
        neighbours.append(landscape[i-1][j])
        neighbours.append(landscape[i-1][j+1])

def find_neighbours(landscape, state):
    neighbours = []
    dim = landscape.shape
    
    # left neighbour
    if state[0] != 0:
        neighbours.append((state[0] - 1, state[1]))
    
    # right neighbour
    if state[0] != dim[0] - 1:
        neighbours.append((state[0] + 1, state[1]))
    
    # top neighbour
    if state[1] != 0:
        neighbours.append((state[0], state[1] - 1))
    
    # bottom neighbour
    if state[1] != dim[1] - 1:
        neighbours.append((state[0], state[1] + 1))
    
    # top left
    if state[0] != 0 and state[1] != 0:
        neighbours.append((state[0] - 1, state[1] - 1))
    
    # bottom left
    if state[0] != 0 and state[1] != dim[1] - 1:
        neighbours.append((state[0] - 1, state[1] + 1))
    
    # top right
    if state[0] != dim[0] - 1 and state[1] != 0:
        neighbours.append((state[0] + 1, state[1] - 1))
    
    # bottom right
    if state[0] != dim[0] - 1 and state[1] != dim[1] - 1:
        neighbours.append((state[0] + 1, state[1] + 1))
    
    return neighbours

def hill_climb(landscape, current_state):
    neighbours = find_neighbours(landscape, current_state)
    for neighbour in neighbours:
        ascended = False
        next_state = current_state
        for neighbour in neighbours: #Find the neighbour with the greatest value
            if landscape[neighbour[0]][neighbour[1]] > landscape[next_state[0]][next_state[1]]:
                next_state = neighbour
                ascended = True
        return ascended, next_state

landscape = np.random.randint(1, high=50, size=(10, 10))
print(landscape)
start_state = (3, 6) # matrix index coordinates
current_state = start_state
count = 1
ascending = True
while ascending:
    print("\nStep #", count)
    print("Current state coordinates: ", current_state)
    print("Current state value: ", landscape[current_state[0]][current_state[1]])
    count += 1
    ascending, current_state = hill_climb(landscape, current_state)
print("\nStep #", count)
print("Optimization objective reached.")
print("Final state coordinates: ", current_state)
print("Final state value: ", landscape[current_state[0]][current_state[1]])
