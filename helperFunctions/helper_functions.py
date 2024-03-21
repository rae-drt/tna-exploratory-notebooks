## ***
## Helper functions for the mapping module
## ***

## A series of data points for 2 ships engaged in a chase battle along the English Channel. These data are entirely fictional and fabricated, designed to be useful 
## for a programming exercise. As the data are fictional, the speed may not be correct based on the timestamps and distances between waypoints. 

leader_waypoints = [
    {"timestamp": "2015-02-24T00:00:00Z", "latitude": 48.0, "longitude": -7.0, "crew": 223, "speed": 13},
    {"timestamp": "2015-02-24T01:00:00Z", "latitude": 48.5, "longitude": -6.0, "crew": 215, "speed": 12.7},
    {"timestamp": "2015-02-24T02:00:00Z", "latitude": 49.0, "longitude": -4.5, "crew": 210, "speed": 13.2},
    {"timestamp": "2015-02-24T03:00:00Z", "latitude": 49.5, "longitude": -3.2, "crew": 210, "speed": 12.1},
    {"timestamp": "2015-02-24T04:00:00Z", "latitude": 50, "longitude": -2.8, "crew": 198, "speed": 12.3},
    {"timestamp": "2015-02-24T05:00:00Z", "latitude": 50.5, "longitude": -1.7, "crew": 190, "speed": 11.7},
    {"timestamp": "2015-02-24T06:00:00Z", "latitude": 50.3, "longitude": -1.2, "crew": 177, "speed": 11.3}, # major broadside, hence the crew decrease
    {"timestamp": "2015-02-24T07:00:00Z", "latitude": 50.3, "longitude": 0, "crew": 177, "speed": 3.1}, # mast shot down, hence the speed drop
    {"timestamp": "2015-02-24T08:00:00Z", "latitude": 50.7, "longitude": 1.2, "crew": 176, "speed": 3.2}, 
]

chaser_waypoints = [
    {"timestamp": "2015-02-24T02:00:00Z", "latitude": 47.8, "longitude": -7.0, "crew": 250, "speed": 13.5},
    {"timestamp": "2015-02-24T03:00:00Z", "latitude": 48.6, "longitude": -6.3, "crew": 248, "speed": 12.8}, # match speed with leader
    {"timestamp": "2015-02-24T04:00:00Z", "latitude": 49.0, "longitude": -4.5, "crew": 245, "speed": 13.2},
    {"timestamp": "2015-02-24T05:00:00Z", "latitude": 49.5, "longitude": -3.2, "crew": 244, "speed": 11.9}, # lucky shot, hence the crew decrease, fall back in speed
    {"timestamp": "2015-02-24T06:00:00Z", "latitude": 49.9, "longitude": -2.8, "crew": 228, "speed": 12.3},
    {"timestamp": "2015-02-24T07:00:00Z", "latitude": 50.0, "longitude": -1.7, "crew": 225, "speed": 12.1}, 
    {"timestamp": "2015-02-24T08:00:00Z", "latitude": 49.95, "longitude": -0.8, "crew": 225, "speed": 11.2},
    {"timestamp": "2015-02-24T09:00:00Z", "latitude": 50.0, "longitude": 0.5, "crew": 224, "speed": 13.1}, # fleet sighted, hence the turn and run
    {"timestamp": "2015-02-24T10:00:00Z", "latitude": 49.5, "longitude": -0.1, "crew": 224, "speed": 13.1},
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