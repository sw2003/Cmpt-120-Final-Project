def give_start_instructions():
    print(' Dear player! Welcome to the "Even/Odd Colorful Graphical" game ')
    print(" ============================================================== ")
    print("")
    print("With this system you will be able to play as many games as you want!")
    print("The objective of this game is that rows in board")
    print("add to an even number and all columns in the board add to an odd number")
    print("For each game:")
    print("- you will be able to choose to play 'SOLO' or against the computer ('AI')")
    print("- you will be able to choose an initial board")
    print("- at the end of each game you will win (or lose) points, and")
    print("- you will see a graphical representation of some game related values.")
    print("Enjoy!")
    print("\n"*2)

def request_user_actions(game_number):
    start = ""
    if game_number == 1:
        start = input("Would you like to play (y/n) ==> ")
        start = start.strip().lower() 
    if start == "y" or game_number != 1:
        user_actions = []

        print("\nGame: {}\n========".format(game_number))

        input_type = False
        while input_type == False:
            accepted_initial_board_inputs = ["0", "1", "2", "3"]

            game_style = input("What style would you want to play ('SOLO or 'AI'): ==> ")
            initial_board = input("\nWhich initial board do you want to use (0, 1, 2, or 3): ==> ") 

            game_style = game_style.strip().lower()
            initial_board = initial_board.strip()

            if game_style == "solo" or game_style == "ai":
                if initial_board in accepted_initial_board_inputs:
                    input_type = True
                    user_actions.append(game_style)
                    user_actions.append(initial_board)
                    #user_actions[game_style, initial_board]

            if input_type == False:
                print("\nPlease correctly type the inputs\n")

        return user_actions
        
    else:
        print("\nuser has decided not to play the game\n")
        return False

def display_board(table_data, display_code, ai_data):
    print("\nThe board is\n" + "-"*10)
    if display_code == "initial":
        print("\n(initial board)\n")
    elif display_code == "after_user_played":
        print("\n(after user played)\n")
    elif display_code == "ai":
        print("\n(after computer played in (row, col) {} with value: {})\n".format(ai_data[0], ai_data[1]))

    base_row_string = " "*12
    row_length = len(table_data["row_0"])
    for i in range(row_length):
        base_row_string += "Col {}   ".format(i)

    print(base_row_string)
    #print(" "*11 + " Col 0   Col 1   Col 2") 

    for i in range(len(table_data["row_0"])): 
        row_data = table_data["row_" +str(i)]

        base_string = "Row " + str(i) + " "*9

        for j in range(0, len(table_data["row_0"])):
            base_string += row_data[j] + " "*7 

        print(base_string + "\n")

        #row_data_col_1 = row_data[0] 
        #row_data_col_2 = row_data[1]
        #row_data_col_3 = row_data[2] 
        #print("Row " + str(i) + " "*9 + row_data_col_1 + " "*7 + row_data_col_2 + " "*7 + row_data_col_3 + "\n")

    turns = (len(table_data["row_0"])**2 ) / 2
    turns = int(turns)

    if display_code == "initial":
        print("You will have up to {} turns".format(turns) + "\n"*2)
        print("You have {} turns left...\n".format(turns))

def check_game_result(data):
    win = False

    col_data = [
        [],
        [],
        [],
        []
    ]

    row_even = False
    col_odd = False

    for k in data:
        counter = 0
        sum = 0
        for i in data[k]:            
            i = int(i)
            sum += i

            col_data[counter].append(i) 
            counter += 1 

        if sum % 2 == 0:
            row_even = True
        else:
            row_even = False
            break
            
    for i in col_data:
        sum = 0 
        for j in i:
            j = int(j) 
            sum += j
        if sum % 2 != 0:
            col_odd = True
        else:
            col_odd = False
            break

    if row_even == True and col_odd == True:
        return True
    else:
        return win

def calculate_game_points(turns, data):
    sum = 0
    for k in data:
        for i in data[k]:
            i = int(i) 
            if i % 2 == 0:
                sum += i
    
    points = sum/turns
    points = int(points)
    return points



def display_game_result(points, game_result, total_points):
    print("\nTotals for this game")
    print("--------------------\n")
    print("The points resulting from this game are: {}".format(points))
    print("Points were calculated as:")
    print("  the sum of all even values in the board")
    print("  divided by the number of turns played(2)")

    if game_result:
        print("Congratulations, User you won this game!")
        print("All rows add to even numbers or not all cols add to odd numbers!")
        print("You will be added {} points from your total".format(points))
        print("Your points so far are {}".format(total_points))
    else:
        print("\nSo sorry, User you lost this game!")
        print("Not all rows add to even numbers or not all cols add to odd numbers!")
        print("You will be substracted {} points from your total".format(points))
        print("Your points so far are: {}".format(total_points))

def display_totals(user_stats):
    print("\nTOTALS ALL GAMES")
    print("Total points user in all games: {}".format(user_stats["total_points"]))
    print("Total games the user won: {}".format(user_stats["plr_wins"]))
    print("Total games the computer won: {}".format(user_stats["comp_wins"]))



        
    




    

        


  
