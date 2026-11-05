# Week 1. Rational Agents

## Task 1. Consider the Python files for this week

- **`setup.py`** — Causes changing the working directory to the location of the files. Must be different each week in order to keep the files organized.
- **`utils.py`** — Imports the standard packages and defines some auxiliary functions.
- **`def_agents.py`** — Defines the agents, the environment and the agent functions implementing the perceptions and the actions. Each week the definitions will change to **`def_<name>.py`** where *`<name>`* is specific to the week.
- **`test_agents.py`** — Specifies test functions which check the code of the Python functions defined earlier, like **`test_Agent()`**, without actually executing them. You can run them one by one to check the code which is different each week. Note the use of the operation `assert` in the code – it suspends the execution of the corresponding Python operation while running the code, which otherwise would execute.
- **`run_agents.py`** — Specifies the actual functions which execute the agents, without actually executing them. You can execute them by invoking the corresponding **`run_<name>.py`** functions in the file, which will be different each week. This file is similar to **`test_agents.py`** but the **`assert`** commands are removed so that the code they protect runs.

Look inside the files and try to identify and understand the following:

- Which agent has been implemented
- Which actions and perceptions are there and how are they represented
- Where the environment changes and what causes the change
- How do we measure the performance

### Answers

**Which agent has been implemented**

The **vacuum-cleaner agent** (AIMA, Chapter 2), working in the two-square **[`TrivialVacuumEnvironment`](Workshop%201_Files/def_agents.py#L679)** with locations A `(0, 0)` and B `(1, 0)`. Four versions are defined in **[`def_agents.py`](Workshop%201_Files/def_agents.py)**:

- **[`RandomVacuumAgent`](Workshop%201_Files/def_agents.py#L173)** — ignores the percept and picks an action at random.
- **[`TableDrivenVacuumAgent`](Workshop%201_Files/def_agents.py#L178)** — looks up the action in a table keyed by the whole sequence of percepts seen so far. Defined but not used in **[`test_agents.py`](Workshop%201_Files/test_agents.py)** or **[`run_agents.py`](Workshop%201_Files/run_agents.py)**.
- **[`ReflexVacuumAgent`](Workshop%201_Files/def_agents.py#L194)** — simple reflex agent: `Suck` if dirty, otherwise move to the other square. No memory.
- **[`ModelBasedVacuumAgent`](Workshop%201_Files/def_agents.py#L207)** — model-based reflex agent: same rules, but it remembers the status of both squares and does `NoOp` once both are clean.

Only the random, reflex and model-based agents are exercised by **[`test_agents.py`](Workshop%201_Files/test_agents.py)** and **[`run_agents.py`](Workshop%201_Files/run_agents.py)**. The Wumpus World classes ([`Explorer`](Workshop%201_Files/def_agents.py#L762), [`WumpusEnvironment`](Workshop%201_Files/def_agents.py#L773)) are also in the file but are not used this week.

**Which actions and perceptions are there and how are they represented**

- **Percept** — a tuple `(location, status)`, e.g. `((0, 0), 'Dirty')`, returned by **[`TrivialVacuumEnvironment.percept()`](Workshop%201_Files/def_agents.py#L695)**. The location is an `(x, y)` tuple and the status is the string `'Clean'` or `'Dirty'`.
- **Actions** — the strings `'Right'`, `'Left'`, `'Suck'` and `'NoOp'`.
- The agent program is a function that takes a percept and returns an action; it is stored in the agent's **`program`** slot (see [`Agent`](Workshop%201_Files/def_agents.py#L71)).

**Where the environment changes and what causes the change**

- The environment changes in **[`TrivialVacuumEnvironment.execute_action()`](Workshop%201_Files/def_agents.py#L699)**: `'Right'` / `'Left'` change **`agent.location`**, and `'Suck'` sets **`self.status[location]`** to `'Clean'`. `'NoOp'` changes nothing.
- The change is caused by the agent's action. Each **[`Environment.step()`](Workshop%201_Files/def_agents.py#L266)** gets the percept, passes it to the agent program, and executes the returned action. **[`run()`](Workshop%201_Files/def_agents.py#L282)** repeats this for up to 1000 steps.
- The initial state is random: each square starts `'Clean'` or `'Dirty'` and the agent starts in A or B. Dirt never reappears, because **[`exogenous_change()`](Workshop%201_Files/def_agents.py#L258)** is not overridden.

**How do we measure the performance**

- Each agent has a **`performance`** score starting at 0 (set in [`Agent.__init__()`](Workshop%201_Files/def_agents.py#L88)). In **[`execute_action()`](Workshop%201_Files/def_agents.py#L699)** it gets **+10** for each dirty square it cleans and **−1** for each move (`'Right'` / `'Left'`). `'Suck'` on a clean square and `'NoOp'` cost nothing.
- **[`compare_agents()`](Workshop%201_Files/def_agents.py#L939)** creates 10 random environments, runs each agent for 1000 steps in a copy of each, and returns the average score per agent (computed by [`test_agent()`](Workshop%201_Files/def_agents.py#L949)).
- The model-based agent scores best because it stops with `NoOp` once both squares are clean. The reflex agent keeps moving back and forth and loses 1 point per move (in one run: about 9 for model-based, −989 for reflex, −486 for random).

## Task 2. Execute the agent

Load the files one by one and execute them at the prompt.

## Task 3. Modify the code to generate meaningful output

Add **`print()`** operations to the code so that you can trace the execution of the agents and log the information from the environment. You may wish to do this by modifying the **`test_agents.py`** file first but do not forget to change **`run_agents.py`** as well.

## Task 4. Modify the code

You may wish to revisit the files to use different data structures for representing the perceptions and the actions of the agent.

## Task 5 (Homework). Expand the code

Implement some additional types of agents or create your own agents for different tasks.
