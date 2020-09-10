import random
# moves the trainer based on random positions and uses a random probability of capture to decide if pokemon are caught
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
    return (row,col),pokemon
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
last_report = 0
seed_value = 10*M + N
random.seed(seed_value)
#body of function, calls move trainer 250 times and prints one report every 20 steps
while step < 251:
    direction = random.randint(0, 3)
    cprobability = random.random()
    position,pokemon = move_trainer(position, bounds, cprobability)
    if pokemon == 1:
        pokemon_caught += 1
        last_report += 1
    if step%20 == 0 and step != 0:
        print("Time step {}: position {} pokemon caught since the last report {}".format(step,position,last_report))
        last_report = 0
    step += 1
print("After 250 time steps the trainer ended at position {} with {} pokemon.".format(position,pokemon_caught))