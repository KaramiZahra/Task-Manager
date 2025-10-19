# Task Manager (Flask)

A simple **web-based Task Manager** built with **Flask** and **SQLAlchemy**.
This app allows you to **add**, **view**, **edit**, **delete**, and **toggle task completion** with data stored in a **SQLite database**.

## Features

- Add new tasks
- View all tasks in a clean web interface
- Edit existing tasks
- Delete tasks
- Toggle completion status (done / not done)
- Persistent storage using **SQLite + SQLAlchemy**
- Clean MVC-like structure using Flask routes and templates

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/KaramiZahra/Task-Manager
   cd Task-Manager
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate   # macOS/Linux
   env\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip3 install flask flask-sqlalchemy
   ```

4. **Run the app**

   ```bash
   python3 app.py
   ```

Then open your browser and go to **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** 

## Usage

- Type a new task in the input box and click **Add Task**.
- View all your tasks in a table.
- Click **Edit**, **Delete**, or **Change Status** to update each task.
- Completed tasks toggle between ✔️ and ✗.

## Project Structure

```
Task-Manager/
│
├── app.py                # Main Flask application
├── instance/
│   ├── project.db        # SQLite database (auto-created)
├── templates/
│   ├── base.html
│   ├── index.html        # Home page (list + add tasks)
│   └── edit.html         # Edit task form
├── static/
│   └── styles.css        # CSS styling
├── requirements.txt      # Packages
└── README.md             # Documentation
```

---

## Model Overview

### `Task`

Represents a single task in the database.

**Attributes:**

- `id`: unique task ID
- `content`: text description of the task
- `status`: boolean (completed or not)

## Routes Overview

| Route          | Method     | Description                     |
| -------------- | ---------- | ------------------------------- |
| `/`            | GET / POST | Show all tasks or add a new one |
| `/delete/<id>` | GET        | Delete a task                   |
| `/edit/<id>`   | GET / POST | Edit an existing task           |
| `/change/<id>` | GET        | Toggle completion status        |
