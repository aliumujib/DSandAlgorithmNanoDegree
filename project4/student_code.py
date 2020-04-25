import math
import heapq


# This State class allows me to represent the vertex and its estimate based on the explanation in the Uniform Cost Search lessons.

class State:
    def __init__(self, vertex, h_estimate):
        self.vertex = vertex
        self.h_estimate = h_estimate

    def __lt__(self, other):
        return self.h_estimate < other.h_estimate


def shortest_path(graph, start, goal):
    path_heap = [State(start, 0)]
    heapq.heapify(path_heap)

    previous_vertices = {start: None}
    look_up_table = {start: 0}

    while path_heap:
        current = heapq.heappop(path_heap).vertex
        if current == goal:
            build_path(previous_vertices, start, goal, [goal])

        for node in graph.roads[current]:
            updated_score = look_up_table[current] + \
                            heuristic_cost_estimate(graph.intersections[current], graph.intersections[node])

            if node not in look_up_table or updated_score < look_up_table[node]:
                look_up_table[node] = updated_score
                total_score = updated_score + \
                              heuristic_cost_estimate(graph.intersections[current],
                                                      graph.intersections[node])
                heapq.heappush(path_heap, State(node, total_score))
                previous_vertices[node] = current

    return build_path(previous_vertices, start, goal, [goal])


def heuristic_cost_estimate(start, goal):
    # uses Pythagoras's theorem to find straight line distance between start and goal.
    # Learnt an interesting lesson here about floating point multiplication in python here.
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


def build_path(previous_vertices, start, current, path):  # constructs the path recursively.
    if current == start:
        path.reverse()
        return path
    else:
        current = previous_vertices[current]
        path.append(current)
        return build_path(previous_vertices, start, current, path)
