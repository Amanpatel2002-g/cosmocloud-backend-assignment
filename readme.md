# CosmoCloud Backend Assignment Documentation

This document provides an overview, setup instructions, and API documentation for the CosmoCloud Backend Assignment project.

## Overview

CosmoCloud Backend Assignment is a FastAPI-based backend application that serves as the backend for the CosmoCloud platform. It provides various endpoints to manage student data.

### Project Structure

```
.
├── app
│   ├── api
│   │   └── routers.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── constants.py
│   │   └── settings.py
│   ├── models
│   │   └── student_models.py
│   ├── services
│   │   └── student_services.py
│   ├── repository
│   │   └── student_repository.py
│   ├── main.py
│   └── .env
└── requirements.txt
```

- `app`: Contains the main application logic.
- `api`: Contains API routers for handling HTTP requests.
- `config`: Contains configuration files, including settings and constants.
- `models`: Contains data models for students.
- `services`: Contains business logic services for students.
- `repository`: Contains database repository functions for students.
- `main.py`: Entry point for the FastAPI application.
- `.env`: Environment variables configuration file.
- `requirements.txt`: File containing required Python dependencies.

## Local Setup

Follow the steps below to set up the project locally:

### Prerequisites

- Python 3.6 or higher installed on your system.
- MongoDB installed and running on your local machine.

### Step 1: Clone the Repository

Clone the project repository to your local machine using Git:

```bash
git clone https://github.com/your-username/cosmocloud-backend-assignment.git
```

### Step 2: Navigate to the Project Directory

Navigate to the project directory:

```bash
cd cosmocloud-backend-assignment
```

### Step 3: Create a Virtual Environment

Create a virtual environment for the project:

```bash
python3 -m venv venv
```

### Step 4: Activate the Virtual Environment

Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS and Linux:

```bash
source venv/bin/activate
```

### Step 5: Install Dependencies

Install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 6: Set Environment Variables

Create a `.env` file in the project root directory by copying the contents from `.env.example` file:

```plaintext
cp .env.example .env
```

Then, open the `.env` file and update the values of environment variables as per your local environment. Make sure to set the MongoDB URI and database name accordingly:

```plaintext
MONGODB_URI=mongodb://localhost:27017/
MONGODB_DB_NAME=cosmocloud_db
```

Replace the MongoDB URI and database name with your local MongoDB configuration. Ensure that sensitive information such as passwords and secret keys are kept confidential and not shared publicly.

### Step 7: Run the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will start running on `http://localhost:8000` by default.

## API Documentation

The following table summarizes the available API endpoints and their functionalities:

| Endpoint             | Method | Description                                    |
|----------------------|--------|------------------------------------------------|
| `/students`          | GET    | Get a list of all students.                   |
| `/students/{student_id}`| GET  | Get student details by student ID.            |
| `/students`          | POST   | Create a new student.                         |
| `/students/{student_id}`| PUT | Update student details by student ID.          |
| `/students/{student_id}`| DELETE | Delete student by student ID.                 |

Detailed descriptions of each endpoint:

- **GET `/students`**: Retrieves a list of all students stored in the database.
- **GET `/students/{student_id}`**: Retrieves the details of a specific student identified by the student ID.
- **POST `/students`**: Creates a new student with the provided student data.
- **PUT `/students/{student_id}`**: Updates the details of a student identified by the student ID with the provided data.
- **DELETE `/students/{student_id}`**: Deletes the student identified by the student ID from the database.

---

This documentation provides an overview of the CosmoCloud Backend Assignment project, setup instructions, and API documentation. Customize it as needed for your project.
