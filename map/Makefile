# Makefile for project management

# Variables
DATA_DIR = data
AFTER_DIR = $(DATA_DIR)/after
BEFORE_DIR = $(DATA_DIR)/before

# Lists of files and directories to remove
JSON_FILES = $(wildcard $(BEFORE_DIR)/*.json)
GEOJSON_FILES = $(wildcard $(BEFORE_DIR)/*.geojson)
GEOJSON_DIR = $(BEFORE_DIR)/geojson
ZIP_FILE = $(BEFORE_DIR)/data.zip
UNZIPED_DIR = $(BEFORE_DIR)/data/

.PHONY: all clean unzip compile plot

# Default target
all: create_after_dir unzip compile

# Compiles the data
compile:
	python3 src/run_all.py

# Plots the graph
plot:
	python3 src/plot_portugal_graph.py
	
# Plots the graph with labels
plot-labels:
	python3 src/plot_portugal_graph.py --show-labels

# Creates the directory data/after
create_after_dir:
	mkdir -p $(AFTER_DIR)

# Unzips the data.zip file into the data directory
unzip:
	unzip -o $(ZIP_FILE) -d $(BEFORE_DIR)

# Cleans files and directories
clean:
	rm -f $(JSON_FILES) $(GEOJSON_FILES) 
	rm -rf $(GEOJSON_DIR) $(AFTER_DIR) $(UNZIPED_DIR)
