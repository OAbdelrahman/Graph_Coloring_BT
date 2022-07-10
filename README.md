# Graph_Coloring_BT

### Programming Language:
Python

### Purpose:
This program colors the nodes of a graph such that no two connected nodes have the same color.


### How it works:
This program takes in an adjacency matrix of the graph, and a list of available colors.<br>
This program is hard coded for the following graph:<br>
[[False, True, False, False, False, True ], <br>
[True, False, True, False, False, True ], <br>
[False, True, False, True, True, False], <br>
[False, False, True, False, True, False], <br>
[False, False, True, True, False, True ], <br>
[True, True, False, False, True, False]] <br>

and the following colors: red, green, blue. <br>

The program starts at one of the nodes and colors it with the first color on the list, <br>
and does so with the following node, until there's a conflict (two connected nodes with the same color). <br>
Once a conflict is detected, the algorithm backtracks to the previous node and changes its color. <br>
