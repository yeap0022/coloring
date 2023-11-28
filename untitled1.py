# -*- coding: utf-8 -*-
"""

@author: yeapym
"""

# Python program for solution of M Coloring  
# problem using backtracking 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] 
                              for row in range(vertices)] 
  
    # A utility function to check if the current color assignment 
    # is safe for vertex v 
    def isSafe(self, v, colour, c): 
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colour[i] == c: 
                return False
        return True
      
    # A recursive utility function to solve m 
    # coloring  problem 
    def graphColourUtil(self, m, colour, v): 
        if v == self.V: 
            return True
  
        for c in range(1, m + 1): 
            if self.isSafe(v, colour, c) == True: 
                colour[v] = c 
                if self.graphColourUtil(m, colour, v + 1) == True: 
                    return True
                colour[v] = 0
  
    def graphColouring(self, m): 
        colour = [0] * self.V 
        if self.graphColourUtil(m, colour, 0) == None: 
            return False
  
        # Print the solution 
        print("Solution exist and Following are the assigned colours:")
        for c in colour: 
            print(c), 
        return True
  
# Driver Code
file1 = open("./data/gc_250_9.txt") 
input_data = file1.read()
  # print(input_data)
file1.close()
 
lines = input_data.split('\n')
 
first_line = lines[0].split()
node_count = int(first_line[0])
edge_count = int(first_line[1])
 
edges = []
for i in range(1, edge_count + 1):
    line = lines[i]
    parts = line.split()
    edges.append((int(parts[0]), int(parts[1]))) 

gra = [[0 for x in range(node_count)] for x in range(node_count)]

for i in edges:
    gra[i[0]][i[1]] = 1
    gra[i[1]][i[0]] = 1

g = Graph(node_count) 
g.graph = gra 
m = 98
g.graphColouring(m)
# g = Graph(node_count) 
# g.graph = edges
# m = 3
# g.graphColouring(m) 
  
# This code is contributed by Divyanshu Mehta 
