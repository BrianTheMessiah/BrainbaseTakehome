extract_flight_offers_search = {
    "type": "function",
    "function": {
        "name": "extract_flight_offers_search",
        "description": "Extract flight details from the user prompt if they ask specifically about flights",
        "parameters": {
            "type": "object",
            "properties": {
                "origin_location_code": {
                    "type": "string",
                    "description": "The origin location code"
                },
                "destination_location_code": {
                    "type": "string",
                    "description": "The destination location code"
                },
                "departure_date": {
                    "type": "string",
                    "description": "The date of departure"
                },
                "adults": {
                    "type": "string",
                    "description": "How many people are over 12"
                }
            },
            "required": ["query"]
        }
    }
}

extract_hotels_by_city = {
    "type": "function",
    "function": {
        "name": "extract_hotels_by_city",
        "description": "Extract hotel details from the user prompt if they ask specifically about hotels",
        "parameters": {
            "type": "object",
            "properties": {
                "city_code": {
                    "type": "string",
                    "description": "The code of where the hotel is located"
                },
                "radius": {
                    "type": "integer",
                    "description": "Maximum distance from the geographical coordinates express in defined units. The default unit is metric kilometer."
                },
                "ratings": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Potential list of user inputted ratings that can be up to 4 values"
                },
                "amenities": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "List of wanted amenities that the user requests"
                }
            },
            "required": ["query"]
        }
    }
}

extract_points_of_interest = {
    "type": "function",
    "function": {
        "name": "extract_points_of_interest",
        "description": "Extract points of interest details and the latitude \
            and longitude from the user prompt if they ask about particular things \
            an area",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {
                    "type": "number",
                    "description": "The latitude to the 6th decimal place of where the user is or where they want to be"
                },
                "longitude": {
                    "type": "number",
                    "description": "The longitude to the 6th decimal place of where the user is or where they want to be"
                }
            },
            "required": ["query"]
        }
    }
}

plan_my_trip = {
    "type": "function",
    "function": {
        "name": "plan_my_trip",
        "description": "Plans the entire trip based on where the user is and where they want to go",
        "parameters": {
            "type": "object",
            "properties": {
                "radius": {
                    "type": "integer",
                    "description": "Maximum distance from the geographical coordinates express in defined units. The default unit is metric kilometer."
                },
                "ratings": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Potential list of user inputted ratings that can be up to 4 values"
                },
                "amenities": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "List of wanted amenities that the user requests"
                },
                "origin_location_code": {
                    "type": "string",
                    "description": "The origin location code"
                },
                "destination_location_code": {
                    "type": "string",
                    "description": "The destination location code"
                },
                "departure_date": {
                    "type": "string",
                    "description": "The date of departure, if one isnt given look for one past the current date"
                },
                "adults": {
                    "type": "string",
                    "description": "How many people are over 12"
                }
            },
            "required": ["query"]
        }
    }
}

tools = [
    plan_my_trip,
    extract_flight_offers_search,
    extract_hotels_by_city,
    extract_points_of_interest
]
