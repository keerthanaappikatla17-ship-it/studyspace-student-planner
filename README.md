# StudySpace – Student Planner

A simple and user-friendly web application that helps students organize study tasks, manage deadlines, and track their progress.

## Features

- **Task Management:** Add, edit, and delete study tasks.
- **Deadline Tracking:** Set deadlines and identify overdue tasks.
- **Priority Management:** Organize tasks by High, Medium, and Low priority.
- **Task Status:** Mark tasks as completed or pending.
- **Search and Filters:** Search tasks and filter by completion status.
- **Progress Dashboard:** View total, pending, and completed tasks with a progress bar.
- **Data Persistence:** Store tasks using an SQLite database.
- **Responsive Design:** Use the dashboard on desktop and mobile screens.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

## Project Structure

```text
Student Planner/
├── app.py
├── templates/
│   ├── index.html
│   └── edit.html
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd "Student Planner"
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Flask

```bash
python -m pip install flask
```

### 5. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## How It Works

Users can create study tasks with deadlines and priority levels. The dashboard displays task statistics and completion progress. Tasks can be edited, completed, searched, filtered, or deleted. SQLite stores task information locally.

## Future Enhancements

- User registration and login
- Calendar view for deadlines
- Study reminders and notifications
- Weekly productivity reports

## Author

Developed as a student productivity project to practice Python web development and database integration.