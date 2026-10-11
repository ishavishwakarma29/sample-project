# Sample Project

This is a simple Python Flask application that demonstrates a small task tracker web app with a REST API.

## Features
- View a list of sample tasks
- Add new tasks from the UI
- Toggle task completion status
- Delete tasks
- API endpoints for CRUD-style operations

## Tech Stack
- Python 3
- Flask

## Project Structure
- `app.py` — Flask server and API
- `templates/index.html` — web UI
- `static/style.css` — page styling
- `requirements.txt` — Python dependencies

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open the app in your browser:
   ```text
   http://localhost:5000
   ```

## API Endpoints
- `GET /api/items` — list all tasks
- `POST /api/items` — create a task
- `PUT /api/items/<id>/toggle` — toggle completion
- `DELETE /api/items/<id>` — delete a task

## Notes
This sample project is intentionally simple and beginner-friendly. It is designed to be easy to extend for learning and demos.
