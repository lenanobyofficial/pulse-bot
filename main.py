import requests
from datetime import datetime

# WEATHER API
weather_url = "https://wttr.in/?format=j1"

weather_data = requests.get(weather_url).json()

temp = weather_data['current_condition'][0]['temp_C']
desc = weather_data['current_condition'][0]['weatherDesc'][0]['value']

# QUOTE API
quote_url = "https://zenquotes.io/api/random"

quote_data = requests.get(quote_url).json()

quote = quote_data[0]['q']
author = quote_data[0]['a']

# CREATE SUMMARY
today = datetime.now().strftime("%d-%m-%Y")

summary = f"""
# Daily Pulse Report

Date: {today}

Weather:
{temp}°C - {desc}

Quote:
"{quote}"
- {author}

Generated automatically by Pulse Bot.
"""

# SAVE TO FILE
with open("report.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("README updated successfully!")