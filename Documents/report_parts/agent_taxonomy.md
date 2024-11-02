## 3.  Agent Taxonomy

### 3.1 Classification Framework
The emergency response multi-agent system uses a hierarchical framework that
sets clear boundaries between three primary agent types: Contact Agents, Organisation Agents, and Actuator Agents. This design optimises emergency reponse operations while maintaining clear command structure at the same time with the goal of optimal operational efficiency.

#### 3.1.1 Agent Types
**Contact Agent (Type: Faciliator)**
This agent is the primary coordinator within the emergency response team, operating as a high-evel design facilitator. While this agent has high levels of autonomy and strong reasoning capabilities, it lacks proactiveness and mobility. The primary role includes optimal distribution of resources and coordination of response teams - making it essential for maintaining system-wide coherence without direct involvement. 

**Organisation Agent (Type: Faciliator)**
The organisation agent functions as strategic planners within each specialised crew (firefighting, medical, and police). Some qualities of these agents include:

- Deliberative decision-making processes.
- High autonomy in plan creation.
- Strong reactive capabilities to emergency evolution.
- Stationary operation with robust communication abilities.

**Organisation Agent (Type: Faciliator)**
The actuator agent represents the operational level of the system, which includes firefighters, medical staff, and police patrol units. Some qualities of these agents include:

- Hybrid architecture combining planned and reactive behaviors
- Limited autonomy within predetermined operational frameworks
- High mobility for field operations
- Specialized task execution capabilities


### 3.2 Cross-Domain Analysis

#### 3.2.1 Common Properties Across Agent Types
Several fundamental agent properties are shared across all of our agent types, while other properties are selected for an agent based on the required needs.

##### 1. Universal Characteristics
- Flexibility: All agents maintain adaptability to dynamic emergency situations.
- Social Ability: Required for inter-agent coordination.
- Rationality: Essential for logical, information-based decision-making.
- Temporal Continuity: All agents operate continuously to maintain response readiness.

##### 2. Differentiated Properties 
The system implements distinction in properties to maximise efficiency:
- **a) Reasoning Capabilities**
Contact and organisation agents employ a high level of reasoning, whereas actuator agents employ limited level of reasoning.
- **b) Autonomy Distribution**
Contact and organisation agents employ a high level of reasoning to perform strategic planning, whereas actuator agents employ limited level of reasoning for consistent plan execution.

#### 3.2.2 Domain-Specific Variations
The basic framework remains consistent across domains, but more specific implementations are
required based on the operational requirements:

**1. Firefighting Domain**
- Organisation Agents: Emphasises firefighting-specific planning.
- Actuator Agents: Split between firefighting and rescue operations which require specialised mobility patterns - these to be provided by the organisation agents.

**2. Medical Domain**
- Organisation Agents: Focuses on allocation of resources and patient distribution.
- Actuator Agents: Split between medical care and transportation roles.

**3. Police Domain**
- Organisation Agents: Coordinates traffic and crowd control strategies.
- Actuator Agents: Focuses on mobility restrictions and public interaction.

#### 3.2.3 System-Wide Characteristics
Several system-wide characteristics have been established following on from our analysis of the problem:

**1. Learning Implementation**
The system excludes the use of learning capabilities to learn from previous responses. As the system relies on pre-defined protocols and real-time adaptation, tt is assumed an optimal plan is established - hence no learning is required.

**2. Mobility Patterns**
A clear distinction is formed between stationary agents (Contact and Organisation) and mobile agents (Actuators) for operations.

**3. Communication Hierarchy**
Vertical communication channels are established between different agent types who have the ability for cross-agent communication, whereas horizontal communication channels are established for same-level agent communication.

### 3.3 Agent Taxonomy Grid
Below is a agent taxonomy grid outlining each agent along with each fundamental agent property, and whether an agent contains the property or not along with a justification for the design.

|                  | Emergency          | Firefighting Crew          |                  | Medical Team            |                  | Police Crew              |                  | Justification                                                                                                                                                                                                                                                                                    |
|------------------|--------------------|----------------------------|------------------|--------------------------|------------------|--------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  | **Contact Agent**  | **Organization Agent**     | **Actuator Agent** | **Organization Agent**   | **Actuator Agent** | **Organization Agent**   | **Actuator Agent** |                                                                                                                                                                                                                                                                                                 |
| **Flexibility**  | YES                | YES                        | YES              | YES                      | YES              | YES                      | YES              | All agents need to adapt to changing situations, such as a new fire occurring or a lack of resources.                                                                                                                                                    |
| **Reactivity**   | YES                | YES                        | YES              | YES                      | YES              | YES                      | YES              | All agents need to be reactive to changes in the environment to ensure an optimal plan is followed at all times.                                                                                                                                         |
| **Proactiveness**| NO                 | YES                        | YES              | YES                      | YES              | YES                      | YES              | All agents except the contact agent must anticipate future states and act accordingly. For example, an unused actuator crew must be ready and available at all times to respond to a change in the environment (i.e.: new fire). Contact agent is not proactive because they cannot anticipate the conditions of a new fire that has not yet occurred. |
| **Social Ability** | YES             | YES                        | YES              | YES                      | YES              | YES                      | YES              | Communication is essential for coordination among agents.                                                                                                                                                                                                                                                                                  |
| **Rationality**  | YES                | YES                        | YES              | YES                      | YES              | YES                      | YES              | Agents must make logical decisions based on available information.                                                                                                                                                                                                                                                                       |
| **Reasoning**    | YES                | YES                        | LESS             | YES                      | LESS             | YES                      | LESS             | Organization and contact agents require more reasoning than actuator Agents. Actuator agents follow a pre-defined plan given to them by the organization agents, with minimal decision-making capabilities to adapt to minor changes in the emergency.                                      |
| **Learning**     | NO                 | NO                         | NO               | NO                       | NO               | NO                       | NO               | Agents follow pre-defined plans and do not learn from experiences.                                                                                                                                                                                                                                                                      |
| **Autonomy**     | HIGH               | HIGH                       | LOW              | HIGH                     | LOW              | HIGH                     | LOW              | Organization agents have more autonomy than actuator Agents. Actuator agents follow a pre-defined plan given to them by the organization agents. Giving these agents high autonomy could hinder the optimality of the plan generated by the contact agent.                                 |
| **Temporal continuity** | YES        | YES                        | YES              | YES                      | YES              | YES                      | YES              | All agents operate continuously over time. All agents must be on standby to react to new emergencies emerging.                                                                                                                                                                                     |
| **Mobility**     | NO                 | NO                         | YES              | NO                       | YES              | NO                       | YES              | Contact and organisational agents are stationary; the actuator agents need to move to perform tasks given to them by the other agents.                                                                                                                                                                                                                                                                      |
