import random
from def_agents import Direction
from def_agents import Agent
from def_agents import Status
from def_agents import (ReflexVacuumAgent, ModelBasedVacuumAgent, TrivialVacuumEnvironment, compare_agents,
                          RandomVacuumAgent)


random.seed("aima-python")


def test_move_forward():
    print()
    print("=============================================================")
    print("Testing move_forward() with various directions and positions")
    print("=============================================================")
    d = Direction("up")
    l1 = d.move_forward((0, 0))
    print("Facing", d.direction, "from (0, 0) ->", l1, "expected (0, -1):", l1 == (0, -1))
    assert l1 == (0, -1)

    d = Direction(Direction.R)
    l1 = d.move_forward((0, 0))
    print("Facing", d.direction, "from (0, 0) ->", l1, "expected (1, 0):", l1 == (1, 0))
    assert l1 == (1, 0)

    d = Direction(Direction.D)
    l1 = d.move_forward((0, 0))
    print("Facing", d.direction, "from (0, 0) ->", l1, "expected (0, 1):", l1 == (0, 1))
    assert l1 == (0, 1)

    d = Direction("left")
    l1 = d.move_forward((0, 0))
    print("Facing", d.direction, "from (0, 0) ->", l1, "expected (-1, 0):", l1 == (-1, 0))
    assert l1 == (-1, 0)

    l2 = d.move_forward((1, 0))
    print("Facing", d.direction, "from (1, 0) ->", l2, "expected (0, 0):", l2 == (0, 0))
    assert l2 == (0, 0)


def test_add():
    print()
    print("=============================================================")
    print("Testing __add__() with various directions and turns")
    print("=============================================================")
    d = Direction(Direction.U)
    l1 = d + "right"
    l2 = d + "left"
    print("Facing", d.direction, "turn right ->", l1.direction, "expected", Direction.R + ":", l1.direction == Direction.R)
    print("Facing", d.direction, "turn left ->", l2.direction, "expected", Direction.L + ":", l2.direction == Direction.L)
    assert l1.direction == Direction.R
    assert l2.direction == Direction.L

    d = Direction("right")
    l1 = d.__add__(Direction.L)
    l2 = d.__add__(Direction.R)
    print("Facing", d.direction, "turn left ->", l1.direction, "expected up:", l1.direction == "up")
    print("Facing", d.direction, "turn right ->", l2.direction, "expected down:", l2.direction == "down")
    assert l1.direction == "up"
    assert l2.direction == "down"

    d = Direction("down")
    l1 = d.__add__("right")
    l2 = d.__add__("left")
    print("Facing", d.direction, "turn right ->", l1.direction, "expected", Direction.L + ":", l1.direction == Direction.L)
    print("Facing", d.direction, "turn left ->", l2.direction, "expected", Direction.R + ":", l2.direction == Direction.R)
    assert l1.direction == Direction.L
    assert l2.direction == Direction.R

    d = Direction(Direction.L)
    l1 = d + Direction.R
    l2 = d + Direction.L
    print("Facing", d.direction, "turn right ->", l1.direction, "expected", Direction.U + ":", l1.direction == Direction.U)
    print("Facing", d.direction, "turn left ->", l2.direction, "expected", Direction.D + ":", l2.direction == Direction.D)
    assert l1.direction == Direction.U
    assert l2.direction == Direction.D


def test_RandomVacuumAgent() :
    print()
    print("=============================================================")
    print("Testing RandomVacuumAgent")
    print("=============================================================")
    # create an object of the RandomVacuumAgent
    agent = RandomVacuumAgent()
    # create an object of TrivialVacuumEnvironment
    environment = TrivialVacuumEnvironment()
    # add agent to the environment
    environment.add_thing(agent)
    print("Start:", environment.status, "agent at", agent.location)
    # run the environment
    environment.run()
    # check final status of the environment
    print("End:", environment.status, "agent at", agent.location, "performance", agent.performance)
    print("Expected final status: {(1,0): Status.CLEAN, (0,0): Status.CLEAN}")
    assert environment.status == {(1,0): Status.CLEAN, (0,0): Status.CLEAN}


def test_ReflexVacuumAgent() :
    print()
    print("=============================================================")
    print("Testing ReflexVacuumAgent")
    print("=============================================================")
    # create an object of the ReflexVacuumAgent
    agent = ReflexVacuumAgent()
    # create an object of TrivialVacuumEnvironment
    environment = TrivialVacuumEnvironment()
    # add agent to the environment
    environment.add_thing(agent)
    print("Start:", environment.status, "agent at", agent.location)
    # run the environment
    environment.run()
    print("End:", environment.status, "agent at", agent.location, "performance", agent.performance)
    print("Expected final status: {(1,0): Status.CLEAN, (0,0): Status.CLEAN}")
    # check final status of the environment
    assert environment.status == {(1,0): Status.CLEAN, (0,0): Status.CLEAN}


def test_ModelBasedVacuumAgent() :
    print()
    print("=============================================================")
    print("Testing ModelBasedVacuumAgent")
    print("=============================================================")
    # create an object of the ModelBasedVacuumAgent
    agent = ModelBasedVacuumAgent()
    # create an object of TrivialVacuumEnvironment
    environment = TrivialVacuumEnvironment()
    # add agent to the environment
    environment.add_thing(agent)
    print("Start:", environment.status, "agent at", agent.location)
    # run the environment
    environment.run()
    print("End:", environment.status, "agent at", agent.location, "performance", agent.performance)
    print("Expected final status: {(1,0): Status.CLEAN, (0,0): Status.CLEAN}")
    # check final status of the environment
    assert environment.status == {(1,0): Status.CLEAN, (0,0): Status.CLEAN}


def test_compare_agents() :
    print()
    print("=============================================================")
    print("Comparing ModelBasedVacuumAgent and ReflexVacuumAgent")
    print("=============================================================")
    environment = TrivialVacuumEnvironment
    agents = [ModelBasedVacuumAgent, ReflexVacuumAgent]

    result = compare_agents(environment, agents)
    performance_ModelBasedVacummAgent = result[0][1]
    performance_ReflexVacummAgent = result[1][1]

    # The performance of ModelBasedVacuumAgent will be at least as good as that of
    # ReflexVacuumAgent, since ModelBasedVacuumAgent can identify when it has
    # reached the terminal state (both locations being clean) and will perform
    # NoOp leading to 0 performance change, whereas ReflexVacuumAgent cannot
    # identify the terminal state and thus will keep moving, leading to worse
    # performance compared to ModelBasedVacuumAgent.
    print("Performance ModelBasedVacummAgent:", performance_ModelBasedVacummAgent)
    print("Performance ReflexVacummAgent:", performance_ReflexVacummAgent)
    print("Expected: performance_ReflexVacummAgent <= performance_ModelBasedVacummAgent")
    assert performance_ReflexVacummAgent <= performance_ModelBasedVacummAgent


def test_Agent():
    print()
    print("=============================================================")
    print("Testing Agent")
    print("=============================================================")
    def constant_prog(percept):
        return percept
    agent = Agent(constant_prog)
    result = agent.program(5)
    print("Percept 5 -> action", result, "expected 5:", result == 5)
    assert result == 5

def getTestNames():
    return [name for name in globals() if name.startswith("test_")]
