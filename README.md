# AI-Powered Resume Analyzer & Career Recommendation System

## Project Overview
An AI-powered backend application that analyzes uploaded resumes, extracts technical skills, matches candidates with job requirements, and recommends suitable career opportunities.

## Technologies Used
- Python
- Django
- Django REST Framework
- MySQL
- Google Gemini API
- JWT Authentication
- Git and GitHub

## Key Features
- User registration and authentication
- Resume upload (PDF and DOCX)
- Automatic resume text extraction
- Technical skill identification
- Resume-to-job matching with percentage scores
- AI-powered resume analysis and suggestions
- Career recommendations
- RESTful API endpoints
- Swagger API documentation
- Role-based job and skill management

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Configure your MySQL database.
5. Add your environment variables in `.env`.
6. Run migrations using `python manage.py migrate`.
7. Start the server using `python manage.py runserver`.

## Environment Variables

Configure the following variables in your local `.env` file:

- `GEMINI_API_KEY`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

Never commit your actual credentials.

## API Documentation
Swagger: `http://127.0.0.1:8000/api/docs/`

## Developer
Python Full Stack Developer | Django | REST APIs | MySQL