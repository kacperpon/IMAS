# Architecture

## Enviromnent

For this assignment, the environment proposed is a city where the agents will have to move to extinguish fires and resque injured people.

### Accesible?

If this was a real-life scenario, the environment would be inaccessible, that is, it would be impossible for any of the agents to fully know the state of the environment.
However, for this assignment we can assume that the agents are able to access the state of the environment at all times. If we agree that the only entities changing the environment are the agents themselves it's easy to reason that all that's needed for the agents to fully know the state of the environment is communication between them. At any point an agent could ask all the other agents about their locations and the actions they have performed on the enviromnent (for example, resquing a person or extinguishing a fire). In the same manner, once a fire report is received in the system it would be communicated to all the agents that need to know that information.

As a note, the accessibility depends on how we decide to model the environment, if we decide to introduce changes in the environment external to the agents and we don't inform them, for example a road block, the environment would not longer be fully accessible at all times. We could decide that for the agents to know about a road block, an agent would need to notice it before and communicate it to the rest of the agents. In this scenario the agents could never be sure that they know the state of the environment completely, making the environment inaccessible.

