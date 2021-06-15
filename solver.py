#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
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
    # Consider nodes in descending degree 
    for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
        neighbor_colors = set(color_map.get(neigh) for neigh in graph[node])
        color_map[node] = next( 
             color for color in range(len(graph)) if color not in neighbor_colors
             )
    
    solution = []
    for i in range(0,node_count):
        solution.append(color_map[str(i)])
    max_color = max(color_map.values())+1
    # prepare the solution in the specified output format
    output_data = str(max_color) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

