# Taximeter - Factoría F5

## Description
This project simulates a digital taximeter using Python.
The program calculates the total fare of a taxi trip based on the time spent in two different states: stopped and moving.

## Features
- Fare calculation based on stopped and moving time
- Trip history generartion
- Logging system
- Password authentication
- Unit testing
- Object-oriented programming structure

## Project Structure
```text
project1-taximetro-Torok_Polito/
│
├── taximetro_esencial.py
├── taximetro_intermediate.py
├── taximetro_advanced.py
├── test_taximeter_intermediate.py
├── test_taximeter_advanced.py
├── trip_history.txt
├── taximeter.log
├──  README.md
└── consigna taxímetro.pdf
```

### File Description

- `taximetro_esencial.py` → Basic version of the taximeter. The code includes detailed comments to explain the program line by line and facilitate understanding for beginner programmers.

- `taximetro_intermediate.py` → Intermediate version with logging system, trip history generation and configurable fare rates stored in variables instead of hardcoded values.

- `taximetro_advanced.py` → Advanced version developed using an object-oriented programming approach. This version also includes an authentication system to control access to the running program.

- `test_taximeter_intermediate.py` → Automated tests created for the intermediate version of the project.

- `test_taximeter_advanced.py` → Automated tests adapted to the object-oriented structure used in the advanced version.

- `trip_history.txt` → Text file generated automatically to store trip information such as start date, end date, stopped time, moving time and total fare for internal company analysis and trip tracking.

- `taximeter.log` → Technical log file designed to register system events and facilitate monitoring, debugging and possible auditing processes.

## Installation
Clone the repository:
```bash
git clone https://github.com/Bootcamp-IA-MAD-P7/project1-taximetro-Torok_Polito.git
```

Enter the project folder:
```bash
cd project1-taximetro-Torok_Polito
```

## How to Run the Project

### Essential Version
```bash
python taximetro_esencial.py
```

### Intermediate Version
```bash
python taximetro_intermediate.py
```

### Advanced Version
```bash
python taximetro_advanced.py
```

## Available Commands
| Command | Description |
|---|---|
| start | Starts a new trip |
| stop | Changes the taximeter state to stopped |
| move | Changes the taximeter state to moving |
| finish | Ends the trip and calculates the final fare |
| exit | Closes the program |

## Running Tests

### Intermediate Version Tests
```bash
python -m unittest test_taximeter.py
```

### Advanced Version Tests
```bash
python -m unittest test_taximeter_advanced.py
```

## Concepts Practiced
- Python fundamentals
- Functions and methods
- Variables and conditionals
- Classes and objects
- Object-oriented programming
- File handling
- Logging systems
- Unit testing
- Authentication systems
- Git and GitHub
- Program organization
- Terminal interaction
- State management
- Code refactoring
- Command-line application development
- Software scalability concepts
- Configuration through variables
- Data persistence
- Debugging
- Error handling
- Software scalability concepts
- Configuration through variables
- Technical documentation
- Repository management
- Version control workflows

## Example Execution
```text
Enter password to access the taximeter: p7taximetro
Authentication successful. Welcome!

Enter command: start
Trip started. Initial state: 'stopped'.

Enter command: move
State changed to 'moving'.

Enter command: finish

-- Trip summary --
Stopped time: 10.2 seconds
Moving time: 25.4 seconds
Total fare: €1.47
```

## Possible Future Improvements

- Develop a graphical user interface (GUI) to make the application more user-friendly.
- Integrate a database to store trip history records.
- Dockerize the application to improve deployment and portability.
- Develop a web version of the application accessible through the internet.

## Author
Fernanda Torok Polito

Artificial Intelligence & Data Bootcamp – Factoría F5