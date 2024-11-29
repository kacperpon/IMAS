IMAS PROJECT 


TASK 1 - MULTI-AGENT SYSTEM DESIGN



1. Environment Design
- Accessible vs. Inaccessible: The environment is accessible, as firefighters can reach the emergency sites, but certain areas may become temporarily inaccessible due to fire or structural damage.
- Deterministic vs. Non-Deterministic: The environment is non-deterministic. The behavior of fire, weather conditions, and the actions of individuals can change unpredictably. (CHECK WITH TEAM)
- Episodic vs. Non-Episodic: The environment is non-episodic. Each emergency situation is unique, and the agents must adapt to new conditions and challenges each time. (CHECK WITH TEAM)
- Static vs. Dynamic: The environment is dynamic. Conditions can change rapidly due to the spread of fire, changes in wind direction, or the arrival of new information.
- Discrete vs. Continuous: The environment is continuous. Firefighters must make real-time decisions based on continuous data inputs, such as temperature readings and smoke levels. 

2. Agent Selection and Definition
The MAS will consist of the following agents, inspired by real firefighter crews:

1. Incident Commander (IC):
   - Role: Oversees the entire operation, makes strategic decisions, and coordinates between different teams.
   - Tools: Communication devices, mapping software, and incident reporting tools.

2. Fire Suppression Crew (FSC):
   - Role: Directly engages with the fire to suppress it using hoses, extinguishers, and other equipment.
   - Tools: Fire hoses, water tanks, fire extinguishers, and protective gear.

3. Rescue Team (RT):
   - Role: Focuses on rescuing individuals trapped in dangerous situations.
   - Tools: Rescue tools (e.g., jaws of life), medical kits, and communication devices.

4. Logistics Coordinator (LC):
   - Role: Manages resources, supplies, and equipment needed for the operation.
   - Tools: Inventory management software, communication devices, and transport vehicles.

5. Safety Officer (SO):
   - Role: Ensures the safety of all personnel on-site and assesses risks.
   - Tools: Safety equipment, communication devices, and risk assessment tools.



3. Agent Taxonomy
Each agent can be classified based on their type and properties:

1. Incident Commander (IC)
   - Type: Facilitator and Collaborative Agent
   - Properties: High-level decision-making, coordination of multiple teams, and communication with external agencies.

2. Fire Suppression Crew (FSC)
   - Type: Collaborative Agent
   - Properties: Executes tasks in coordination with other agents, requires real-time data to adapt strategies, and operates under high-pressure conditions.

3. Rescue Team (RT)
   - Type: Collaborative Agent
   - Properties: Works closely with the FSC and IC, requires quick decision-making, and prioritizes human safety.

4. Logistics Coordinator (LC)
   - Type: Information Agent
   - Properties: Manages data related to resources, ensures availability of supplies, and communicates needs to the IC.

5. Safety Officer (SO)
   - Type: Facilitator and Interface Agent
   - Properties: Monitors safety conditions, interfaces with all teams to ensure compliance with safety protocols, and provides real-time feedback.

Summary
This design for a multi-agent system leverages the structure and roles found in real firefighter crews, ensuring effective coordination and response to emergencies. The environment is characterised as dynamic and non-deterministic, requiring agents to adapt quickly to changing conditions. Each agent is defined by its role and taxonomy, facilitating collaboration and efficient operation during emergency situations.

