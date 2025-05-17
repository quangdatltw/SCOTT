# SCOTT - Audio Streaming Service

SCOTT is a Django-based audio streaming platform that allows users to discover, play, and manage music.

## Technologies Used

- Django 5.0.4
- HTMX
- PostgreSQL (database)
- pydub (audio processing)
- python-dotenv (environment variables)

## Setup Instructions

### Prerequisites
- Python 3.12
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd SCOTT
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Database Setup

1. Apply migrations:
```bash
cd myProject
python manage.py migrate
```

2. Create an admin user:
```bash
python manage.py createsuperuser
```

### Running the Application

Start the development server:
```bash
python manage.py runserver
```

The application will be available at: http://127.0.0.1:8000/

The admin interface can be accessed at: http://127.0.0.1:8000/admin/

## Features

- User profiles with customizable details
- Artist profiles
- Music streaming
- Song, album, and playlist management
- Genre-based music categorization
- Search song, artist, album

## Models

- **UserProfile**: Extended user information including profile image
- **Artist**: Music creators linked to user profiles
- **Song**: Music tracks with metadata and streaming capabilities
- **Album**: Collections of songs by artists
- **Playlist**: User-created collections of songs


