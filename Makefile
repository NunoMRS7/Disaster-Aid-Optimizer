# Makefile for project management

# Variables
DATA_DIR = map/data
AFTER_DIR = $(DATA_DIR)/after
BEFORE_DIR = $(DATA_DIR)/before
MAP_SRC = map/src

# Lists of files and directories to remove
JSON_FILES = $(wildcard $(BEFORE_DIR)/*.json)
GEOJSON_FILES = $(wildcard $(BEFORE_DIR)/*.geojson)
GEOJSON_DIR = $(BEFORE_DIR)/geojson
ZIP_FILE = $(BEFORE_DIR)/data.zip
UNZIPED_DIR = $(BEFORE_DIR)/data/

.PHONY: build all

# Default target
all: build run

# Build target
build: create_after_dir unzip compile

# Creates the directory data/after
create_after_dir:
	mkdir -p $(AFTER_DIR)

# Unzips the data.zip file into the data directory
unzip:
	unzip -o $(ZIP_FILE) -d $(BEFORE_DIR)

# Compiles the data
compile:
	python3 $(MAP_SRC)/run_all.py

# Run main
run:
	python3 main.py

# Cleans files and directories
clean:
	rm -f $(JSON_FILES) $(GEOJSON_FILES) 
	rm -rf $(GEOJSON_DIR) $(AFTER_DIR) $(UNZIPED_DIR)
