
import requests

API_KEY = 'enter your api key here'

# Step 1: Get user input for food query and dataType
user_input = input("Please enter a food: ")
data_type_input = input("Enter 'B' for Branded foods or 'F' for Foundation foods: ").upper()

# Determine the dataType based on user input
data_type = "Branded" if data_type_input == "B" else "Foundation" if data_type_input == "F" else None

if not data_type:
    print("Invalid input for data type. Please enter 'B' or 'F'.")
else:
    # Step 2: Make API request with user query and dataType
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={user_input}&dataType={data_type}&api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        if not data.get('foods'):
            print("No results found. Try another query.")
        else:
            # Step 3: Display search results with numbers
            print("Search Results:")
            for idx, food in enumerate(data['foods'], start=1):
                print(f"{idx}. {food['description']}")
            
            # Step 4: Allow user to pick a food by number
            try:
                choice = int(input("Enter the number of the food to see full details: ")) - 1
                if 0 <= choice < len(data['foods']):
                    selected_food = data['foods'][choice]
                    print("\nFull Details:")
                    print(f"Description: {selected_food['description']}")
                    print(f"Data Type: {selected_food['dataType']}")
                    print("Nutrients:")
                    for nutrient in selected_food.get('foodNutrients', []):
                        if nutrient['value'] > 0.0:
                            print(f"  {nutrient['nutrientName']}: {nutrient['value']} {nutrient['unitName']}")
                    addFood = input("Would you like to add this food?: yes (Y/N): ").upper()
                    
                else:
                    print("Invalid choice. Please run the program again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    else:
        print(f"Error: {response.status_code}")
