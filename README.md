# Terminal or Fork

This project, `terminal-or-fork.py`, is a Python script designed to provide an interactive shell experience within Google Colab's virtual machines. The script allows users to execute terminal commands directly from the Python environment. Additionally, it includes a demonstration of creating multiple processes using the `os.fork()` method, which could lead to a "fork bomb" if used recklessly.

**Disclaimer:** The `get_rekt()` function, which utilizes `os.fork()`, can cause a system to become unresponsive by spawning an excessive number of processes. It is included here for educational purposes and should not be executed on your local machine or any system where you do not have permission to experiment.

## Features

- **Interactive Shell**: Run terminal commands directly from a Python script.
- **Fork Bomb Demonstration**: Illustrates the potential danger of uncontrolled process creation using `os.fork()`.

## Why This Was Made

This script was created to enable the use of a terminal in Google Colab's virtual machines without requiring a paid membership. By using this interactive shell, users can execute shell commands without relying on Colab's limited native terminal access.

## Usage

### Running the Script

To use the interactive shell:

1. Download or clone this repository to your local machine or upload the `terminal-or-fork.py` script to your Google Colab notebook.

2. Run the script:

   ```bash
   python terminal-or-fork.py
   ```
3. Enter any terminal commands directly into the prompt provided by the interactive shell. To exit, type exit.

## Fork Bomb Warning
The script includes a get_rekt() function that, if executed, will cause the system to create an overwhelming number of processes, potentially leading to a crash. Do not run this function on any critical system. It is commented out by default.

## Example Commands
Here are a few example commands you can try in the interactive shell:

List files in the current directory:

Copy code
```bash
ls
```
Check the current working directory:

Copy code
```bash
pwd
```
Display the content of a file:

Copy code
```bash
cat filename.txt
```

### Notes
This script is intended for educational purposes. The get_rekt() function is a fork bomb and is included to illustrate the potential consequences of uncontrolled process creation.

Use this script responsibly, especially when working in a shared or virtual environment like Google Colab.

# MIT License

Copyright (c) [2024] [Shadowdrums]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


