### Accessibility
- **Accessible vs Inaccessible**: The general city map is accessible to all agents, but certain areas will be defined as inaccessible. Each agent only knows their specific location, the severity and type of the fire, and the number of wounded individuals nearby. To get a complete view of the situation, agents must communicate and share information about these details.

### Determinism
- **Deterministic vs Non-Deterministic**: The environment is **Non-Deterministic**. Actions do not guarantee the same outcomes each time; probabilistic factors are at play. For instance, attempting to extinguish a fire might not always succeed, as conditions could cause the fire to persist or spread.

### Episodicity
- **Episodic vs Non-Episodic**: The environment is **Non-Episodic**. Since there is no training algorithm relying on distinct episodes (the system is based on pre-trained language models), the scenario runs continuously. However, each emergency report could be treated as an individual episode.

### Dynamism
- **Static vs Dynamic**: The environment is **Dynamic**. Fires can escalate over time, and the health of injured individuals may decline if they are not treated quickly.

### Continuity
- **Discrete vs Continuous**: The environment is **Continuous** in terms of the map and time. Agents can navigate freely along the X and Y coordinates. While the map and time are continuous, agent actions (e.g., moving, extinguishing fire) are discrete.
