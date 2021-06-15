# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:01:00 2020

@author: USER
"""

from ortools.sat.python import cp_model
# import matplotlib.pyplot as plt
# import networkx as nx

# Define a class for solution printing inheriting the CpSolverSolutionCallback
class SolutionPrinter(cp_model.CpSolverSolutionCallback):
  """Print intermediate solutions."""

  # def __init__(self, variables, limit):
  def __init__(self, variables):
    cp_model.CpSolverSolutionCallback.__init__(self)
    self.__variables = variables
    self.__solution_count = 0
    # self.__solution_limit = limit
    self.colors = ["0", "1", "2", "3"]
    self.node_colors = []
  
  # This is a callback function which is called when a solution is found.
  def OnSolutionCallback(self):
    self.__solution_count += 1
    for v in self.__variables:
      print('{} = {}'.format(v, self.colors[self.Value(v)]), end = '\n')
      self.node_colors.append(self.colors[self.Value(v)])
    print()
    # if self.__solution_count >= self.__solution_limit:
    #   print('Stop search after {} solutions'.format(self.__solution_limit))
    #   self.StopSearch()

  def SolutionCount(self):
    return self.__solution_count, self.node_colors

# A function to solve the graph coloring problem
# def graph_coloring(num_nodes, connections, k, num_solutions=2):
def graph_coloring(num_nodes, connections, k):

  # Instantiate the CpModel 
  model = cp_model.CpModel()
  # Create a variable ranging from 0 to k for each node.
  nodes = [model.NewIntVar(0, k-1, 'x%i' %i) for i in range(num_nodes)]

  # Add a constraint (i.e value of node A != value of node B) for each edge.
  model.Add(nodes[1]==0)
  for i, conn in enumerate(connections):
    model.Add(nodes[conn[0]] != nodes[conn[1]])
    


  
  # Instantiate a Cp solver
  solver = cp_model.CpSolver()
  # Instantiate a callback function to print solution
  # solution_printer = SolutionPrinter(nodes, num_solutions)
  solution_printer = SolutionPrinter(nodes)

  # Search for all soltuions 
  status = solver.SearchForAllSolutions(model, solution_printer)
  count, colors = solution_printer.SolutionCount()
  print("Solution found : %i" % count)
  # Return the color values
  return colors

file = open("./data/gc_4_1.txt")
input_data = file.read()
# print(input_data)
file.close()

lines = input_data.split('\n')

first_line = lines[0].split()
node_count = int(first_line[0])
edge_count = int(first_line[1])

edges = []
for i in range(1, edge_count + 1):
    line = lines[i]
    parts = line.split()
    edges.append((int(parts[0]), int(parts[1])))
# Define number of nodes in the graph
num_nodes = node_count
# Set number of colors as domain
domain = 3
# Add a connection for each edge.
connections = edges
# Define the number of solutions required.
# num_solutions = 3

# # plot a raw graph
# g1 = nx.Graph()
# for conn in connections:
#   g1.add_edge(conn[0], conn[1], color="black")
# plt.subplot(121)
# nx.draw(g1, with_labels=True, font_weight='bold') 
# plt.savefig("raw.png")

# call the graph coloring function to solve the graph for given colors.
# colors = graph_coloring(num_nodes, connections, domain, num_solutions)
colors = graph_coloring(num_nodes, connections, domain)

# # Plot a processed graph.
# plt.subplot(122)
# assign_colors = []
# for node in g1.nodes():
#   assign_colors.append(colors[node])
# nx.draw(g1,node_color = assign_colors, with_labels=True, font_weight='bold')
# plt.savefig("processed.png")