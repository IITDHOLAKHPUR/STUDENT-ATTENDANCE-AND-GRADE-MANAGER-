# Student Attendance and Grade Manager

## Problem Statement

Managing student attendance and academic marks manually can be time-consuming and may lead to calculation errors.

The Student Attendance and Grade Manager is a Python-based program designed to manage basic student information, attendance, marks, grades, and student reports.

The system provides a menu-driven interface through which the user can add students, view and search student records, record attendance, enter marks, calculate grades, and generate a student report.

The project demonstrates problem-solving, functions, conditional statements, loops, lists, dictionaries, and modular programming concepts covered in CSE1021 Introduction to Problem Solving and Programming.

## Objectives

1. To store and manage student names and roll numbers.
2. To record and calculate student attendance percentages.
3. To store student marks and calculate grades.
4. To provide a simple menu-driven system for managing student records.
5. To generate a basic report containing student attendance, marks, and grade.
6. To apply Python programming concepts such as functions, loops, conditional statements, lists, and dictionaries.

## Functional Requirements

1. The system shall allow the user to add student details.
2. The system shall allow the user to view all registered students.
3. The system shall allow the user to search for a student using the roll number.
4. The system shall allow the user to enter attendance details.
5. The system shall calculate the attendance percentage.
6. The system shall allow the user to enter marks.
7. The system shall calculate the student's grade based on marks.
8. The system shall generate a student report containing available academic information.
9. The system shall prevent duplicate roll numbers.
10. The system shall validate marks and attendance input.

## Non-Functional Requirements

1. The system should be simple and easy to use.
2. The system should provide clear messages for valid and invalid inputs.
3. The system should respond quickly to user commands.
4. The program should be organized into separate Python modules.
5. The code should be readable and maintainable.
6. The system should perform basic input validation to reduce errors.

## System Architecture

The project is divided into separate Python modules. Each module performs a specific task.

### Modules

- `main.py` — Controls the menu and program flow.
- `data.py` — Stores the student data.
- `student.py` — Adds, views, and searches students.
- `attendance.py` — Records and calculates attendance.
- `marks.py` — Records marks and calculates grades.
- `reports.py` — Generates student reports.
- `validation.py` — Validates marks and attendance inputs.

### Basic Flow

User
↓
`main.py`
↓
Student / Attendance / Marks / Reports
↓
`data.py`
↓
Student Information


## Process Workflow

1. The program starts.
2. The main menu is displayed.
3. The user selects an operation.
4. The selected module performs the required task.
5. Student information is stored in the program's data structure.
6. The result is displayed to the user.
7. The program returns to the main menu.
8. The user can continue using the system or choose Exit.


## Design Rationale

The project is divided into multiple Python modules so that each module has a specific responsibility. This makes the program easier to understand, test, and maintain.

A dictionary is used to store information related to each student, while a list is used to maintain multiple student records.

Functions are used to divide the program into smaller tasks such as adding students, recording attendance, entering marks, calculating grades, and generating reports.

Conditional statements and loops are used for decision-making, repetition, searching, and validation.

