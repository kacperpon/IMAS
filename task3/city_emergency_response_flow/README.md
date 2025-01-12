# City Emergency Response Flow

A multi-agent system for handling city emergency responses using CrewAI framework. The system coordinates between emergency services (fire, medical, police) to respond to urban emergencies effectively.

## Features

- Emergency situation assessment and response coordination
- Multi-phase emergency response handling
- Integration with OpenStreetMap data using OSMnx
- Ethical decision-making support
- Dynamic resource allocation
- Route optimization for emergency vehicles

## Prerequisites

- Python 3.12
- Poetry package manager

## Poetry Installation

### 1. Check if Poetry is Already Installed

Run the following command to check if Poetry is installed:

```bash
poetry --version
```

### 2. Install Poetry

If Poetry is not installed, use the official installer instructions:

```bash
https://python-poetry.org/docs/#installation
```

Ensure Poetry is accessible by being contained in the system's PATH.

Reload your shell configuration:

```bash
source ~/.bashrc
```

### 3. Verify Installation

Check that Poetry is installed and working:

```bash
poetry --version
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/kacperpon/IMAS.git
cd city_emergency_response_flow
```

2. Set up the Python environment with Poetry:

```bash
poetry env use python3.12
poetry install
```

## Usage

### Running the Emergency Response Simulation

Start the emergency response flow:

```bash
poetry run crewai flow kickoff
```

### Selecting the test-case

Change the last parameter of the path in main.py in line 35 to either "initial_report_01.md" or "initial_report_02.md" or "initial_report_03.md". The test-cases mentioned in the report incorporate the second and the third file.

###  Selection Ollama model and server

Change the configuration parameters at `task3/city_emergency_response_flow/src/city_emergency_response_flow/config/config.properties` to change the Ollama server location and Ollama LLM model for all the Crews.

## Project Structure

```
city_emergency_response_flow/
├── pyproject.toml         # Project dependencies and configuration
├── README.md             # This file
├── notes.md              # Development notes and documentation
└── src/
    └── city_emergency_response_flow/
        ├── crews/       # Crew implementations
        ├── tools/        # Custom tools for agents
        └── main.py       # Entry point
```

## Key Components

- **Emergency Crew**: Handles initial response coordination
- **Firefighting Crew**: Handles fire suppression and rescue
- **Medical Crew**: Provides medical assistance and transport
- **Police Crew**: Manages traffic and evacuation
