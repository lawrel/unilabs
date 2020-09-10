# a code that plays pokemon go with the ability to move 1 space at a time, caputure pokemon from a list, and print a list of remaining pokemon
import hw4_util
def print_pokemon(pokemon,locations):
    print("Current pokemon:")
    for i in range(len(pokemon)):
        print(" "*5+"{} at {}".format(pokemon[i],locations[i]))
    print("")
def move(x,y,direction,amount):
    if direction == 'E':
        x += amount
    elif direction == 'W':
        x -= amount
    elif direction == 'N':
        y -= amount
    elif direction == 'S':
        y += amount    
    if x > 10:
        x = 10
    elif x < 0:
        x = 0
    if y > 10:
        y = 10
    elif y < 0:
        y = 0
    return x,y
x,y = (5,5)
end = False
turn = -1
pokemon, locations = hw4_util.read_pokemon()
print_pokemon(pokemon,locations)
while end == False:
    command = input("N,S,E,W to move, 'print' to list, or 'end' to stop ==> ")
    print(command)
    command = command.upper()
    if command == "END":
        end = True
    elif (command == "N") or (command == 'W') or (command == 'E') or (command == 'S'):
        turn += 1
        x,y = move(x,y,command,1)
        print("Currently at ({}, {})".format(x,y))
        if (x,y) in locations:
            index = locations.index((x,y))
            print("You capture a {} on turn {}".format(pokemon[index],turn))
            locations.pop(index)
            pokemon.pop(index)
    elif command == 'PRINT':
        turn += 1
        print_pokemon(pokemon,locations)
        print("Currently at ({}, {})".format(x,y))
    else:
        turn += 1
        print("Currently at ({}, {})".format(x,y))