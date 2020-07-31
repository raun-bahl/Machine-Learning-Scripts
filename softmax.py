import numpy as np
import matplotlib.pyplot as plt
import random 

o1_o2 = [0.2,0.2]
o_three = [random.uniform(0,5) for x in range(0,50)]
tuple_list= []

for i in o_three:
    tuple_list.append((0.2,0.2,i))

soft = []
for elems in tuple_list:
    
    soft.append(np.exp(elems[2])/ (np.exp(elems[0]) + np.exp(elems[1]) + np.exp(elems[2])))

def line_graph(x, y, x_title, y_title):
    """
    Draw line graph with x and y values
    :param x:
    :param y:
    :param x_title:
    :param y_title:
    :return:
    """
    plt.scatter(x, y)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title("Plot of the softmax's value as a function of o3 (y3)")
    plt.show()
    

graph_x = o_three
graph_y = soft

line_graph(graph_x, graph_y, "o3", "Softmax value (y3)")




