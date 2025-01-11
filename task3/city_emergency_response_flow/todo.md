# TODOS

## Priority 1

- [x] firefighting crew first implementation
- [ in progress ] medical crew first implementation
    - [x] hospital info in file (hospital tier, capacity, location)
    - [x] first voting in text, improve task description
    - [ ] second voting in text, improve task description
    - [ ] tool to sum to votes as input to the last task.
    - [ ] vehicle selection revision for medical crew?

- [ ] police crew first implementation
- [ ] final plan collection first implementation

- [x] implement osmnx route calculation
- [ ] Leverage ethical issues (probably in initial report)

---

- [x] resolve how the emergency crew can be called in the beginning and in the end
- [x] Check if the contexts really work
- [x] add context field to each fire-task whenever depending on previous task
- [x] add context field to each medical-task whenever depending on previous task
- [x] add context field to each police-task whenever depending on previous task
- [x] include medical information to each task
- [x] include police information to each task

## Priority 2

- [ ] change ambulance routes to go from emergency to hospitals, not from ambulance pos to emergency??
- [ ] output route statistics such as duration, etc.
- [ ] format all crews outputs in the same way (tell llm to "output as markdown with heading 1 being…")
- [ ] check initial report if works with ONLY natural language (no bulletpoints)

---

- [x] check all tasks regarding crewai-task-parameter "context" which might be beneficial

## Priority 3

- [ ] resolve the redundant declaration of @classmethod get_schema

---

## Report

- Show how we organised the code
- Explain all adjustments which we have done
- Use Cases at least for routing (1 with meds, 1 without)
- Include final output/results to report and talk about it (what couldve been better, whats going well, specific moments of particular interest)

---

## Presentation

- Show how we organised the code
- Explain all adjustments which we have done
- No execution during presentation
