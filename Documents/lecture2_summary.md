# Lecture 2: Agent Architectures

## 1. Intelligent Agent - Definition
- **Intelligent Agent**: System that perceives an environment through sensors and acts on it through effectors.
- **Autonomous Agent**: Computational system that operates independently in a complex, dynamic environment to achieve predefined goals.

## 2. Types of Environments
- **Accessible vs. Inaccessible**: Accessible environments offer complete, accurate information, while inaccessible ones do not.
- **Deterministic vs. Non-deterministic**: Deterministic environments have predictable outcomes; non-deterministic ones have uncertain results.
- **Episodic vs. Non-episodic**: Episodic environments involve independent episodes; non-episodic ones require linking actions across episodes.
- **Static vs. Dynamic**: Static environments remain unchanged; dynamic environments constantly change beyond the agent’s control.
- **Discrete vs. Continuous**: Discrete environments have finite actions; continuous ones are vast and complex.

## 3. Agent Architectures

### 3.1 Reactive Architectures
- **Characteristics**: Agents respond quickly to changes without complex processing, often relying on local sensor data.
- **Examples**: Ant colony behavior demonstrates swarm intelligence, where simple interactions lead to complex, emergent functionality.
- **Pros and Cons**: 
  - Pros: Simple design, adaptable in dynamic environments, and low computational cost.
  - Cons: Limited in long-term planning, challenging to incorporate learning, and complex to manage numerous behaviors.

### 3.2 Deliberative Architectures
- **Belief-Desire-Intention (BDI) Model**: Uses a symbolic world model to make logical decisions.
  - **Beliefs**: Agent’s view of the world.
  - **Desires**: Potential goals derived from beliefs.
  - **Intentions**: Committed goals that drive behavior.
- **Sense-Plan-Act Paradigm**: Actions are planned based on reasoning, but this is resource-intensive.
- **Challenges**: High computational cost, especially in dynamic environments, where continuous model updating is necessary.

### 3.3 Hybrid Architectures
- **Overview**: Combines reactive and deliberative architectures for balanced performance.
- **Layered Architectures**: Uses layers where reactive components handle immediate responses, while deliberative ones manage complex planning.
- **Examples**:
  - **TOURINGMACHINES**: Uses multiple control layers to manage perception and action.
  - **InteRRaP**: Vertically layered structure with behavior, planning, and cooperative layers to handle agent and social modeling.
- **Critiques**: Lack of general methodologies, highly specific designs, and limited formal theory support.
