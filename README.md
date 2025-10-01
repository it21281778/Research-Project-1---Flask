# RP-Flask-Server

## Project Overview

RP-Flask-Server will handle the data processing and machine learning models of the project. It will be responsible for training and serving the models to Backend Server

# How to run the project
1. Clone the repository:
    ```bash
    git clone

2. Navigate to the project directory:
    ```bash

3. Create a virtual environment:
    ```bash

4. Activate the virtual environment:
    - On Windows:
        ```bash

    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
          
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the Flask server:
    ```bash
     python3 app/main.py
    ```
7. Open your web browser and navigate to `http:// 

-- 
## Team details
- **Project Name**: 24-25J-293
- **Team Members**:

  - **Name**: Alwis P.K.D.L.W
    - **Student ID**: IT21281778

  - **Name**: De Alwis K.C
    - **Student ID**: IT21306204

  - **Name**: Ameen F.A 
    - **Student ID**: IT21377730

  - **Name**: Jahani M.J.A 
    - **Student ID**: It21346736

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

- Handle ML models of the project

## Requirements

- Python 3.6+
- Flask 2.0.1+

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/RP-Flask-Server.git
    ```
2. Navigate to the project directory:
    ```bash
    cd RP-Flask-Server
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask server:
    ```bash
    flask run
    ```
2. Open your web browser and navigate to `http://127.0.0.1:8000/` to see the server in action.

## API Endpoints

- `GET /`: Returns a welcome message.
