import subprocess
import os

main_dir = "map/data/before/data"

# List of scripts to run in order
    
scripts = [
    'map/src/data_manipulation/big_data/parser.py',
    'map/src/data_manipulation/big_data/centroide.py',
    'map/src/data_manipulation/big_data/fronteirs.py',
    'map/src/data_manipulation/big_data/final_json.py',
    'map/src/data_manipulation/big_data/final.py'
]

if os.path.exists(main_dir): # Run each script in order
    for script in scripts:
        print("\n==== Running " + script + " ====")
        subprocess.run(['python3', script], check=True)
else: print("Process interrupted: unzip the .zip file first")
