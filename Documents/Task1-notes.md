ENVIRONMENT

- **Accessibility**: Inaccessible: define some parts inaccessible. General map is accessible. But agents know specifics like their particular location, magnitude of the fire, number of wounded… Agent communications is required for all agents to know the full state.  
- **Deterministic:** Non-Deterministic**:** The fact that we perform an action does not mean that we will always get the same results from the environment. There can be a set of probabilistic variables that make the environment non-deterministic. For instance, if we put out a fire, there can be a chance that the fire will be stopped or not.  
- **Episodic:** Non-Episodic: Since we won’t have any algorithm to train along a set of distinct episodes (implementation based on pre-trained LLM) we will not make the environment episodic. However, it could be episodic if every emergency is considered an individual episode.  
- **Static/dynamic**: Dynamic. A fire can get worse over time. Victim’s health can be reduced over time.  
- **Discrete/continuous:** Continuous. In terms of the map, the agent can go anywhere in X, Y, without being discrete. Time will also be continuous. Actions can be discrete, each type of agent will have a list of actions it can perform, but the environment itself is continuous. The fire intensity can be from 1 to 100 continuous.

CREWS

- **Emergency**  
  - **Contact agent.** Distributes everything, and coordinates other CREWS. Gives objectives to the Organization Agent of each crew.  
    - **Type: Facilitator**  
    - *No flexibility.*  
    - *Deliberative*  
    - *Not reactive.*  
    - *Not proactive: Does not read into the details of the emergency, just orders the crews to solve the problem.*  
    - *Social Ability: Interact with other agents.*  
    - *No mobility.*  
- **Firefighting crew**  
  - **Organization Agent:** Creates strict plan for this crew.  
    - **Type: Facilitator**  
    - *Deliberative. Makes a general plan to be executed by Actuator agents. This plan does not include small details as the Agent will now know the full state of the environment. Remember, the environment is not fully accessible.*  
    - *Reactive: Will change plan based on the evolution of the emergency.*  
  - **(3x) Firefighter Actuator Agent:** Follows the plan of the Organization Agent. (Fights fire).  
    - **Type: Actuator.**  
    - *Hybrid (follows a plan and takes small decisions). A small obstacle does not imply that the organization agent needs to know about it and change the whole plan. Little obstacles can be surpassed by the Actuator Agent’s own decisions.*  
    - *Reactive: Will change plan based on the evolution of the emergency.*  
  - **(3x) Rescue Actuator Agent:** Follows the plan of the Organization Agent. (Rescues people)  
    - **Type: Actuator.**  
    - *Hybrid*  
    - Reactive: Will change plan based on the evolution of the emergency.  
- **Medical Team**  
  - **Organization Agent:** Creates strict plan for this crew.  
    - **Type: Facilitator**  
    - Deliberative  
  - **(3x) Med Actuator Agent:** Follows the plan of the Organization Agent. (Attends victims, first aid).  
    - **Type: Actuator.**  
    - Hybrid  
  - **(3x) Driver Actuator Agent**: Follows the plan of the Organization Agent. (Drives ambulance).  
    - **Type: Actuator.**  
    - Hybrid

INDIVIDUAL AGENT PROPERTIES
|  | Emergency | Firefighting Crew |  | Medical Team |  |  |
| :---- | ----- | ----- | :---- | ----- | :---- | :---- |
|  | **Contact Agent** | **Organization Agent** | **Actuator Agent** | **Organization Agent** | **Actuator Agent** | **Justification** |
| **Flexibility** | YES | YES | YES | YES | YES | All agents need to adapt to changing situations, such as a new fire occurring or a lack of resources. |
| **Reactivity** | YES | YES | YES | YES | YES | All agents need to be reactive to changes in the environment to ensure an optimal plan is followed at all times. |
| **Proactiveness** | NO | YES | YES | YES | YES | All agents except the contact agent must anticipate future states and act accordingly. For example, an unused actuator crew must be ready and available at all times to respond to a change in the environment (i.e.: new fire). Contact agent is not proactive because they cannot anticipate the conditions of a new fire that has not yet occurred. |
| **Social Ability** | YES | YES | YES | YES | YES | Communication is essential for coordination among agents. |
| **Rationality** | YES | YES | YES | YES | YES | Agents must make logical decisions based on available information. |
| **Reasoning** | YES | YES | LESS | YES | LESS | Organization and contact agents require more reasoning than actuator Agents. Actuator agents follow a pre-defined plan given to them by the organization agents, with minimal decision making capabilities to adapt to minor changes in the emergency. |
| **Learning** | NO | NO | NO | NO | NO | Agents follow pre-defined plans and do not learn from experiences. |
| **Autonomy** | HIGH | HIGH | LOW | HIGH | LOW | Organization Agents have more autonomy than Actuator Agents. Actuator agents follow a pre-defined plan given to them by the organization agents. Giving these agents high autonomy could hinder the optimality of the plan generated by the contact agent.|
| **Temporal continuity** | YES | YES | YES | YES | YES | All agents operate continuously over time. All agents must be on standby to react to new emergencies emerging. |
| **Mobility** | NO | NO | YES | NO | YES | Contact and organisational agents are stationary, the actuator agents need to move to perform tasks given to them by the other agents. |
