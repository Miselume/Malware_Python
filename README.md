# Malware Sample in the Python

**Warning**: This script contains malicious code and is intended for educational or research purposes only. Running it on a system without proper authorization and understanding of its functionality can lead to severe consequences, including data loss, system damage, and privacy breaches.

## Description:

This Python script performs the following actions:

- Hides its execution: It launches a web browser (Edge on Windows, Safari on macOS, Firefox on other systems) to disguise its activity.
- Converts files to Python: It scans the current directory and its subdirectories, converting files with various extensions to Python files (.py).
- Injects malicious code: It injects the contents of the current script into other Python files within the same directory structure, effectively propagating itself.
- Executes Python files: It runs all Python files (including those newly converted and infected) within the current directory and its subdirectories.

## Usage:

Do not run this script on any system without explicit permission and understanding of its potential impact.

For educational or research purposes, execute the script using Python 3:

   ```bash
   python3 main.py
   ```

## Licance:
MIT Licance

## Author:
Miselume
