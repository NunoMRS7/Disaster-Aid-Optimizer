from graph.algorithms.heuristic import edge_heuristic
from utils.graph_generator import apply_randomness_to_graph

def a_star(graph, start, end, use_simple_heuristic=True, vehicle=None):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {start}
        closed_list = set([])

        # g contains current distances from start to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start] = start
        
        n = None
        iterations_count = 1
        while len(open_list) > 0:
            if not use_simple_heuristic and iterations_count % 3 == 0:
                apply_randomness_to_graph(graph)

            # find a node with the lowest value of f() - evaluation function
            calc_heurist = {}
            flag = False
            for v in open_list:
                if n == None:
                    n = v
                else:
                    v.determine_self_heuristic()
                    flag = True
                    h = v.calculate_distance_between_zones(end) + (0.0 if use_simple_heuristic else v.heuristic)    
                    calc_heurist[v] = g[v] + h
            if flag == True:
                n = get_min_heuristic(calc_heurist)  
            if n == None:
                print('Path does not exist!')
                return None, None, None

            # if the current node is the end
            # then we begin reconstructing the path from it to the start
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                total_path_cost = 0
                for i in range(len(reconst_path) - 1):
                    distance = reconst_path[i].calculate_distance_between_zones(reconst_path[i + 1])
                    total_path_cost += distance
                    if not use_simple_heuristic and vehicle:
                        autonomy_loss = vehicle.calculate_autonomy_loss(distance)
                        print(f'Vehicle autonomy: {vehicle.autonomy}')
                        if vehicle.autonomy - autonomy_loss < 0:
                            reconst_path[i].supplies += vehicle.load
                            vehicle.load = 0
                            print('Vehicle ran out of autonomy!')
                            return reconst_path[:i+1], closed_list, total_path_cost
                        
                        vehicle.autonomy -= autonomy_loss
                        
                        supplies_to_leave = reconst_path[i].calculate_supplies_to_leave()
                        print(f'Vehicle load: {vehicle.load}, supplies to leave: {supplies_to_leave}')
                        if vehicle.load - supplies_to_leave < 0:
                            reconst_path[i].supplies += vehicle.load
                            vehicle.load = 0
                            print('Vehicle ran out of supplies!')
                            return reconst_path[:i+1], closed_list, total_path_cost
                        
                        reconst_path[i].supplies += supplies_to_leave
                        vehicle.load -= supplies_to_leave

                return (reconst_path, closed_list, total_path_cost)

            # for all neighbors of the current node do
            for (m, road) in graph.get_connections(n):
                weight = road.cost if use_simple_heuristic else edge_heuristic(road.cost, road.conditions, road.geography, road.infrastructure, road.availability, vehicle.type)
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

            iterations_count += 1

        print('Path does not exist!')
        return None, None, None

def get_min_heuristic(map):
    minimum = float('inf')
    zone = None
    for key in map:
        if map[key] < minimum:
            minimum = map[key]
            zone = key
    return zone