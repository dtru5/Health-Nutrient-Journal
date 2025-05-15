🥗 Food & Nutrient Journal
Overview

This project is an in-progress Python-based application designed to help users track their daily food intake and compare their nutrient consumption against recommended dietary guidelines. By leveraging the USDA FoodData Central API, the app retrieves nutritional data (calories, macronutrients, micronutrients) for both branded and foundation food items.

Users can log their meals into a daily journal, and over time, gain insights into their nutritional habits.
✨ Features

    🔍 Search for foods using public USDA databases

    📊 View detailed nutrient breakdowns including calories, proteins, fats, carbs, and micronutrients

    📆 Log food entries with quantity, date, and time

    👤 User accounts to manage individual journals

    📈 Compare daily intake with standard dietary recommendations (planned)

📂 Project Structure
Code: main.py

Core Python script to:

    Take user input for food search

    Call the USDA API

    Display search results and nutritional details

    Prompt user to add the food item to their journal (database integration planned)
    
🧪 Getting Started

    Clone the repository

    Install dependencies (if any in future)

    Get your USDA API key from https://fdc.nal.usda.gov/api-key-signup.html

    Run the main script:

python main.py

🛠 Future Enhancements

    Integrate food logging directly into a database

    User authentication and dashboard

    Visual charts of nutrient trends

    Nutrient intake recommendations and warnings

    Exporting logs and summaries
