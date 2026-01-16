Personal Intelligence & Decision Engine (PIDE)
Project Overview

The Personal Intelligence & Decision Engine (PIDE) is a lightweight analytical system built using Python and Streamlit that helps users log daily activities and gain meaningful insights into how they spend their time, energy, and focus.

The project focuses on data-driven self-analysis without using machine learning, making it a strong foundation for future ML integration.

Key Features

Daily activity logging (name, age, activity, hours, energy, focus)

Input validation with clear error feedback

Persistent data storage using CSV

Safe file handling and error logging

Analytics engine to compute:

Total hours worked

Average hours per entry

Productivity score

Activity-wise time distribution

Interactive dashboard built with Streamlit

Project Structure
pide/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
├── data/
│   ├── activity_log.csv    # Activity data storage
│   └── user_profile.json   # Reserved for future use
│
├── logs/
│   └── errors.log          # Error logs
│
├── utils/
│   ├── file_ops.py         # File handling utilities
│   ├── validators.py       # Input validation logic
│   ├── analytics.py        # Analytics engine
│   └── helpers.py          # Logging utilities

Technologies Used

Python

Streamlit

Pandas

CSV-based persistence

Productivity Score Explanation

The productivity score is calculated using the formula:

Productivity = hours × focus × energy


This approach emphasizes quality of work, not just time spent.

High focus and energy increase productivity

Long hours with low focus reduce productivity

The score is best used for trend comparison, not absolute judgment

How to Run the Project

Activate the virtual environment

Install dependencies:

pip install -r requirements.txt


Run the application:

streamlit run app.py


Open the provided local URL in your browser

Error Handling & Reliability

The app safely handles missing or corrupted CSV files

Invalid user inputs are rejected with clear messages

All runtime errors are logged to logs/errors.log

Analytics functions are empty-safe and never crash the UI

Future Scope (ML Integration)

Replace rule-based productivity logic with ML models

Predict burnout or low-focus days

Learn personalized productivity patterns

Add multi-user support and authentication