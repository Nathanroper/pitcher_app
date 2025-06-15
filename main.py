#!/usr/bin/env python3
 
import subprocess
import sys
 
def prompt(text: str) -> str:
    """Prompt the user and return their input."""
    return input(text).strip()
 
def main():
    # Collect inputs
    first_name = prompt("Pitcher first name: ")
    last_name  = prompt("Pitcher last name: ")
    start_date = prompt("Start date (YYYY-MM-DD): ")
    end_date   = prompt("End date   (YYYY-MM-DD): ")
 
    # Build the command to call run_summary.py
    cmd = [
        sys.executable,                # ensures we use the same Python interpreter
        "run_summary.py",              # your existing script
        "--first-name", first_name,
        "--last-name",  last_name,
        "--start-date", start_date,
        "--end-date",   end_date
    ]
 
    # Execute it
    subprocess.run(cmd, check=True)
 
if __name__ == "__main__":
    main()