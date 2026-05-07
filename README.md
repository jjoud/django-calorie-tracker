# CalorieTrack

CalorieTrack is a beginner-friendly Django web application for tracking daily calorie intake. Users can create an account, set a daily calorie goal, add foods to a simple food database, log meals, and view their calorie history.

## Features

- User registration and login using Django's built-in authentication system
- Personal daily calorie goal
- Food database with calories per serving
- Meal logging for authenticated users
- Dashboard with:
  - calories consumed today
  - remaining calories
  - daily progress percentage
- History page with calorie totals grouped by date
- Responsive HTML/CSS layout using Django templates
- Static CSS and JavaScript separated from templates

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript

## Project Structure

```text
calorietrack/
+-- manage.py
+-- calorietrack/
|   +-- settings.py
|   +-- urls.py
|   +-- asgi.py
|   +-- wsgi.py
+-- apps/
|   +-- accounts/
|   +-- calories/
|   +-- dashboard/
+-- templates/
|   +-- layouts/
|   +-- includes/
|   +-- accounts/
|   +-- calories/
|   +-- dashboard/
+-- static/
|   +-- styles/
|   +-- js/
+-- README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/calorietrack.git
cd calorietrack
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

3. Install Django:

```bash
pip install django
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open the app in your browser:

```text
http://127.0.0.1:8000/
```

## Main Pages

- Landing page: `/`
- Login: `/accounts/login/`
- Register: `/accounts/register/`
- Dashboard: `/dashboard/`
- Add meal: `/calories/add/`
- Food database: `/calories/foods/`
- History: `/calories/history/`
- Goal settings: `/accounts/settings/`

## Models

The app uses three main calorie-tracking models:

- `Food`: stores food name, calories, and serving size
- `Meal`: stores meals logged by users
- `Goal`: stores each user's daily calorie goal

Each meal belongs to a logged-in Django user.
