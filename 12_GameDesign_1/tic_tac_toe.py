grid = [
    ["1", "2", "3", "4", "5", "6", "7"],     # [R0C0, R0C1, R0C2]
    ["-", "-", "-", "-", "-", "-", "-"],     # [R1C0, R1C1, R1C2]
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"]  # [R2C0, R2C1, R2C2]
]

current_piece = "R"

def print_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col != 6:
                print(grid[row][col], end="  ")            
            else:
                print(grid[row][col])
                print()

def is_bad_num_string(choice : str):
    if (choice.isnumeric() and int(choice) >= 1 and int(choice) <= 9):
        return False
    return True
                
def is_bad_choice(choice : str):
    if(choice.__eq__("STOP")):
        return False
    return is_bad_num_string(choice)

def get_row(grid_spot):
    if grid_spot == 1 or grid_spot == 2 or grid_spot == 3:
        return 0
    elif grid_spot == 4 or grid_spot == 5 or grid_spot == 6:
        return 1
    else:
        return 2    

def get_col(grid_spot):
    if grid_spot == 1 or grid_spot == 4 or grid_spot == 7:
        return 0
    elif grid_spot == 2 or grid_spot == 5 or grid_spot == 8:
        return 1
    else:
        return 2
    
def place_piece(grid_spot : int):
    global last_row
    global last_col
    global remaining_spots
    while (True):
        row = 5
        while (row >= 0):
            if grid[row][col].__eq__("-"):
                grid[row][col] = current_piece
                last_row = row
                last_col = col
                remaining_spots -= 1
                break
            else:
                row -= 1
        if row != -1:
            break
        else:
            user_choice = ""
            while (is_bad_num_string(user_choice)):
                user_choice = input(
                    "Enter a different number (0-6) where to drop the piece: ")
            col = int(user_choice)

def check_row():
    first_list = [last_col, last_col + 1, last_col + 2, last_col + 3]
    second_list = [last_col - 1, last_col, last_col + 1, last_col + 2]
    third_list = [last_col - 2, last_col - 1, last_col, last_col + 1]
    fourth_list = [last_col - 3, last_col - 2, last_col - 1, last_col]
    if(first_list[0] >= 0 and first_list[0] < 7 and first_list[3] >= 0 and first_list[3] < 7):
        one = grid[last_row][first_list[0]]
        two = grid[last_row][first_list[1]]
        three = grid[last_row][first_list[2]]
        four = grid[last_row][first_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    if (second_list[0] >= 0 and second_list[0] < 7 and second_list[3] >= 0 and second_list[3] < 7):
        one = grid[last_row][second_list[0]]
        two = grid[last_row][second_list[1]]
        three = grid[last_row][second_list[2]]
        four = grid[last_row][second_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    if (third_list[0] >= 0 and third_list[0] < 7 and third_list[3] >= 0 and third_list[3] < 7):
        one = grid[last_row][third_list[0]]
        two = grid[last_row][third_list[1]]
        three = grid[last_row][third_list[2]]
        four = grid[last_row][third_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    if (fourth_list[0] >= 0 and fourth_list[0] < 7 and fourth_list[3] >= 0 and fourth_list[3] < 7):
        one = grid[last_row][fourth_list[0]]
        two = grid[last_row][fourth_list[1]]
        three = grid[last_row][fourth_list[2]]
        four = grid[last_row][fourth_list[3]]
        if one.__eq__(two) and two.__eq__(three) and three.__eq__(four):
            return True
    return False
 
def check_col():
    return False

def check_left_diag():
    return False

def check_right_diag():
    return False

def check_draw(): 
    return remaining_spots == 0

def check_game_over():
    if check_row():
        print(current_piece + " wins!")
        return True
    elif check_col():
        print(current_piece + " wins!")
        return True
    elif check_left_diag():
        print(current_piece + " wins!")
        return True
    elif check_right_diag():
        print(current_piece + " wins!")
        return True
    elif check_draw():
        print("The Game Ends in a Draw!")
        return True
    else:
        return False

def game_loop():
    global current_piece
    print("Welcome to TIC TAC TOE")
    user_choice = ""
    while(True):
        print_grid()
        while(is_bad_choice(user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (1-9) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        grid_spot = int(user_choice)
        place_piece(grid_spot)
        if(check_game_over()):
            print_grid()
            break
        current_piece = "Y" if current_piece.__eq__("R") else "R"
        user_choice = ""
    print("GAME OVER")
        
game_loop()