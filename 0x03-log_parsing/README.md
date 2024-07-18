# 0x03. Log Parsing
This repository contains the implementation of a log parsing script, which reads logs from standard input and computes metrics such as total file size and the number of status codes. The task is part of the ALX Interview preparation series.

## Table of Contents
- Background Context
- Requirements
- Files
- Usage
- Example
- Author
## Background Context
In this project, we created a script that parses logs. The logs contain lines with information about HTTP requests. Our script reads these lines from standard input and computes metrics every 10 lines or when a keyboard interruption (CTRL+C) is received.

## Requirements
Allowed editors: vi, vim, emacs
All files should end with a new line
Python scripts must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(import("my_module").doc)')
All your functions should have a documentation (python3 -c 'print(import("my_module").my_function.doc)')
The code should use the PEP 8 style (version 1.7.*)
The script should not import any module that is not allowed
### Files
- 0-stats.py: The main Python script that parses the log lines, computes, and prints metrics.
## Usage
The script reads from standard input, which can be simulated by echoing lines into the script or using files. It will continuously read lines until interrupted and will print the metrics every 10 lines and upon termination.
To run the script:

```bash
./0-stats.py
`````
You can also pipe a file into the script:
```
```bash
cat log_file | ./0-stats.py```

## Author
Efa07 - GitHub

