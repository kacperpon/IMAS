# Agent Definitions for Fire Emergency Response System

**CHANGES**
- Added more info on tasks
- Properties field to highlight most important properties for each agent.
- Added additional tools.
- Added a rescue agent for firefighting crew.
- Added a driver agent for ambulance crew.


## 1. Emergency Crew
### Contact Agent:
- **Task:** 
  Receives emergency reports in natural language, parses and compiles data into JSON format, and passes it to organization agents. Consolidates individual crew plans into a global response plan. Handles ethical dilemmas by consulting the Ethics Crew and dispatches the final plan to respective crews for execution.
- **Type:** Facilitator
- **Properties:**
  - **Deliberative:** Creates global plans for execution.
  - **Social Ability:** Communicates with all crews and resolves conflicts or ethical dilemmas.
- **Tools:** FileReadTool, PlanCompilerTool

---

## 2. Ethics Crew
### Philosopher Agent:
- **Task:** 
  Resolves ethical dilemmas by consulting an ethics database (text file) using Retrieval-Augmented Generation (RAG). Provides a decision that balances crew priorities and safety considerations.
- **Type:** Facilitator
- **Properties:**
  - **Reasoning:** Processes complex ethical dilemmas.
  - **Rationality:** Ensures decisions align with ethical guidelines.
- **Tools:** FileReadTool, EthicsSolverTool

---

## 3. Firefighting Crew
### Organization Agent:
- **Task:** 
  Receives structured data from the Contact Agent, evaluates resource availability, and plans task distribution for fire suppression and rescue efforts. Monitors evolving situations and adjusts plans accordingly.
- **Type:** Facilitator
- **Properties:**
  - **Deliberative:** Creates task plans based on available resources and distances.
  - **Reactive:** Updates plans as emergencies evolve.
- **Tools:** DistanceMetricTool, ResourceAllocatorTool

### Firefighter Actuator Agents (x3):
- **Task:** 
  Executes the firefighting tasks assigned by the Organization Agent. Makes minor autonomous decisions when encountering unexpected obstacles (e.g., debris or blocked access).
- **Type:** Actuator
- **Properties:**
  - **Hybrid:** Combines following predefined plans with reactive behavior to handle localized challenges.
- **Tools:** FireExtinguishingTool, ObstacleAvoidanceTool

### Rescue Actuator Agents (x3):
- **Task:** 
  Rescues individuals trapped in hazardous areas as per the Organization Agent’s plan.
- **Type:** Actuator
- **Properties:**
  - **Hybrid:** Makes real-time decisions to bypass small obstacles or reprioritize rescues.
- **Tools:** VictimExtractionTool, ObstacleAvoidanceTool

---

## 4. Medical Crew
### Organization Agent:
- **Task:** 
  Organizes ambulance and medical responses. Assigns victims to the nearest available hospitals, ensuring optimal resource utilization. Plans ambulance routes and victim prioritization.
- **Type:** Facilitator
- **Properties:**
  - **Deliberative:** Allocates resources efficiently based on patient condition and distance.
- **Tools:** DistanceMetricTool, PatientPrioritizationTool

### Medical Actuator Agents (x3):
- **Task:** 
  Provide first aid and medical care to victims at the scene as directed by the Organization Agent.
- **Type:** Actuator
- **Properties:**
  - **Hybrid:** Autonomous in delivering immediate medical care but follows general plans.
- **Tools:** MedicalKitTool

### Driver Actuator Agents (x3):
- **Task:** 
  Drives ambulances to the scene and transports victims to hospitals.
- **Type:** Actuator
- **Properties:**
  - **Hybrid:** Follows planned routes but adapts to dynamic traffic conditions.
- **Tools:** AmbulanceNavigationTool

---

## 5. Police Crew
### Organization Agent:
- **Task:** 
  Plans alternative traffic routes, blocks roads near fire zones, and facilitates safe evacuation of civilians. Coordinates with other crews to prevent congestion.
- **Type:** Facilitator
- **Properties:**
  - **Deliberative:** Designs route changes and evacuation plans.
- **Tools:** DistanceMetricTool, TrafficManagerTool

### Patrol Actuator Agents (x3):
- **Task:** 
  Implements the traffic and evacuation plans. Sets up roadblocks, assists in evacuation, and directs traffic flow.
- **Type:** Actuator
- **Properties:**
  - **Hybrid:** Follows plans but adjusts for real-time changes like civilian behavior or unexpected obstacles.
- **Tools:** TrafficControlTool, EvacuationSupportTool
