from pydoc import resolve
import amadeus
from httpx import head
import openai
import os
import json

from openai.resources.chat import Completions
from src.amadeus_api import AmadeusAPI
from src.tools_for_open_ai import tools

api_mapping = {
    "extract_flight_offers_search": {
        "function": AmadeusAPI().flight_offers_search,
        "params":  ["origin_location_code", "destination_location_code", "departure_date", "adults"]
    },
    "extract_hotels_by_city": {
        "function": AmadeusAPI().hotels_by_city,
        "params": ["city_code", "radius", "ratings"]
    },
    "extract_points_of_interest": {
        "function": AmadeusAPI().points_of_interest_search,
        "params": ["latitude", "longitude"]
    },
    "plan_my_trip": {
        "function": AmadeusAPI().plan_trip_by_chaining,
        "params": ["origin_location_code", "destination_location_code", "departure_date", "adults", "city_code", "radius", "ratings"]
    }
}

def query_openai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        tools=tools,
        tool_choice="auto",
    )
    function_arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    function_call = response.choices[0].message.tool_calls[0].function.name
    
    return function_call, function_arguments

def format_data(data):
    data_str = str(data)

    prompt = f"Format the following data into a readable text format:\n{data_str}"

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    formatted_text = response.choices[0].message.content.strip()
    return formatted_text

def call_api(intent, parameters):
    api_details = api_mapping.get(intent)
    if not api_details:
        return {"error": "Unknown intent"}
    
    api_function = api_details["function"]
    function_params = api_details["params"]
    params = {
        key: parameters[key] for key in function_params if key in parameters
    }
    
    data, status_code = api_function(**params)
    if status_code == 200:
        formatted_data = format_data(data)
        return formatted_data
    else:
        return "error " + str(status_code) + " " + data
    
if __name__ == "__main__":
    user_input = "What are some hotels I can find in paris within 5 miles of the city and with 5 star ratings"
    intent, params = query_openai(user_input)
    result = call_api(intent, params)
    
    print(result)
    
    user_input = "What are some cheap flights that I can take if I want to leave by march 3 2025 and want to travel from seattle to new york"
    intent, params = query_openai(user_input)
    result = call_api(intent, params)
    print(result)
