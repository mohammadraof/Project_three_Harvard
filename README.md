# Django Library Management System

A simple library management system built with Django.

## Features

* View books
* View members
* Search books
* Borrow books
* Return books
* View borrowing history
* View library statistics

## Technologies

* Python
* Django
* HTML
* CSS

## Project Structure

Tamrin/
├── config/
├── library/
│   ├── templates/
│   │   └── library/
│   ├── sample_data.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md

## Installation

Create and activate a virtual environment:

python -m venv .venv

Activate it on Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

## Run the Project

python manage.py runserver

Then open:

http://127.0.0.1:8000/

## Note

This project uses Python lists and dictionaries for storing data during runtime. No database is required.
