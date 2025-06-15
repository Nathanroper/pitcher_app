# pitcher_app
Summary of pitcher performance

# What do the files in this project do/mean?

### run_summary.py:
Entry-point script that parses command-line arguments (pitcher name and date range), orchestrates data fetching and cleaning, and invokes plotting functions to generate the summary graphics.
 
### src/pitching_summary/data_processing.py:
Module containing functions to lookup the pitcher’s MLBAM ID, fetch raw Statcast data via PyBaseball, and clean/process the DataFrame for plotting.
 
### src/pitching_summary/plotting_functions.py:
Module defining global plotting styles and functions to create and save visualizations of pitch break and pitch zone, including configuration of color palettes and figure settings.
 
### src/pitching_summary/__init__.py:
Initializes the pitching_summary package, making its modules importable.
 
### requirements.txt:
Lists all Python dependencies with version pins required to reproduce the environment described in the Medium article.
 
### .gitignore:
Specifies files and directories for Git to ignore (e.g., virtual environment directory, cache folders, and Python bytecode).