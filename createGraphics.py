#Even Odd Graphical Game
#Authors: Sam Wen, Jasper Song
#December 5th

import matplotlib.pyplot as plt

def create_graph(x_axis, player_values, time, ai_values):
    plt.plot(x_axis, player_values,"s-", label = "player values")
    plt.plot(x_axis, time ,"s-", label = "time per turn")

    if ai_values != None:
        plt.plot(x_axis, ai_values, "s-",label = "computer values")

    plt.legend()
    plt.savefig("graph.png")
    plt.show()
    


