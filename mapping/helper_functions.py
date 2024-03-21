# series of 12 waypoints along the English Channel for the first ship, with timestamps and speed 

leader_waypoints = [
    {"timestamp": "2015-02-24T00:00:00Z", "latitude": 48.0, "longitude": -7.0},
    {"timestamp": "2015-02-24T01:00:00Z", "latitude": 48.5, "longitude": -6.0},
    {"timestamp": "2015-02-24T02:00:00Z", "latitude": 49.0, "longitude": -4.5},
    {"timestamp": "2015-02-24T03:00:00Z", "latitude": 49.5, "longitude": -3.2},
    {"timestamp": "2015-02-24T04:00:00Z", "speed": 17.0, "latitude": 50, "longitude": -2.8},
    {"timestamp": "2015-02-24T05:00:00Z", "speed": 17.0, "latitude": 50.5, "longitude": -1.7},
    {"timestamp": "2015-02-24T06:00:00Z", "speed": 17.0, "latitude": 50.3, "longitude": -1.2},
    {"timestamp": "2015-02-24T07:00:00Z", "speed": 17.0, "latitude": 50.3, "longitude": 0},
    {"timestamp": "2015-02-24T08:00:00Z", "speed": 17.0, "latitude": 50.7, "longitude": 1.2},
]

chaser_waypoints = [
    {"timestamp": "2015-02-24T02:00:00Z", "latitude": 47.8, "longitude": -7.0},
    {"timestamp": "2015-02-24T03:00:00Z", "latitude": 48.6, "longitude": -6.3},
    {"timestamp": "2015-02-24T04:00:00Z", "latitude": 49.0, "longitude": -4.5},
    {"timestamp": "2015-02-24T05:00:00Z", "latitude": 49.5, "longitude": -3.2},
    {"timestamp": "2015-02-24T06:00:00Z", "latitude": 49.9, "longitude": -2.8},
    {"timestamp": "2015-02-24T07:00:00Z", "latitude": 50.0, "longitude": -1.7},
    {"timestamp": "2015-02-24T08:00:00Z", "latitude": 49.95, "longitude": -0.8},
    {"timestamp": "2015-02-24T09:00:00Z", "latitude": 50.0, "longitude": 0},
    {"timestamp": "2015-02-24T10:00:00Z", "latitude": 49.5, "longitude": -0.1},
]

height_of_surprise_in_m = 40

height_of_acheron_in_m = 48

nautical_miles_to_degrees = 1 / 60

def height_in_m_to_visibility_in_nautical_miles(h):
    #return 1.852 * (math.sqrt(2 * h / 0.573))
    return (2.04 * (h ** 0.5))

def visibility_in_nm_to_visibility_in_degrees(v):
    return v * nautical_miles_to_degrees

def visibility_around_a_waypoint(waypoint_lat, waypoint_long, height_of_observer):
    visibility = height_in_m_to_visibility_in_nautical_miles(height_of_observer)
    max_north = waypoint_lat + visibility_in_nm_to_visibility_in_degrees(visibility) 
    min_north = waypoint_lat - visibility_in_nm_to_visibility_in_degrees(visibility)
    max_east = waypoint_long + visibility_in_nm_to_visibility_in_degrees(visibility)
    min_east = waypoint_long - visibility_in_nm_to_visibility_in_degrees(visibility)
    north_waypoint = [max_north, waypoint_long]
    south_waypoint = [min_north, waypoint_long]
    east_waypoint = [waypoint_lat, max_east]
    west_waypoint = [waypoint_lat, min_east]
    return [north_waypoint, east_waypoint, south_waypoint, west_waypoint]