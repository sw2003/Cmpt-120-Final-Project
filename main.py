total_points = 0
total_game_counter = 1

table_data = {
    "row_0": [],
    "row_1": [],
    "row_2": []
}

def get_initial_data(file):
    file.readline()
    counter = 0
    for i in file:
        data_string = i
        data_list = i.strip("\n ").split(",") 
        table_data["row_" + str(counter)] = data_list

        counter += 1

#Prints out row / col values
def display_table(is_initial):

    print("\nThe board is")
    print("-------------\n")
    if is_initial:
        print("(initial board)")
    else:
        print("(after user played)")
    print("\n")
    print(" "*11 + " Col 0   Col 1   Col 2") 
    for i in range(3): 
        row_data = table_data["row_" +str(i)]
        row_data_col_1 = row_data[0] 
        row_data_col_2 = row_data[1]
        row_data_col_3 = row_data[2] 
        print("Row " + str(i) + " "*9 + row_data_col_1 + " "*7 + row_data_col_2 + " "*7 + row_data_col_3)
        print("")
    if is_initial:
        #print("\n")
        print("You will have up to 4 turns")
        print("\n"*2)

##Game logic
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

start_game = input("Would you like to play (y/n) ==> ")
play_game = False

if start_game == "y":
    play_game = True
    print("\nGame: {}\n========".format(total_game_counter))
else:
    play_game = False

game_style = input("What style would you want to play ('SOLO or 'AI'): ==> ")
print("\n")
initial_board = input("Which initial board do you want to use (0, 1, 2, or 3): ==> ") 

file = open("board{}.csv".format(initial_board))

if play_game == True:
    while play_game == True:
        get_initial_data(file)
        display_table(True)

        for i in range(4,0,-1):
            
            print("You have {} turns left...\n".format(i))
            print("User, where do you want your value? (row 99 - no more turns)\n")
            row_input = input("row? (>= 0 and <= 2) ==> ")
            print("")
            col_input = input("col? (>=0 and <= 2) ==> ")
            print("")
            val_input = input("value (0 to 50): ==> ")

            #print("The board is\n" + "-"*13)

            ##update the dictionary
            table_data["row_" + str(row_input)][int(col_input)] = val_input

            display_table(False)

        ## Calculates players points 
        ## Determines row sum 
        ## Appends column sums into array
        sum_even = 0
        win = False
        even_rows = False
        odd_cols = False

        col_sum = [
            [], # <-- first column 
            [], # <-- second column
            [] # <-- third column
        ]

        for i in table_data:
            row_sum = 0
            index = 0
            for v in table_data[i]:
                number = int(v) 

                col_sum[index].append(number)

                row_sum += number
                if number % 2 == 0:
                    sum_even += number
                #elif number % 2 == 1:

                index += 1
            if row_sum % 2 == 0: #<-- determines if the sum of a row is a even number
                even_rows = True
            else: 
                even_rows = False

        #Determining if column sum is a odd number
        for col_list in col_sum:
            sum = 0

            for i in col_list:
                sum += i

            if sum % 2 != 0:
                odd_cols = True
            else: 
                odd_cols = False
            
        #Gives user their points
        points = sum_even / 4
        print("You reached the maximum turns possible, the game is over! \n")
        print("Totals for this game\n" + "-"*13 + "\n"*2)
        print("The points resulting from this game are {}".format(points))
        print("Points are calculated as:")
        print("  the sum of all even values in the board")
        print("  divided by the number of turns played(4)\n")

        #Tells user if they have won and rewards or punishes player
        if odd_cols and even_rows:
            total_points += points
            print("Congratulations, User, you won this game") 
            print("All rows add to even numbers and all cols add to odd numbers") 
            print("You will be added {} points from your total".format(points))
            print("Your points so far are {}".format(total_points))

        else:
            total_points -= points

            print("So sorry, User, you lost this game!")
            print("Not all rows add to even numbers or not all cols add to odd numbers!")
            print("You will be subtracted {} points from your total".format(points))
            print("Your points so far are {}".format(total_points))

        print("\n"*4)

        #asks player if they want to play again

        continue_playing = input("Would you like to play another game? (y/n) ==> ")
        if continue_playing != "y":
            play_game = False
        else:
            total_game_counter += 1
            print("\n"*2)
            file.seek(1)




