Workout Logger
A Python script that automatically logs your workouts to Google Sheets using natural language input.

How It Works
You describe your workout in plain English, and the script uses Nutritionix API to extract exercise details. Each exercise gets logged to a Google Sheet with date, time, duration, and calories burned.

Features
Natural Language Input: Just type what you did (e.g., "ran 5km and did 30 minutes of yoga")

Automatic Parsing: Nutritionix identifies exercises, duration, and calories

Google Sheets Integration: All data gets saved to a spreadsheet via Sheety API

Timestamped Entries: Each workout includes date and time of logging

Workflow
Prompts for workout description

Sends text to Nutritionix API with your stats

Receives structured exercise data

Posts each exercise to Google Sheets

Shows confirmation for each entry

Data Tracked
For each exercise, the script records:

Date and time

Exercise name

Duration in minutes

Calories burned

All data is stored in a Google Sheet for easy tracking and analysis.