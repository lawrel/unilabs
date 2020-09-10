def ok_to_add(row, column, number):
    number = str(number)
    for x in range(len(bd)): 
        for y in range(len(bd[x])):
            if(bd[row][y] == number):
                return False
            elif(bd[x][column] == number):
                return False
            if(row in [0, 1, 2] and x in [0, 1, 2]):
                if(column in [0, 1, 2] and y in [0, 1, 2]):
                    if(number == bd[x][y]):
                        return False                    
                elif(column in [3, 4, 5] and y in [3, 4, 5]):
                    if(number == bd[x][y]):
                        return False                      
                elif(column in [6, 7, 8] and y in [6, 7, 8]):
                    if(number == bd[x][y]):
                        return False
            elif(row in [3, 4, 5] and x in [3, 4, 5]):
                if(column in [0, 1, 2] and y in [0, 1, 2]):
                    if(number == bd[x][y]):
                        return False                    
                elif(column in [3, 4, 5] and y in [3, 4, 5]):
                    if(number == bd[x][y]):
                        return False                      
                elif(column in [6, 7, 8] and y in [6, 7, 8]):
                    if(number == bd[x][y]):
                        return False
            elif(row in [6, 7, 8] and x in [6, 7, 8]):
                if(column in [0, 1, 2] and y in [0, 1, 2]):
                    if(number == bd[x][y]):
                        return False                    
                elif(column in [3, 4, 5] and y in [3, 4, 5]):
                    if(number == bd[x][y]):
                        return False                      
                elif(column in [6, 7, 8] and y in [6, 7, 8]):
                    if(number == bd[x][y]):
                        return False
    return True


bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

for x in range(len(bd)):
    if(x == 0 or x == 3 or x == 6):
        print('-' * 25)
    for y in range(len(bd[x])):
        if( y == 0 or y == 3 or y == 6):
            print('|', end=' ')
        print(bd[x][y], end=' ')
        if (y == 8):
            print('|')
    if(x == 8):
        print('-' * 25)
        
x1 = int(input('Enter a row from 0 to 8: '))
y1 = int(input('Enter a column from 0 to 8: '))
numb = int(input('Enter the number from 0 to 9: '))

print(ok_to_add(x1, y1, numb))
