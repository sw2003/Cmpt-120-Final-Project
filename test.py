import helper

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
}

def main(game_number):
    if game_number == 1:
        helper.give_start_instructions()
    preferences = helper.request_user_actions(game_number)
    if preferences != False:
        game_style = preferences[0] 
        if game_style == "solo":
            initial_board_number = preferences[1]
            is_initial_bool = True
            file = open("board{}.csv".format(initial_board_number))

            store_initial_file_data(file)

            helper.display_board(table_data, is_initial_bool)

            #Updates board with player input
            def finish_game(turns):
                game_result = helper.check_game_result(table_data) 
                
                current_game_points = helper.calculate_game_points(turns, table_data)
                if game_result:
                    user_stats["plr_wins"] += 1
                    user_stats["total_points"] += current_game_points
                else:
                    user_stats["comp_wins"] += 1
                    user_stats["total_points"] -= current_game_points

                helper.display_game_result(current_game_points, game_result, user_stats["total_points"]) 
                
            for i in range(4,0,-1):
                print("User, where do you want your value? (row 99 - no more turns)\n")
                row_input = input("row? (>= 0 and <= 2) ==> ")
                if row_input != "99":
                    col_input = input("\ncol? (>=0 and <= 2) ==> ")
                    val_input = input("\nvalue (0 to 50): ==> ")
                    table_data["row_" + str(row_input)][int(col_input)] = val_input
                else:
                    print("Since you didn't want to update more values, the game is over\n")
                    finish_game(i)
                    break

                helper.display_board(table_data, False)

                if i != 1:
                    print("\nYou have {} turns left...\n".format(int(i)-1))
                elif i == 1:
                    print("\nYou have reached the maximum turns possible, the game is over!" )
                    finish_game(4)

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

main(1)




