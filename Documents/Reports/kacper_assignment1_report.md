**1. Environment Analysis**
**1. Agent Selection and Definition**
**1. Agent Taxonomy**


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