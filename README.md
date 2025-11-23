# Pluto Fit Backend

A backend service for Pluto Fit, built with Python. This project provides RESTful APIs to support fitness-related features.

## Folder Structure

```
pluto-fit-backend/
├── modules/
│   ├── workouts/
│   ├── nutrition/
│   ├── users/                  # User management module
│   │   ├── user_controller.py  # Handles user-related endpoints
│   │   ├── user_service.py     # User business logic
│   │   ├── user_repo.py        # User data access
│   │   ├── user_model.py       # User database models
│   │   ├── user_schema.py      # User Pydantic schemas
│   │   ├── user_enums.py       # User-related enums
│   │   └── user_validator.py   # (Optional) User data validation
│   └── ...
├── core/
│   ├── config.py            # Application configuration
│   └── db.py                # Mongo Database connection and setup
├── requirements.txt
├── README.md
├── .env                     # Environment variables (e.g., secrets, DB URIs)
├── main.py                  # Entry point for the FastAPI application
└── ...
```

## Technology Stack

- **Python 3.x**
- **FastAPI**
- **PyMongo**

## Features

- Google authentication and authorization
- JWT-based authentication
- User management APIs
- Workout tracking APIs
- Nutrition tracking APIs
- Progress monitoring endpoints
- Modular and scalable codebase

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pluto-fit-backend.git
   cd pluto-fit-backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

## API Documentation

Interactive API documentation is available via Swagger UI. You can access the documentation at: http://localhost:8000/docs
