# Portugal Municipalities Graph Visualization

## Overview
This project visualizes the municipalities (concelhos) of Portugal using a graph structure. Each node represents a concelho, and the edges represent connections based on geographical distances. Node sizes are proportional to the population of each municipality.

## Preview
![preview image](assets/preview.png)

## Features
- Fetches municipality data from a .zip file.
- Visualizes the graph using NetworkX and Matplotlib.
- Node sizes are dynamically scaled based on the population.
- Option to show or hide node labels.

## Installation
To run this project, make sure you have Python 3.x installed. You will also need the following libraries:
- `networkx`
- `matplotlib`
- `numpy`
- `requests`
- `geopandas`

### Steps
```bash
git clone git@github.com:2101dudu/PortugueseGraph.git
cd PortugalGraph
```

You can install the required packages using pip:

```bash
pip install networkx matplotlib numpy requests geopandas
```

## Usage
1. Unzip, compile and run the project:
```bash
make 
make [plot/plot_labels]
```
2. Or do it step by step:
```bash
make create_after_dir
make unzip
make compile
make [plot/plot_labels]
```

## Data Sources
- CAOP, provided by @pedrofp4444
