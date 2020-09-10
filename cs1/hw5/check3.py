#lab06_util import for reading 
import lab06_util 
        
# checks if ok to add number 
def ok_to_add(row, column, number, board):
    number = str(number)
    for x in range(len(board)): 
        for y in range(len(board[x])):
            if(board[row][y] == number):
                return False
            elif(board[x][column] == number):
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

def verify_board(board):
    for x in range(len(bd)): 
        for y in range(len(bd[x])):
            if bd[x][y] in ['.'] or not ok_to_add(x,y,bd[x][y],bd):
                return True
    return False
    

board_file = input('Enter board file: ')
bd = lab06_util.read_sudoku(board_file)
complete = False

def print_sudoku(board):
    for x in range(len(board)):
        if(x == 0 or x == 3 or x == 6):
            print('-' * 25)
        for y in range(len(board[x])):
            if( y == 0 or y == 3 or y == 6):
                print('|', end=' ')
                    
            print(board[x][y], end=' ')
                
            if (y == 8):
                print('|')
        if(x == 8):
            print('-' * 25)              

while not complete:
    print_sudoku(bd)
    if(verify_board(bd)):  
        x1 = int(input('Enter a row from 0 to 8: '))
        y1 = int(input('Enter a column from 0 to 8: '))
        numb = int(input('Enter the number from 0 to 9: '))
        if(ok_to_add(x1, y1, numb, bd)):
            bd[x1][y1] = str(numb)
        else:
            print('incorrect')
    else:
        complete = True
        print("Has been solved.")
    
    
    
        
    


