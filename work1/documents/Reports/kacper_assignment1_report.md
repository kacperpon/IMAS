**1. Environment Analysis**
**1. Agent Selection and Definition**
**1. Agent Taxonomy**

1. Flexibility: Agents can adapt to changes in the environment. For example, if an agent is called to a fire, and a fire with greater severity occurs while the agent is on route, they can be re-routed. 

Also, agents need to be flexible regarding road-closures if a fire is present -> agent cannot respond to another fire by driving past an on-going fire.

2. Reactive: Same as above?

3. Proactiveness: Agents should react to the changes in the environment (new fires) themselves, by suggesting recommendations and suggestions (directing to fires). 

Need communication between agents for them to be proactive.

4. Social Ability: Agents have the ability to communicate amongst themselves -> imperative for creating an optimal solution. 

5. Rationality: Agent needs to act in a way to achieve it's goals -> imperative also. Cannot have agents doing random actions -> not helpful.

6. Reasoning: Ability to infer and extrapolate information based on current environment knowledge -> also very important. Agents cannot be flexible and proactive without the ability to reason and make plans.

7. Learning: Agent can improve their behaviour and responses to problems based on previous knowledge. Could be useful but not essential for the solution.

8. Autonomy: Agents can pursue goals autonomously -> don't need to be told what to do directly. Given they can communicate amongst themselves, we want this.

9. Temporal continuity: Continuously running processes -> yes. Need to be on standby ready to react to a new fire.

10. Mobility: Can be executing in a given computer and move through a network into a different computer -> not needed.

---

<h4>Notes</h4>


**Environment:** Use OSMnx, DO NOT use same map as from lab exercises.

Preferably find map with varying degree of difficulty (i.e.: size, 1-one streets if possible)
Map with geographical challenges such as river or mountains / hills.

Tool: need to find out how this works. Do we create ourselves?
    -> "or an improved version of it" -- how do we improve it?


**Inputs:** 

Variables:
ESSENTIALS:
- Fire type (e.g.: ordinary, electrical, gas, etc...)
- X location
- Y location
- Injured people (#)
- Fire severity

COULD ALSO INCLUDE:
- Injured person severity: scale of how bad the injury for each injured person is
- and more?

Gotten from a markdown file


Information on the objects (ambulance, fire trucks, hospitals):
ESSENTIALS:
- Id (name)
- X location
- Y location

Also include more personalised information for each.

For fire trucks and ambulance could include:
- type of fire truck,
- Accessories included (ladder? tools? etc...)
- Capacity

For hospital could include:
- capacity for ppl (beds)
- can it deal with all injury severities? (if applicable)
- capacity for workers / ambulances

Also: does a certain injury severity need a bed? E.g.: minor burns should not occupy a bed for someone severely injured.
--> for this we could have medical centres but not hospitals.

**Agent Crews**
- Emergency service: notifies firemen and medical services about incident.
- Firemen: distributes units as required -> must be optimal for the incident to not waste resources
- Medical services: coordinates medical centres and ambulances optimally based on ppl distribution and distance. Also optimal choice for ambulances.