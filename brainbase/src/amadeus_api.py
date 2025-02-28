import os
from amadeus import Client, ResponseError
import amadeus
import arrow
from dataclasses import dataclass


class AmadeusAPI:
    def __init__(self) -> None:
        self.amadeus_client = Client()
        
    def points_of_interest_search(
        self,
        latitude: float,
        longitude: float,
    ):
        try:
            response = self.amadeus_client.reference_data.locations.points_of_interest.get(
                longitude=longitude,
                latitude=latitude
            )
            
            pois = []
            for poi in response.data:
                poi_dict = {
                "type": poi.get("type"),
                "subType": poi.get("subType"),
                "id": poi.get("id"),
                "name": poi.get("name"),
                "category": poi.get("category"),
                "rank": poi.get("rank"),
                "geoCode": poi.get("geoCode"),
                "tags": poi.get("tags")
            }
            pois.append(poi_dict)
        
            return pois, response.status_code
        except ResponseError as re:
            return re.response.body, re.response.status_code

    def flight_offers_search(
        self,
        origin_location_code: str,
        destination_location_code: str,
        departure_date: str = arrow.now().shift(days=1).format('YYYY-MM-DD'),
        adults: str = '1'
    ):
        try:
            response = self.amadeus_client.shopping.flight_offers_search.get(
                originLocationCode=origin_location_code,
                destinationLocationCode=destination_location_code,
                departureDate=departure_date,
                adults=adults
            )
            flights_list = []
            for flights in response.data:
                flight_dict = {
                    "source": flights.get("source"),
                    "instantTicketingRequired": flights.get("instantTicketingRequired"),
                    "nonHomogeneous": flights.get("nonHomogeneous"),
                    "oneWay": flights.get("oneWay"),
                    "lastTicketingDate": flights.get("lastTicketingDate"),
                    "numberOfBookableSeats": flights.get("numberOfBookableSeats"),
                    "price": flights.get("price"),
                    "pricingOptions": flights.get("pricingOptions"),
                    "validatingAirlineCodes": flights.get("validatingAirlineCodes"),
                    "travelerPricings": flights.get("travelerPricings"),
                    "itineraries": []
                }

                for itinerary in flights.get("itineraries", []):
                    itinerary_dict = {
                        "duration": itinerary.get("duration"),
                        "segments": []
                    }
                    
                    for segment in itinerary.get("segments", []):
                        segment_dict = {
                            "departure": segment.get("departure"),
                            "arrival": segment.get("arrival"),
                            "carrierCode": segment.get("carrierCode"),
                            "number": segment.get("number"),
                            "aircraft": segment.get("aircraft"),
                            "duration": segment.get("duration"),
                            "numberOfStops": segment.get("numberOfStops"),
                            "blacklistedInEU": segment.get("blacklistedInEU")
                        }
                        itinerary_dict["segments"].append(segment_dict)
                    
                    flight_dict["itineraries"].append(itinerary_dict)
                    
                flights_list.append(flight_dict)
        
            return flights_list[0:3], response.status_code
        
        except ResponseError as re:
            return re.response.body, re.response.status_code
            
    def hotels_by_city(
        self,
        city_code: str,
        radius: int,
        amenities: list[str] = None,
        ratings: list[str] = ['5'],
    ):
        try:
            response = self.amadeus_client.reference_data.locations.hotels.by_city.get(
                cityCode = city_code,
                radius=radius,
                ratings=ratings,
            )
            
            gotten_hotels = []
            for hotel in response.data:
                hotel_dict = {
                    "name": hotel.get("name"),
                    "hotelId": hotel.get("hotelId"),
                    "address": hotel.get("address").get("countryCode")
                }
                gotten_hotels.append(hotel_dict)
            
            return gotten_hotels[0:3], response.status_code
        
        except ResponseError as re:
            return re.response.body, re.response.status_code
            
    def plan_trip_by_chaining(
        self,
        origin_location_code: str,
        destination_location_code: str,
        ratings: list[str] = ['5', '4'],
        departure_date: str = arrow.now().shift(days=1).format("YYYY-MM-DD"),
        adults: str = '1',
        radius: int = 5,
    ):
        try:
            flights, flight_status_code = self.flight_offers_search(origin_location_code, destination_location_code, departure_date, adults)
            hotels, hotel_status_code = self.hotels_by_city(destination_location_code, radius, ratings)
        
            flights_hotels = flights + hotels
            
            for code in [flight_status_code, hotel_status_code]:
                if code != 200:
                    raise ResponseError(response="Recieved non valid code")
        
            return flights_hotels, 200
        
        except ResponseError as re:
            return re.response.body, re.response.status_code
            
    
            
if __name__ == "__main__":
   # print(AmadeusAPI().flight_offers_search('MAD', 'BOS', '2025-07-01', '1'))
    print(AmadeusAPI().points_of_interest_search(48.8583736, 2.2922926))
