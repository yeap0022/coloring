# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:49:34 2020

@author: yeapym
"""

# def color_nodes(graph):
#     color_map = {}
#     # Consider nodes in descending degree 
#     for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
#         neighbor_colors = set(color_map.get(neigh) for neigh in graph[node])
#         color_map[node] = next( 
#             color for color in range(len(graph)) if color not in neighbor_colors
#         )
#     return color_map    
    

if __name__ == '__main__':
   file1 = open("./data/gc_50_3.txt") 
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
        
   graph = {}
    
   for j in range(0,len(edges)):
       if str(edges[j][0]) not in graph:
           graph[str(edges[j][0])] = [str(edges[j][1])]
       else:
           graph[str(edges[j][0])].append(str(edges[j][1]))
 
   for j in range(0,len(edges)):
       if str(edges[j][1]) not in graph:
           graph[str(edges[j][1])] = [str(edges[j][0])]
       else:
           graph[str(edges[j][1])].append(str(edges[j][0])) 
       
   color_map = {}
   color_map['1'] = 0
   color_map['4'] = 0
   color_map['9'] = 0
   color_map['17'] = 0
   color_map['18'] = 0
   color_map['34'] = 0
   color_map['37'] = 0
   color_map['41'] = 0
   color_map['48'] = 0
   color_map['49'] = 0
   color_map['0'] = 5
   color_map['23'] = 5
   color_map['24'] = 5
   color_map['26'] = 5
   color_map['35'] = 5
   color_map['38'] = 5
   color_map['44'] = 5
   color_map['47'] = 5
   
    # Consider nodes in descending degree 
   for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
        neighbor_colors = set(color_map.get(neigh) for neigh in graph[node])
        color_map[node] = next( 
                 color for color in range(len(graph)) if color not in neighbor_colors
                 )
   
   # node_color = []
   # for i in range(0,node_count):
   #     node_color.append(color_map[str(i)])
  # print(color_nodes(graph))