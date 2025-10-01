# RP-Flask-Server

## Project Overview

RP-Flask-Server is a Flask-based application designed to handle data processing and machine learning models for the project. It is responsible for training and serving models to the backend server.

## How to Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/RP-Flask-Server.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd RP-Flask-Server
    ```

3. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Flask server**:
    ```bash
    python3 app/main.py
    ```

7. **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:8000/`.


## Folder Structure

```
RP-Flask-Server/
├── app/                    # Flask application
│   ├── __init__.py         # Entry point of the application
│   ├── models/             # ML models
│   ├── routes/             # API endpoint routing
│   └── tests/              # Unit and integration tests
├── venv/                   # Virtual environment
├── .gitignore              # Files and directories to ignore
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and usage guide
```

## Features

- Train and serve machine learning models.
- Provide API endpoints for data processing.

## Requirements

- Python 3.6+
- Flask 2.0.1+

## API Endpoints

- `GET /`: Returns a welcome message.

## Notes

- Ensure Python 3.6+ is installed on your system.
- Use the virtual environment to avoid dependency conflicts.
- Update the `requirements.txt` file if new dependencies are added.
- For any issues, refer to the project repository or contact the team.

