# Survivor Journal

## Overview
The Bootcamp Survivor Journal is a Django based project designed to give students of the 16 week Code Institute Bootcamp a place to document their personal experiences of undertaking and completing the 16 week Full Stack Development course.
This is not just a log of tasks, it is a place for students to record their transformation and resilience throughout the course. A place for them to voice their trials and tribulations.

## Table of Contents

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