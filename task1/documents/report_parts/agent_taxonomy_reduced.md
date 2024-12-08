## 3.  Agent Taxonomy Analysis

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