# Survivor Journal

## Overview
The Bootcamp Survivor Journal is a Django based project designed to give students of the 16 week Code Institute Bootcamp a place to document their personal experiences of undertaking and completing the 16 week Full Stack Development course.
This is not just a log of tasks, it is a place for students to record their transformation and resilience throughout the course. A place for them to voice their trials and tribulations.

## Table of Contents

- [Overview](#overview)
- [UX Design](#ux-design)
- [Project Planning](#project-planning)
- [Key Features](#key-features)
- [Developer Notes](#developer-notes)
- [Deployment](#deployment)
- [Libraries & Frameworks](#libraries--frameworks)
- [Languages & Technologies Used](#languages--technologies-used)
- [AI Implementation](#ai-implementation)
- [Credits](#credits)

## UX Design
Clean, readable layout focused on content and forms
Consistent visual language: Bootstrap + CSS
Centered auth cards for login/register/logout pages
Sticky footer and a centered main container
Accessible: visible focus states
Forms: clear labels, inline validation errors, and accessible controls
Feedback: flash messages appear at the top and auto-dismiss after 5 seconds
Responsive: auth card and main container adapt on small screens; actions stack on narrow viewports

## Project Planning
MOSCOW Prioritisation
- Login (Must-Have)
- Account Registration (Must-Have)
- Logout (Must-Have)
- Home Page (Must-Have)
- Create Posts (Must-Have)
- Admin Post Verification (Must-Have)
- About Page (Should-Have)
- Search Bar (Should-Have)
- Welcome Message (Could-Have)

ERD Diagram
![alt text](images/erd.png)
Wireframes

Home Page
![alt text](images/wireframe.png)

Sign up Page
![alt text](images/wireframe1.png)

About us Page
![alt text](images/wireframe2.png)

## Key Features
- User Authentication
User registration, login and logout

- Journal Entries
CRUD functionalities for journal entries

- Dashboard / Home View
Navbar, Journal Entries Page

- Clean UI
Dark mode option, minimalist design, focus on readability
Mobile responsive layout

- Admin Panel
Admin view for managing users, monitoring shared entries
## Developer Notes

- Prerequisites: Python 3.12+, virtualenv, Git. Optional: PostgreSQL.
- Setup:
	1. Create venv and install deps
		 ```bash
		 python -m venv .venv
		 source .venv/bin/activate
		 pip install -r requirements.txt
		 ```
	2. Environment variables (create an `env.py` or export in shell):
		 - `SECRET_KEY`: any random string for local dev.
		 - `DATABASE_URL`: set to a valid URL (examples below).
		 - Optional Cloudinary: `CLOUDINARY_URL` if you use Cloudinary images.
	3. Static files (required since `DEBUG=False`):
		 ```bash
		 python manage.py collectstatic --noinput
		 ```
	4. Run server:
		 ```bash
		 python manage.py runserver
		 ```

- Database URLs (dj-database-url):
	- SQLite (simple local dev): `sqlite:///db.sqlite3`
	- Postgres (local): `postgres://USER:PASSWORD@127.0.0.1:5432/DBNAME`
	- Heroku-style: `postgres://...` or `postgresql://...`
	- If you see `UnknownSchemeError` ensure the value is not empty and uses a known scheme (e.g., `sqlite:///...`, `postgres://...`). Avoid quotes that render as `b''` or whitespace.

- Static files:
	- Author source assets under `static/` (e.g., `static/images/...`).
	- Do NOT edit `staticfiles/` directly; it is build output from `collectstatic`.
	- In templates use `{% load static %}` and `{% static 'images/your-file.png' %}`.

- Auth templates and styling:
	- allauth pages inherit the site layout via `templates/allauth/layouts/base.html -> extends base.html`, so your CSS and Bootstrap are loaded for login/logout/signup.
	- Logout page uses a centered layout and `.btn-delete` accent; adjust in `static/css/style.css` if needed.

- Images on About page:
	- Place images in `static/images/` and reference with `{% static 'images/name.jpg' %}`.
	- Example used: `static/images/david.jpg`.

- Common issues:
	- Static not loading: verify `STATIC_URL=/static/`, run `collectstatic`, and hard refresh the browser.
	- DB errors: confirm `DATABASE_URL` is set and correctly formatted; for quick local dev use SQLite URL shown above.
	- Template overrides: if an allauth page looks unstyled, ensure the layout override exists at `templates/allauth/layouts/base.html`.

## Deployment

Heroku deploy notes:

- Ensure Debug=False and Whitenoise is enabled
- Push code and build:
	- git add . git commit -m "" git push, pushing all the data to github for deployment to Heroku
- When the code is pushed to GitHub, go to Heroku, go to the deploy tab in heroku, scroll down and click 'Deploy Branch' 
- When Heroku finishes the build, the logs can be viewed in case of any errors
- After ensuring there are no errors, click 'Open App' or 'View' to open the deployed app

## Libraries & Frameworks
- Django 4.2 — main web framework
- django-allauth — user authentication
- WhiteNoise — serves static files in production
- Gunicorn — production WSGI server
- dj-database-url — parses DATABASE_URL
- psycopg2 — PostgreSQL driver
- Bootstrap 5 — responsive UI

## Languages & Technologies Used
- Languages: Python 3.12, HTML5, CSS3, JavaScript
- Frontend: Bootstrap 5, JavaScript
- Deployment / Ops: Heroku, Gunicorn, WhiteNoise, Git
- Tools: GitHub, Django manage commands

## AI Implementation
Provided suggestions for styling and html setup
Performed focused code patches (templates, forms, CSS) to speed iteration.
Diagnosed template and deployment issues and suggested fixes.

## Credits
- Thanks To Max, Rhys, Josh and David for each contributing seperately to this project
- Thanks to Code Institute for use of their material and tools such as copilot and the LS
- W3C HTML W3C HTML Validator for HTML Validation
- W3C CSS Valdiator for CSS validation