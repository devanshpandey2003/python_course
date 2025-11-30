# Assignment 4 – Files, Exceptions, and Errors in Python

This repository contains solutions for **Module 5: Files, Exceptions, and Error Handling in Python**.
The assignment includes two tasks:

- Task 1: Reading files and handling missing file errors
- Task 2: Writing, appending, and reading from a file

Both Python scripts are included in this repository along with this README file.

---

## 📌 Task 1: Read a File and Handle Errors

### Problem Statement

Write a Python program that:
- Opens and reads a text file named `sample.txt`
- Prints its content line by line
- Handles errors gracefully if the file does not exist

### Expected Behavior

**If `sample.txt` exists:**
```
(Contents of the file printed line by line)
```

**If the file does not exist:**
```
Error: The file 'sample.txt' does not exist.
```

### Learning Outcome
- Working with file I/O in Python
- Using try-except blocks to handle exceptions
- Displaying user-friendly error messages

---

## 📌 Task 2: Write and Append Data to a File

### Problem Statement

Write a Python program that:
- Takes user input and writes it to a file named `output.txt`
- Appends additional content to the same file
- Reads and displays the final content of the file

### Example

If the user enters 25, the output file content becomes:
```
Initial Input: 25
Appended Line 1
Appended Line 2
```

### Learning Outcome
- Writing data to files
- Appending new content
- Reading final output
- Understanding write modes (w, a, r)

---

## 📁 Repository Structure
```
📦 Assignment-4
│
├── file_handling.py
├── append_data.py
└── README.md
```
