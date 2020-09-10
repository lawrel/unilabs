import random
def move_trainer(position, bounds, prob):
    row,col = position
    M,N = bounds
    if direction == 2:
        col += 1
    elif direction == 3:
        col -= 1
    elif direction == 0:
        row -= 1
    elif direction == 1:
        row += 1   
    if row > M-1:
        row = M-1
    elif row < 0:
        row = 0
    if col > N-1:
        col = N-1
    elif col < 0:
        col = 0
    if prob < p:
        pokemon = 1
    else:
        pokemon = 0
    return row,col,pokemon
#assignments
M = int(input("Enter the integer number of rows => "))
print(M)
N = int(input("Enter the integer number of cols => "))
print(N)
p = float(input("Enter the probability of finding a pokemon (<= 1.0) => "))
print(p)
position = (M//2,N//2)
bounds = (M,N)
step = 1
pokemon_caught = 0
seed_value = 10*M + N
random.seed(seed_value)
grid = []
for i in range(M):
    grid.append( [0]*N )
#body of function
while step < 251:
    direction = random.randint(0, 3)
    cprobability = random.random()
    row,col,pokemon = move_trainer(position, bounds, cprobability)
    if pokemon == 1:
        pokemon_caught += 1
        grid[row][col] += 1
    step += 1
print(grid)
print(pokemon_caught)