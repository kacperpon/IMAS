# Overall notes for task3

## Differences to task2/task1

- Added new pydantic output for initial information which we did not mention in task2
- Emergency crew
  - Two different phases now
  - First task (schema): not distributed task anymore, instead simply distribution of information
  - First task (schema): additional field including boolean if med is required to use in router
  - Maybe not parsing distributed information after emergency phase 1 as natural text, instead as pydantic model??
- Medical Crew: new helper pydantic output classes to use durin hospital choosing and voting
