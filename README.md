# Optimization of Disaster Resource Distribution

## Project Overview
This project focuses on the **optimization of disaster resources' distribution** using Artificial Intelligence techniques, particularly search algorithms. The system aims to maximize efficiency in delivering supplies to zones affected by natural disasters, considering constraints such as vehicle capacities, time, and environmental conditions. Implemented in Python, the project employs both informed and uninformed search strategies to address real-world constraints dynamically.

## Features

### Core Functionalities
- **Graph Representation**:
  - Nodes represent zones, including attributes like severity, population, and geographic coordinates.
  - Edges represent routes with attributes such as cost, geography, and availability.
- **Dynamic Conditions**:
  - Simulates environmental changes such as blocked roads or adverse weather.
  - Adjusts paths dynamically based on real-time conditions.
- **Vehicle Constraints**:
  - Incorporates vehicle-specific attributes like capacity, autonomy, and type (e.g., drone, truck).
- **Priority System**:
  - Assigns priorities to zones based on severity and population density.

### Algorithms
- **Uninformed Search**:
  - BFS (Breadth-First Search): Guarantees shortest paths in unweighted graphs.
  - DFS (Depth-First Search): Explores deep paths efficiently but may produce suboptimal results.
- **Informed Search**:
  - Greedy Search: Utilizes heuristics for faster, though suboptimal, solutions.
  - A*: Balances cost and heuristic to ensure optimal paths.
  - Dynamic A*: Adapts to environmental changes in real-time, ensuring robustness.

### Visualization and Metrics
- Portugese graph visualization using NetworkX and Matplotlib.
- Metrics include:
  - Execution time.
  - Memory usage.
  - Zones visited and their priority.
  - Path cost and depth.

## Repository Structure
```
.
├── Makefile
├── README.md
├── core
│   ├── __init__.py
│   ├── road.py
│   ├── vehicle.py
│   └── zone.py
├── docs
│   ├── IA TP 2425.pdf
│   └── report.pdf
├── enums
│   ├── __init__.py
│   ├── conditions.py
│   ├── geography.py
│   ├── infrastructure.py
│   ├── severity.py
│   └── vehicle_type.py
├── graph
│   ├── __init__.py
│   ├── algorithms
│   │   ├── __init__.py
│   │   ├── a_star.py
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   ├── greedy.py
│   │   └── heuristic.py
│   └── graph_builder.py
├── main.py
├── map
│   ├── README.md
│   ├── assets
│   │   └── preview.png
│   ├── data
│   │   └── before
│   │       ├── data.zip
│   │       └── municipalities_population.csv
│   └── src
│       ├── data_manipulation
│       │   ├── centroide.py
│       │   ├── final.py
│       │   ├── final_json.py
│       │   ├── fronteirs.py
│       │   └── parser.py
│       ├── plot_portugal_graph.py
│       └── run_all.py
├── metrics
│   └── metrics.py
└── utils
    ├── __init__.py
    ├── coordinate.py
    ├── graph_generator.py
    ├── graph_visualizer.py
    ├── menu.py
    └── name_generator.py
```

## Setup and Execution
### Prerequisites
- Python 3.8 or later
- Required Python libraries:
  ```bash
  pip3 install -r requirements.txt
  ```

### Execution
1. **Ensure the dataset is present**
A `data.zip` file **must** be placed inside the **map/data/before** directory, containing relevant information regarding the Portuguese graph structure. A link to transfer the `data.zip` file is located [here](https://www.swisstransfer.com/d/956ed240-5a6c-42a1-a44f-5937c02ac678) — expires on 2/2/2025. If you wish to use the project and download the `data.zip` file after expiry, contact [Eduardo Faria](https://www.github.com/2101dudu).

2. **Compile the program**
   ```bash
   make build
   ```
3. **Run the program**
   ```bash
   make run
   ```

## Results and Analysis
### Key Insights
- **Dynamic A***
  - Adapts effectively to real-time changes, providing robust solutions.
  - Balances memory usage and computational efficiency.
- **Visualization**
  - Highlights blocked paths and prioritized zones.
- **Metrics**
  - Demonstrates the trade-offs between uninformed and informed search strategies.

## Group Members - Group 1
- [Eduardo Faria](https://www.github.com/2101dudu)
- [Hélder Gomes](https://www.github.com/helderrrg)
- [Nuno Silva](https://www.github.com/NunoMRS7)
- [Pedro Pereira](https://www.github.com/pedrofp4444)
