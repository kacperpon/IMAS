# Design of a Multi-Agent System for Emergency Response Simulation in Urban Environments: Task 1.

**Students:**
Pedro Agundez Fernández,
Pau Baguer Fàbrega,
Carlos Jiménez Farfán,
Kacper Krzysztof Poniatowski,
Niklas Long Schiefelbein

## Index

- [Design of a Multi-Agent System for Emergency Response Simulation in Urban Environments: Task 1.](#design-of-a-multi-agent-system-for-emergency-response-simulation-in-urban-environments-task-1)
  - [Index](#index)
  - [Introduction](#introduction)
- [1. Environment analysis](#1-environment-analysis)
    - [Accessibility](#accessibility)
    - [Determinism](#determinism)
    - [Episodicity](#episodicity)
    - [Dynamism](#dynamism)
    - [Continuity](#continuity)
- [2. Agent selection and definition](#2-agent-selection-and-definition)
- [3 Emergency Response System Workflow](#3-emergency-response-system-workflow)
  - [1. Initial Emergency Report \& Assessment](#1-initial-emergency-report--assessment)
  - [2. Strategic Planning](#2-strategic-planning)
    - [Initial Distribution](#initial-distribution)
    - [Specialized Planning](#specialized-planning)
  - [3. Plan Integration \& Approval](#3-plan-integration--approval)
  - [4. Operational Execution](#4-operational-execution)
    - [Team Deployment](#team-deployment)
    - [Parallel Operations](#parallel-operations)
    - [Real-time Coordination](#real-time-coordination)
  - [5. Incident Resolution](#5-incident-resolution)
    - [Final Checks](#final-checks)
- [4. Agent Taxonomy Analysis](#4-agent-taxonomy-analysis)
    - [3.1 Overview](#31-overview)
    - [3.2 Agent Property Analysis](#32-agent-property-analysis)
    - [3.3 Property Justification](#33-property-justification)
      - [3.3.1 Flexibility](#331-flexibility)
      - [3.3.2 Reactivity](#332-reactivity)
      - [3.3.3 Proactiveness](#333-proactiveness)
      - [3.3.4 Social Ability](#334-social-ability)
      - [3.3.5 Rationality](#335-rationality)
      - [3.3.6 Reasoning](#336-reasoning)
      - [3.3.7 Learning](#337-learning)
      - [3.3.8 Autonomy](#338-autonomy)
      - [3.3.9 Temporal Continuity](#339-temporal-continuity)
      - [3.3.10 Mobility](#3310-mobility)
  - [Bibliography](#bibliography)



## Introduction

This is the report for Task 1, which presents the initial design of a Multi-Agent System (MAS) for managing emergency responses in an urban city. The objective of this project is to simulate a coordinated response among various autonomous agents to solve rescue scenarios which may contain fires, medical injuries, traffic management, etc. The environment will be carefully selected to emulate the real-world challenges and complexities of emergency management, including the optimization of resource allocation to ensure a precise and timely response by the emergency crews.

In this design phase, we focus on analyzing the environment, selecting and defining crews and agent roles, and classifying the agents within the system. The environment includes critical components such as fire trucks, ambulances, hospitals and other emergency services, each positioned and equipped based on realistic constraints. Our agents are structured into dedicated crews, each responsible for distinct aspects of the emergency response, including emergency coordination, fire containment, medical support, and ethical analysis.

# 1. Environment analysis

### Accessibility

An accessible environment is one in which the agent can obtain complete, accurate, up-to-date information about the environment's state.[1]  
The city map is designed to be generally accessible to all agents, with specific areas defined as inaccessible. Each agent, however, has a limited perception of the environment; they are only aware of their current location, the severity and type of any fire nearby, and the number of wounded individuals in the vicinity. To obtain a comprehensive view of the entire situation, agents need to communicate and share information regarding these details with one another.

### Determinism

A deterministic environment is one in which any action has a single guaranteed effect, there is no uncertainty aboutthe state that will result from performing an action.[1,4]  
The environment operates in a **Non-Deterministic** manner, meaning that actions do not always yield the same outcomes. Probabilistic factors influence the success or failure of certain actions. For example, an agent's attempt to extinguish a fire may not always be successful, as external conditions could allow the fire to persist or even spread.

### Episodicity

With episodicity defined as the extent to which an actor's actions during one time period affect events occurring during a different time period [2,4] we have determined that this environment is  **Non-Episodic**.  
There is no reliance on a training algorithm involving distinct episodes, as the system utilizes pre-trained language models, allowing it to operate continuously. However, each emergency report received by agents can be considered a self-contained episode for practical purposes.

### Dynamism

A static environment is one that can be assumed to remain unchanged except by the performance of actions by the agent [1, 4].  
The environment is **Dynamic**, with evolving conditions over time. Fires can grow in intensity if not extinguished, and the health of injured individuals may deteriorate if they do not receive timely assistance. This dynamism adds complexity to the agents' decision-making processes.

### Continuity

An environment is discrete if there are a fixed, finite number of actions and percepts in it[1].  
In terms of space, the environment is **Continuous**. Agents are free to navigate across continuous X and Y coordinates on the map. While the overall map and time structure remain continuous, agent actions, such as moving or extinguishing a fire, are performed in discrete steps.


# 2. Agent selection and definition

![agents](<crews graph.png>)

An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators [3].  
In this section we define the types of agents we propose for this task, each agent is defined by its task, type (facilitator or actuator) and tools.

- **Emergency crew**  
  - **Contact agent.** Recieves the report in natural language and compiles the data in json format to pass it to the organization agents. Once it recrives the plans from each organization agent and compiles them into a global plan, consults with the ethics crew in case there are ethical dilemmas and sends it back to the crews to execute. 
    - **Type:** Facilitator
    - **Tools:** FileReadTool

- **Ethics crew**  
  - **Philosopher agent.** Recieves an ethic dilemma from the emergency planner and solves it using RAG to extract the conclusion from an ethics "book" (text file).  
    - **Type:** Facilitator
    - **Tools:** FileReadTool
    
- **Firefighting crew**  
  - **Organization Agent:** Receives the structured information from the emergency contact agent, creates a list of tasks taking into account the resources available and the distance to the emergencies. Then it sends its plan to the emergency planner agent, when the whole plan is compiled (planner agent has responded), it passes the tasks to the actuators.  
    - **Type:** Facilitator  
    - **Deliberative:** Makes a general plan to be executed by Actuator agents. This plan does not include small details as the Agent will now know the full state of the environment. Remember, the environment is not fully accessible.*  
    - **Reactive:** Will change plan based on the evolution of the emergency.
    - **Tools:** DistanceMetricTool
      
  - **(3x) Firefighter Actuator Agent:** Follows the plan of the Organization Agent. (Fights fire).  
    - **Type:** Actuator.  
    - *Hybrid (follows a plan and takes small decisions). A small obstacle does not imply that the organization agent needs to know about it and change the whole plan. Little obstacles can be surpassed by the Actuator Agent’s own decisions.*  
    - *Reactive: Will change plan based on the evolution of the emergency.*  
  - **(3x) Rescue Actuator Agent:** Follows the plan of the Organization Agent. (Rescues people)  
    - **Type:** Actuator.  
    - *Hybrid*  
    - Reactive: Will change plan based on the evolution of the emergency.  

- **Medical crew**  
  - **Organization Agent:** Receives the structured information from the emergency contact agent, creates a list of tasks taking into account the resources available and the distance to the emergencies. Then it sends its plan to the emergency planner agent, when the whole plan is compiled (planner agent has responded), it passes the tasks to the actuators. 
    - **Type:** Facilitator  
    - **Deliberative**
    - **Tools:** DistanceMetricTool  
  - **(3x) Med Actuator Agent:** Follows the plan of the Organization Agent. (Attends victims, first aid).  
    - **Type:** Actuator.  
    - **Hybrid**  
  - **(3x) Driver Actuator Agent**: Follows the plan of the Organization Agent. (Drives ambulance).  
    - **Type:** Actuator.  
    - **Hybrid**
- **Police Crew**  
  - **Organization Agent:** Receives the structured information from the emergency contact agent, decides on what alternative routes should be created to avoid roads that are blocked by fires.  
    - **Type:** Facilitator  
    - **Deliberative**
    - **Tools:** DistanceMetricTool 
  - **(3x) Patrol Actuator Agent:** Follows the plan of the Organization Agent. (Drives patrol car, manages traffic and evacuation).  
    - **Type:** Actuator.  
    - **Hybrid**  

# 3 Emergency Response System Workflow  

![sequence_diagram](Sequence_diagram/03_11_sequence_diagram_agent_version.drawio.png)  

## 1. Initial Emergency Report & Assessment

The emergency response process initiates when a report is received by the system. Emergency services immediately gather structured information through a detailed Markdown report. This report is essential as it contains comprehensive details about the incident: the specific classification of the fire (whether it's ordinary, electrical, or gas-based), the exact location marked by X and Y coordinates, a count of people who have been injured in the incident, and a clear assessment of the fire's severity, categorized as low, medium, or high.

## 2. Strategic Planning

### Initial Distribution

Upon receiving this information, the emergency service swiftly develops a preliminary general plan. This plan is then systematically distributed to three key specialized departments: the Firefighting Crew, Medical Team, and Police Department. Each department receives relevant aspects of the plan pertaining to their specific roles and responsibilities.

### Specialized Planning

After receiving the initial plan, each department's organizational agents begin developing their own optimized response strategies. The Firefighting team creates a detailed plan considering the specific characteristics of the fire and the resources at their disposal. The Medical team focuses their planning on effective casualty management and coordination with nearby hospitals. Meanwhile, the Police department develops comprehensive strategies for traffic control that might be necessary.

## 3. Plan Integration & Approval

Following the specialized planning phase, all individual plans are brought together at the Emergency Services level for consolidation. When necessary, an ethical review is conducted to ensure all planned actions meet required standards and guidelines. Once approved, a comprehensive final plan is crafted, incorporating all specialized elements, and distributed back to all teams for execution.

## 4. Operational Execution

### Team Deployment

With the final plan approved, all actuator agents, representing the field units, execute their assigned tasks. Firefighting units proceed directly to the fire location, while medical units mobilize to handle casualties. Simultaneously, police units begin implementing traffic management procedures as needed.

### Parallel Operations

The execution phase involves multiple specialized operations occurring concurrently. The Firefighting team conducts both primary firefighting operations and rescue missions when required. The Medical team focuses on providing immediate medical treatment and coordinating patient transportation to appropriate facilities. The Police team maintains area security through regular patrols while managing traffic flow around the incident site.

### Real-time Coordination

Throughout the operation, all units maintain constant communication by providing regular status updates. This dynamic approach ensures effective inter-team coordination and optimal resource utilization throughout the emergency response.

## 5. Incident Resolution

### Final Checks

Once the immediate emergency is addressed, the firefighting team confirms complete fire extinction. All actuator agents then perform thorough final checks of their respective areas of responsibility. Each team methodically verifies that their specific objectives have been fully met according to the response plan.


# 4. Agent Taxonomy Analysis

### 3.1 Overview
This section of the report analyses the properties of each of the agents outlined in the previous section (Contact Agent, Organisation Agent, Actuator Agent, and Philosopher Agent). For each agent type, we examine which properties are present and provide justification for these design decisions.

### 3.2 Agent Property Analysis
|                  | Emergency          | Firefighting Crew          |                  | Medical Team            |                  | Police Crew              |                  | Ethics Crew                                                                                                                                                                                                                                                                                    |
|------------------|--------------------|----------------------------|------------------|--------------------------|------------------|--------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  | **Contact Agent**  | **Organization Agent**     | **Actuator Agent** | **Organization Agent**   | **Actuator Agent** | **Organization Agent**   | **Actuator Agent** |   **Philosopher Agent**      |                                                                                                                                                                                                                                                                                        |
| **Flexibility**  | YES                | YES                        | YES              | YES                      | YES              | YES                      | YES              | YES  |
| **Reactivity**   | YES                | YES                        | YES              | YES                      | YES              | YES                      | YES              | YES  |
| **Proactiveness**| NO                 | YES                        | YES              | YES                      | YES              | YES                      | YES              | NO  |
| **Social Ability** | YES             | YES                        | YES              | YES                      | YES              | YES                      | YES              | YES |
| **Rationality**  | YES                | YES                        | YES              | YES                      | YES              | YES                      | YES              | YES  |
| **Reasoning**    | YES                | YES                        | LESS             | YES                      | LESS             | YES                      | LESS             | YES   |
| **Learning**     | NO                 | NO                         | NO               | NO                       | NO               | NO                       | NO               | NO |
| **Autonomy**     | HIGH               | HIGH                       | LOW              | HIGH                     | LOW              | HIGH                     | LOW              | HIGH  |
| **Temporal continuity** | YES        | YES                        | YES              | YES                      | YES              | YES                      | YES              | YES |
| **Mobility**     | NO                 | NO                         | YES              | NO                       | YES              | NO                       | YES              |  NO |

### 3.3 Property Justification
#### 3.3.1 Flexibility
All agents = YES

Essential in emergency response where situations are dynamic and unpredictable.
Agents must adapt to changing circumstances (new fires, resource constraints, casualties).  
Even with predefined protocols, flexibility allows for situational adaptation.

#### 3.3.2 Reactivity
All agents = YES

All agents must respond to changes in their environment.  
Emergency situations are inherently unpredictable and require immediate responses.
Examples: Contact Agent reacts to new reports, Organization Agents to resource changes, Actuators to field conditions.

#### 3.3.3 Proactiveness

Contact & Philosopher = NO

Only respond to incoming reports/queries.  
Cannot anticipate when emergencies will occur or when ethical guidance will be needed.


Organization & Actuator = YES

Must anticipate potential scenarios and prepare accordingly.  
Example: Organization Agent preparing backup plans, Actuators positioning for better response.

#### 3.3.4 Social Ability
All agents = YES

Essential for coordination in a multi-agent system.  
Emergency response requires constant communication between all levels.
Information must flow smoothly between planning and execution.

#### 3.3.5 Rationality
All agents = YES

All decisions must be based on logical evaluation of available information.  
Critical in emergency situations where resources and time are limited.  
Ensures consistent and justifiable decision-making.

#### 3.3.6 Reasoning

Contact, Organization, Philosopher = YES

Required for complex decision-making and planning.  
Must process multiple variables and constraints.  


Actuator = LESS

Follows pre-defined plans with limited decision-making scope.  
Only needs basic reasoning for immediate field decisions.  



#### 3.3.7 Learning
All agents = NO

System relies on predefined protocols for consistency.  
Emergency response requires predictable, reliable behavior.  
Learning could introduce unpredictability in critical situations.  

#### 3.3.8 Autonomy

Contact, Organization, Philosopher = HIGH

Need independence to make complex decisions.  
Must handle multiple scenarios without constant oversight.  


Actuator = LOW

Follows organization agent's plans.  
Limited decision-making scope to ensure plan consistency.  



#### 3.3.9 Temporal Continuity
All agents = YES

Emergency response system must operate continuously.  
No agent can have "downtime" as emergencies can occur anytime.  
System must maintain readiness 24/7.

#### 3.3.10 Mobility

Contact, Organization, Philosopher = NO

Operate from fixed command/control positions.  
Focus on planning and coordination.  


Actuator = YES

Must physically respond to emergencies.  
Requires movement to execute plans in the field.  


## Bibliography

[1] Wooldridge (2002). An Introduction to Multiagent Systems   
[2] Zou, W. (2023). Overview on reinforcement learning of multi-agent game. In Journal of Physics: Conference Series (Vol. 2646, 012021). IOP Publishing   
[3] Russell, S.J. and Norvig, P. (2009) Artificial Intelligence. Upper Saddle River, N.J: Pearson Education.  
[4] Balaji, P.G., Srinivasan, D. (2010). An Introduction to Multi-Agent Systems. In: Srinivasan, D., Jain, L.C. (eds) Innovations in Multi-Agent Systems and Applications - 1. Studies in Computational Intelligence, vol 310. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-642-14435-6_1