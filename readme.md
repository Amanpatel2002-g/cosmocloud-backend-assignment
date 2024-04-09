# CosmoCloud Backend Assignment Documentation

This document provides an overview, setup instructions, and API documentation for the CosmoCloud Backend Assignment project.

## Overview

CosmoCloud Backend Assignment is a FastAPI-based backend application that serves as the backend for the CosmoCloud platform. It provides various endpoints to manage user data.

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
│   │   └── user_models.py
│   ├── services
│   │   └── user_services.py
│   ├── repository
│   │   └── user_repository.py
│   ├── main.py
│   └── .env
└── requirements.txt
```

- `app`: Contains the main application logic.
- `api`: Contains API routers for handling HTTP requests.
- `config`: Contains configuration files, including settings and constants.
- `models`: Contains data models for users.
- `services`: Contains business logic services for users.
- `repository`: Contains database repository functions for users.
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

Create a `.env` file in the project root directory and set the environment variables:

```plaintext
MONGODB_URI=mongodb://localhost:27017/
MONGODB_DB_NAME=cosmocloud_db
```

Replace the MongoDB URI and database name with your local MongoDB configuration.

### Step 7: Run the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will start running on `http://localhost:8000` by default.

## API Documentation

The following table summarizes the available API endpoints and their functionalities:

| Endpoint          | Method | Description                                 |
|-------------------|--------|---------------------------------------------|
| `/users`          | GET    | Get a list of all users.                    |
| `/users/{user_id}`| GET    | Get user details by user ID.                |
| `/users`          | POST   | Create a new user.                          |
| `/users/{user_id}`| PUT    | Update user details by user ID.             |
| `/users/{user_id}`| DELETE | Delete user by user ID.                     |

Detailed descriptions of each endpoint:

- **GET `/users`**: Retrieves a list of all users stored in the database.
- **GET `/users/{user_id}`**: Retrieves the details of a specific user identified by the user ID.
- **POST `/users`**: Creates a new user with the provided user data.
- **PUT `/users/{user_id}`**: Updates the details of a user identified by the user ID with the provided data.
- **DELETE `/users/{user_id}`**: Deletes the user identified by the user ID from the database.

---

This documentation provides an overview of the CosmoCloud Backend Assignment project, setup instructions, and API documentation. Customize it as needed for your project.
