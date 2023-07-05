mine_list = [ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]

#Create a function called mine_counter to count the number of # around each element
def mine_counter(row, column):
    mines = 0

    if (row > 0 and row < 4) and (column > 0 and column < 4):
        if mine_list[row -1][column -1] == "#":
            mines += 1
        if mine_list[row -1][column] == "#":
            mines += 1
        if mine_list[row -1][column +1] == "#":
            mines += 1
        if mine_list[row][column -1] == "#":
            mines += 1
        if mine_list[row][column +1] == "#":
            mines += 1
        if mine_list[row +1][column -1] == "#":
            mines += 1
        if mine_list[row +1][column ] == "#":
            mines += 1
        if mine_list[row +1][column +1] == "#":
            mines += 1
    
    elif (row == 0) and (column > 0 and column < 4):
        if mine_list[row][column -1] == "#":
            mines += 1
        if mine_list[row][column +1] == "#":
            mines += 1
        if mine_list[row +1][column -1] == "#":
            mines += 1
        if mine_list[row +1][column ] == "#":
            mines += 1
        if mine_list[row +1][column +1] == "#":
            mines += 1

    elif (row > 0 and row < 4) and (column == 0):
        if mine_list[row -1][column] == "#":
            mines += 1
        if mine_list[row -1][column +1] == "#":
            mines += 1
        if mine_list[row][column +1] == "#":
            mines += 1
        if mine_list[row +1][column ] == "#":
            mines += 1
        if mine_list[row +1][column +1] == "#":
            mines += 1

    elif (row == 4) and (column > 0 and column < 4):
        if mine_list[row][column -1] == "#":
            mines += 1
        if mine_list[row][column +1] == "#":
            mines += 1
        if mine_list[row -1][column -1] == "#":
            mines += 1
        if mine_list[row -1][column ] == "#":
            mines += 1
        if mine_list[row -1][column +1] == "#":
            mines += 1
    
    elif (row > 0 and row < 4) and ( column == 4):
        if mine_list[row -1][column -1] == "#":
            mines += 1
        if mine_list[row -1][column] == "#":
            mines += 1
        if mine_list[row][column] == "#":
            mines += 1
        if mine_list[row +1][column -1] == "#":
            mines += 1
        if mine_list[row +1][column ] == "#":
            mines += 1
    
    elif (row == 0) and (column == 0):
        if mine_list[row][column +1] == "#":
            mines += 1
        if mine_list[row +1][column ] == "#":
            mines += 1
        if mine_list[row +1][column +1] == "#":
            mines += 1
    
    elif (row == 0) and (column == 4):
        if mine_list[row][column -1] == "#":
            mines += 1
        if mine_list[row +1][column -1] == "#":
            mines += 1
        if mine_list[row +1][column ] == "#":
            mines += 1
        
    elif (row == 4) and (column == 0):
        if mine_list[row -1][column] == "#":
            mines += 1
        if mine_list[row -1][column +1] == "#":
            mines += 1
        if mine_list[row][column +1] == "#":
            mines += 1

    elif (row == 4) and (column == 4):
        if mine_list[row -1][column -1] == "#":
            mines += 1
        if mine_list[row -1][column] == "#":
            mines += 1
        if mine_list[row][column -1] == "#":
            mines += 1
        
    return mines

#Replace each '-' with the number of '#' found around the element
for row_index, row in enumerate(mine_list):
    for col_index, col in enumerate(mine_list[row_index]):
        if col == '-':
            mine_list[row_index][col_index] = mine_counter(row_index, col_index)

#Prints out the mine_list with the numbers of '#' around each element            
for row in mine_list:
    print(row)