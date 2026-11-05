import def_agents
import test_agents
import random

for testName in test_agents.getTestNames():
    getattr(test_agents, testName)()
    print("Finished: ", testName)

random.seed()

env = def_agents.TrivialVacuumEnvironment()
agent = def_agents.RandomVacuumAgent()
env.add_thing(agent)
print("Start:", env.status, "agent at", agent.location)
for i in range(5):
    env.step()
    print("Step", i + 1, ":", env.status, "agent at", agent.location,
          "performance", agent.performance)
print("End:", env.status, "agent at", agent.location)
print("Final performance:", agent.performance)

print("=============================================================")
random.seed()

env = def_agents.TrivialVacuumEnvironment()
agent = def_agents.ReflexVacuumAgent()
env.add_thing(agent)
print("Start:", env.status, "agent at", agent.location)
for i in range(5):
    env.step()
    print("Step", i + 1, ":", env.status, "agent at", agent.location,
          "performance", agent.performance)
print("End:", env.status, "agent at", agent.location)
print("Final performance:", agent.performance)

print("=============================================================")
random.seed()

env = def_agents.TrivialVacuumEnvironment()
agent = def_agents.ModelBasedVacuumAgent()
env.add_thing(agent)
print("Start:", env.status, "agent at", agent.location)
for i in range(5):
    env.step()
    print("Step", i + 1, ":", env.status, "agent at", agent.location,
          "performance", agent.performance)
print("End:", env.status, "agent at", agent.location)
print("Final performance:", agent.performance)