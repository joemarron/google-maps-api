# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:55:51 2023

@author: joema
"""

# Import Libraries
import config as cf # Load file with API key
import googlemaps # import googlemaps package: `pip install googlemaps`


def calc_distance(origin:str, destination:str, dist_unit:str="mi", region:str="uk", mode:str="driving", transit_mode:str=None, is_return=False):
    
    """
    Calculate the distance between two locations using the Google Maps Distance Matrix API.

    Args:
        origin (str): The starting location for distance calculation.
        destination (str): The ending location for distance calculation.
        dist_unit (str, optional): The desired unit of distance measurement, "mi" (miles) or "km" (kilometers). Defaults to "mi".
        region (str, optional): The region/country used for route calculation (e.g., "uk" for the United Kingdom). Defaults to "uk".
        mode (str, optional): The mode of transportation, e.g., "driving", "walking", "bicycling", "transit". Defaults to "driving".
        transit_mode (str, optional): Additional transit mode information if mode = "transit" (e.g., "bus" or "subway") for public transit. Defaults to None.

    Returns:
        float: The calculated distance between the origin and destination in the specified distance unit.

    Raises:
        Exception: Raised when there are missing start or end location parameters, or if the API response is not recognized.
        ValueError: Raised when an unrecognised `dist_unit` value is provided (Expected `mi` or `km`).

    Example:
        distance = calc_distance("Doncaster", "London", dist_unit="mi", mode="driving")
        print(f"Distance: {distance} miles")
    
    Note:
        - You need a valid Google Maps API key set in `cf.api_key` to use this function.
        - The function utilizes the Google Maps Distance Matrix API to calculate distances.
    """
    
    if not origin or not destination:
        raise Exception("Missing start or end location parameters.")
    
    gmaps = googlemaps.Client(key=cf.api_key)
    
    if not transit_mode:
        resp = gmaps.distance_matrix(origin, destination, mode=mode, region=region, units="imperial")
    else:
        resp = gmaps.distance_matrix(origin, destination, mode=mode, transit_mode=transit_mode, region=region, units="imperial")
        
    try:
        dist = resp["rows"][0]["elements"][0]["distance"]["value"]
        if is_return:
            dist *= 2
        if dist_unit == "mi":
            dist = round(dist/1000/1.609, 2)
        elif dist_unit != "km":
            raise ValueError("Unrecognised `dist_unit` value: Expected `mi` or `km`.")
    except:
        raise Exception("API Response not recognised. Check start and end location parameters or validity of API key.")
    
    return dist
            
    
    
if __name__ == "__main__":
    print(calc_distance("Doncaster", "London"))
