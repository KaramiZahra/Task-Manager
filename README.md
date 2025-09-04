# To-Do List App (CLI)

A simple terminal-based To-Do List application built using Object-Oriented Programming (OOP) in Python. This app allows you to add, view, delete, and update tasks, with persistent storage using a JSON file.

## Features

- Add new tasks
- View all tasks with status (completed or not)
- Delete tasks
- Toggle task completion status
- Automatic ID reassignment after deletion
- Tasks are stored in a JSON file (todo.json)
- Fully object-oriented design using Task and Todolist classes

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/To-Do-List
cd To-Do-List
```

2. Make sure you have Python 3 installed.

## Usage

Run the game:

```bash
python app.py
```

Follow the menu prompts:

---To Do List Menu---

1. Show Tasks
2. Add Tasks
3. Remove Tasks
4. Change Tasks
5. Exit and Save

## Project Structure

```bash
To-Do-List/
│
├── app.py        # Main application code (Task and Todolist classes)
├── todo.json     # JSON file storing tasks (created automatically)
└── README.md     # Project documentation
```

## Classes Overview

### Task
Represents a single task with:
- id — unique identifier
- name — task description
- status — completion status
Methods:
- toggle_status() — change task completion
- display() — returns a formatted string for display
- to_dict() — convert to dictionary for JSON
- from_dict() — create Task object from dictionary

### Todolist
Manages a list of tasks:
- load_tasks() — load tasks from JSON file
- save_tasks() — save tasks to JSON file
- add_task(), delete_task(), change_status() — task operations
- show_tasks() — display tasks
- menu() — terminal menu for user interaction
