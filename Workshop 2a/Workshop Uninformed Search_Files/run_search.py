from def_problem import *
from def_solver import *
from def_search import *


romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)


def run_find_min_edge():
    romania_problem.find_min_edge() == 70


def run_breadth_first_tree_search():
    breadth_first_tree_search(romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']


def run_breadth_first_search():
    breadth_first_search(romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']


def run_best_first_graph_search():
    # uniform_cost_search and astar_search test it indirectly
    best_first_graph_search(romania_problem,
        lambda node: node.state).solution() == ['Sibiu', 'Fagaras', 'Bucharest']
    best_first_graph_search(
        romania_problem,
        lambda node: node.state[::-1]).solution() == ['Timisoara',
                                                      'Lugoj',
                                                      'Mehadia',
                                                      'Drobeta',
                                                      'Craiova',
                                                      'Pitesti',
                                                      'Bucharest']


def run_uniform_cost_search():
    uniform_cost_search(
        romania_problem).solution() == ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']


def run_depth_first_graph_search():
    solution = depth_first_graph_search(romania_problem).solution()
    solution[-1] == 'Bucharest'


def run_iterative_deepening_search():
    iterative_deepening_search(
        romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']


def run_depth_limited_search():
    solution_3 = depth_limited_search(romania_problem, 3).solution()
    solution_3[-1] == 'Bucharest'
    depth_limited_search(romania_problem, 2) == 'cutoff'
    solution_50 = depth_limited_search(romania_problem).solution()
    solution_50[-1] == 'Bucharest'


def run_bidirectional_search():
    bidirectional_search(romania_problem) == 418



