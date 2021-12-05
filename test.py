import helper
import random
import matplotlib.pyplot as plt
import datetime as dt

table_data = {
    "row_0": [],
    "row_1": [],
    "row_2": [],
    "row_3": [], 
}

user_stats = {
    "total_points": 0,
    "plr_wins": 0,
    "comp_wins": 0,
    "player_values": [],
    "ai_values": [],
    "turn_times": [] 

}

def main(game_number):

    user_stats["player_values"] = []
    user_stats["turn_times"] = []
    user_stats["ai_values"] = []

    if game_number == 1:
        helper.give_start_instructions()
    preferences = helper.request_user_actions(game_number)
    if preferences != False:
        game_style = preferences[0] 
        
        initial_board_number = preferences[1]
        file = open("board{}.csv".format(initial_board_number))

        store_initial_file_data(file)

        helper.display_board(table_data, "initial", "")

        #Updates board with player input
        def finish_game(turns, is_early, early_difference):
            game_result = helper.check_game_result(table_data) 
            
            current_game_points = helper.calculate_game_points(turns, table_data)
            if game_result:
                user_stats["plr_wins"] += 1
                user_stats["total_points"] += current_game_points
            else:
                user_stats["comp_wins"] += 1
                user_stats["total_points"] -= current_game_points

            helper.display_game_result(current_game_points, game_result, user_stats["total_points"]) 

            x_axis = []

            if is_early:
                turns = early_difference
            
            for i in range(turns):
                base_string = "Turn {}".format(i+1)
                x_axis.append(base_string)
            

            plt.plot(x_axis, user_stats["player_values"],"s-", label = "player values")
            plt.plot(x_axis, user_stats["turn_times"],"s-", label = "time per turn")

            if len(user_stats["ai_values"]) != 0:
                plt.plot(x_axis, user_stats["ai_values"], "s-", label = "computer values")

            plt.legend()
            plt.show()
            
        row_length = len(table_data["row_0"])
        turns = ((row_length**2) / 2)
        turns = int(turns)

        correct_inputs = []
        for j in range(row_length):
            j = str(j)
            correct_inputs.append(j)

        correct_inputs.append("99")

        for i in range(turns,0,-1):
            time_1 = dt.datetime.now()
            row_input_correct = False
            col_input_correct = False
            val_input_correct = False
            print("User, where do you want your value? (row 99 - no more turns)\n")
            row_input = None
            while row_input_correct == False:
                

                #print("User, where do you want your value? (row 99 - no more turns)\n")
                user_input = input("row? (>= 0 and <= {}) ==> ".format(row_length-1))
                user_input = user_input.strip()

                if user_input in correct_inputs:
                    row_input_correct = True
                    row_input = user_input
                else:
                    print("\nUser, correct row values are from 0 to {}\n".format(row_length-1))
   
            if row_input != "99":
                while col_input_correct == False or val_input_correct == False:
                    col_input = input("\ncol? (>=0 and <= {}) ==> ".format(row_length-1))
                    col_input = col_input.strip()
                    val_input = input("\nvalue (0 to 50): ==> ")
                    val_input = val_input.strip()

                    for k in range(51):
                        k = str(k) 
                        if val_input == k:
                            val_input_correct = True

                    if col_input in correct_inputs:
                        col_input_correct = True

                    if col_input_correct == False or val_input_correct == False:
                        print("\nCorrect row values between 0 and {} and values between 0 and 50".format(row_length-1)) 
                    

                table_data["row_" + str(row_input)][int(col_input)] = val_input
                user_stats["player_values"].append(int(val_input))
            else:
                print("Since you didn't want to update more values, the game is over\n")

                finish_game(i, True, turns-i)
                break

            helper.display_board(table_data, "after_user_played", "")

            time_2 = dt.datetime.now()
            difference = (time_2-time_1).total_seconds()
            user_stats["turn_times"].append(difference)

            if i != 1:
                if game_style == "ai":
                    ai_move()

                print("\nYou have {} turns left...\n".format(int(i)-1))
            elif i == 1:
                if game_style == "ai":
                    ai_move()
                print("\nYou have reached the maximum turns possible, the game is over!" )
                finish_game(turns, False, 0)

        play_again = input("\nWould you like to play another game (y/n): ==> ")
        play_again = play_again.strip().lower()
        if play_again == "y":
            main(game_number+1) 
        else:
            helper.display_totals(user_stats)
            return

                
#Updates dictionary with values from csv file
def store_initial_file_data(file):
    file.readline()
    counter = 0
    for i in file:
        data_list = i.strip("\n ").split(",") 
        table_data["row_" + str(counter)] = data_list

        counter += 1

def ai_move():
    print("\nThe computer will play now!") 
    input("\nHit return to continue") 

    table_parameters = len(table_data["row_0"]) -1 
    rand_int_row = random.randint(0, table_parameters)
    rand_int_col = random.randint(0, table_parameters) 
    rand_value = random.randint(0, 50) 
    rand_value = str(rand_value)

    table_data["row_{}".format(rand_int_row)][rand_int_col] = rand_value
    user_stats["ai_values"].append(int(rand_value))

    ai_string = "({},{})".format(rand_int_row, rand_int_col)

    helper.display_board(table_data, "ai", [ai_string, rand_value])

main(1)




