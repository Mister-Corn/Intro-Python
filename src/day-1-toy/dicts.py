# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Write a loop that prints out all the field values for all the waypoints
def printLocationsInWaypoints(waypoints):
    """
    Prints lat, lon, and name of a location from an array of locations
    """
    for location in waypoints:
        lat, lon, name = location.values()
        print(f"lat:{lat}, lon:{lon}, name:{name}")
    print("")

printLocationsInWaypoints(waypoints)
# Add a new waypoint to the list
waypoints.append({
    "lat": 43,
    "lon": -125,
    "name": "too many places"
})

printLocationsInWaypoints(waypoints)