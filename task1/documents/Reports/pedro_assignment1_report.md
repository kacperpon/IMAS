# Architecture

## Enviromnent

For this assignment, the environment proposed is a city where the agents will have to move to extinguish fires and resque injured people.

### Accesible?

If this was a real-life scenario, the environment would be inaccessible, that is, it would be impossible for any of the agents to fully know the state of the environment.
However, for this assignment we can assume that the agents are able to access the state of the environment at all times. If we agree that the only entities changing the environment are the agents themselves it's easy to reason that all that's needed for the agents to fully know the state of the environment is communication between them. At any point an agent could ask all the other agents about their locations and the actions they have performed on the enviromnent (for example, resquing a person or extinguishing a fire). In the same manner, once a fire report is received in the system it would be communicated to all the agents that need to know that information.

As a note, the accessibility depends on how we decide to model the environment, if we decide to introduce changes in the environment external to the agents and we don't inform them, for example a road block, the environment would not longer be fully accessible at all times. We could decide that for the agents to know about a road block, an agent would need to notice it before and communicate it to the rest of the agents. In this scenario the agents could never be sure that they know the state of the environment completely, making the environment inaccessible.

### Deterministic?

As with the accessibility, the problem can be modeled to be deterministic or non-deterministic. If every action an agent performs has a set of consequences that will happen with 100% probability, then the final state of the environment after the action can be predicted before performing the action.

One way we could model the environment to be non-deterministic would be to introduce a non-zero probability for a fire to restart once it's extinguished, in this case, knowing that some agents have extinguished a fire does not guarantee that the fire is extinguished.

### Episodic?

No idea tbh

### Static or dynamic?

Using the definition of static environment "A static environment is one that can be assumed to remain unchanged except by the performance of actions by the agent" from the lecture slides, and taking into account that the agents can, at any time, receive an external report that describes a change in the environment, we can derive that the enviromnment is dynamic.

### Discrete or continuous?

Although very big, for this assignment's environment there is a finite list of possible actions (for example, all the routes an agent could do in the city) and states (all the fires/fire types that can happen at any time). Thus we can agree that the environment is discrete.


## Agents

# Emergency service

From the assignment description: "this crew is the one which receives the call asking for help. It has to
notify the fire people and medical services about the incidence"

**Emergencies organizer:** The organizer could be in charge of the communication between the user and the fire and medical teams:
    - A fire report
    - The state of any agent as reported by the agent

The task of the organizer is to gather information about the state of the environment and organize it in a structured way to transmit it to the rest of the agents.
For example, if an agent has successfully extinguished a fire they will communicate it to the chief, who would update its knowledge of the state of the environment and communicate it to the agents it considers should know (a medic might not need to know if a fire truck is on its way to a fire).

It will produce and output:
    - A structured and personalized summary of the state of the environment

