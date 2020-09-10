#Code has a turtle at position (200,200) fascing right, and moves him based on user commmands, jump, move, turn, sleep.
turns = 5
instructions = []
x,y = (200,200)
direction = 'right'
print("Turtle: ({0}, {1}) facing: {2}".format(x,y,direction))
#moves turtle in direction indicated, and checks that turtle is within bounds
def move(x,y,direction,amount):
    if direction == 'right':
        x += amount
    elif direction == 'left':
        x -= amount
    elif direction == 'up':
        y -= amount
    elif direction == 'down':
        y += amount    
    if x > 400:
        x = 400
    elif x < 0:
        x = 0
    if y > 400:
        y = 400
    elif y < 0:
        y = 0
    return x,y
def turn(direction):
    if direction == 'right':
        return 'up'
    elif direction == 'up':
        return 'left'
    elif direction == 'left':
        return 'down'
    else:
        return 'right'
while turns > 0:
    command = input("Command (move,jump,turn,sleep) => ")
    print(command)
    instructions.append(command)
    command = command.lower()
    turns -= 1
    if command == "move":
        x,y = move(x,y,direction,20)
    elif command == "jump":
        x,y = move(x,y,direction,50)
    elif command == "turn":
        direction = turn(direction)
    elif command == "sleep":
        print("Turtle falls asleep.")
        turns -= 1
        if turns > 0:
            print("Turtle: ({0}, {1}) facing: {2}\nTurtle is currently sleeping ... no command this turn.".format(x,y,direction))
    print("Turtle: ({0}, {1}) facing: {2}".format(x,y,direction))
print("\nAll commands entered:",instructions)
instructions.sort()
print("Sorted commands:",instructions)