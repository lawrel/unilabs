import random
# moves the trainer based on random positions and uses a random probability of capture to decide if pokemon are caught
def move_trainer(position, bounds, prob):
    direction = random.randint(0,3)
    cprobability = random.random()
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
    if cprobability < p:
        pokemon = 1
    else:
        pokemon = 0
    return (row,col),pokemon
#runs one simulation, modifies the grid and returns pokemon caught and the modified grid
def run_one_simulation(grid):
    step = 1
    pokemon_caught = 0
    position = (M//2,N//2)
    while step < 251:
        position,pokemon = move_trainer(position, bounds, p)
        if pokemon == 1:
            pokemon_caught += 1
            grid[position[0]][position[1]] += 1
        step += 1
    return pokemon_caught,grid
def report(total,grid,sim):
    minimum = []
    maximum = []
    for i in range(len(grid)):
        minimum.append(min(grid[i]))
        maximum.append(max(grid[i]))
    minall = min(minimum)
    maxall = max(maximum)
    percentmin = round(minall/total*100,2)
    percentmax = round(maxall/total*100,2)
    for i in grid:
        print("")
        for x in i:
            print(" {:3d}".format(x),end = "")
    print("\n\nTotal pokemon caught is {}".format(total))
    print("Minimum pokemon caught was {} in simulation {}".format(min(sim),sim.index(min(sim))+1))
    print("Maximum pokemon caught was {} in simulation {}".format(max(sim),sim.index(max(sim))+1))
    print("Max number of pokemon caught on a space is {} which was {}% of all pokemon caught".format(maxall,percentmax))
    print("Min number of pokemon caught on a space is {} which was {}% of all pokemon caught".format(minall,percentmin)) 
#assignments
M = int(input("Enter the integer number of rows => "))
print(M)
N = int(input("Enter the integer number of cols => "))
print(N)
p = float(input("Enter the probability of finding a pokemon (<= 1.0) => "))
print(p)
sim = int(input("Enter the number of simulations to run => "))
print(sim)
bounds = (M,N)
seed_value = 10*M + N
random.seed(seed_value)
count_grid = []
total = 0
sim_pcount = []
pokemon = 0
for i in range(M):
    count_grid.append( [0]*N )
#body of code - this part tests if probability is zero to avoid a divide by zero error in the calculation of report function
if p == 0:
    for i in count_grid:
        print("")
        for x in i:
            print(" {:3d}".format(x),end = "")    
    print("\n\nTotal pokemon caught is 0\nMinimum pokemon caught was 0 in simulation 1")
    print("Maximum pokemon caught was 0 in simulation 1")
    print("Max number of pokemon caught on a space is 0")
    print("Min number of pokemon caught on a space is 0")
else: 
    while sim > 0:
        pokemon_caught,count_grid = run_one_simulation(count_grid)
        total += pokemon_caught
        sim_pcount.append(pokemon_caught)
        sim -= 1
    report(total, count_grid, sim_pcount)
