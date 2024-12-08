# Pydantic outputs

## 1. User Request input

```python
class UserRequest(BaseModel):
    fire_type: str  # "ordinary", "electrical", "gas", etc.
    x_location: float # OSMnx uses floats
    y_location: float
    injured_people: tuple[int, str] # int as id and str as severity/type of injury (3rd degree burn/ intoxication via smoke)
    fire_severity: str  # "low", "medium", "high"
    additional_info: Optional[str] = None  # Extra details about the incident
```

## 2. General Plan

```python
class GeneralPlan(BaseModel):
    plan_id: int
    fire_location: tuple[float, float]  # (x, y) coordinates
    estimated_severity: str  # "low", "medium", "high"
    involved_crews: list[str]  # "Firefighting", "Medical", "Police"
    timestamp: str
```

## 3. Firefighting Crew Plan

```python
class FirefightingPlan(BaseModel):
    fire_truck_ids: list[str]
    fire_type: str  # "ordinary", "gas", "electrical"
    fire_severity: str  # "low", "medium", "high"
    assigned_units: list[str] # "chemical-expert", "magma-man", etc.
    special_tools: Optional[list[str]] # e.g. CO2 cartridges for fires in server rooms
    action_details: str = Field(..., description='Brief description of the operation steps.')
```

## 4. Medical Crew Plan

```python
class MedicalPlan(BaseModel):
    ambulance_ids: list[str]
    hospital_ids: list[str] # ids of hospitals in a 10km?? radius
    hospital_capacities: list[int] # number of free beds in those hospitals
    injured_count: int
    triage_plan: str  # e.g., "prioritise severe cases"
    transport_details: Optional[str] = None  # extra details on logistics
```

## 5. Police Crew Plan

```python
class PolicePlan(BaseModel):
    patrol_car_ids: list[str]
    traffic_control_points: list[tuple[float, float]]  # coordinates of control points
    unit_allocation: list[tuple[int, tuple[float, float]]] # which car goes where, maybe redundant TODO
    crowd_management_plan: str = Field(..., description='Brief description of the operation plan.')
```

## 6. Ethical Consultation

```python
class EthicalConsultation(BaseModel):
    issue_description: str
    recommendation: str  # Ethical decision or resolution
    timestamp: str
```

## 7. Final Plan

```python
class FinalPlan(BaseModel):
    plan_id: int
    firefighting_plan: FirefightingPlan
    medical_plan: MedicalPlan
    police_plan: PolicePlan
    ethical_consultation: EthicalConsultation
    overall_status: str  # "ready", "in_progress", "completed"
    approval_status: str  # "approved", "pending_ethics"
    timestamp: str
```
