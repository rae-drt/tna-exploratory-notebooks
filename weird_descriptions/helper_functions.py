import requests
import json
import time

baseurl = "https://discovery.nationalarchives.gov.uk/API"
search_endpoint = "/search/records"
children_endpoint = "/records/children/"

def find_first_level_children(series, max_depth):
    found_children = []
    for i in range (1, 1000): # shold cover all possible child series
        time.sleep(1)
        url = baseurl + search_endpoint + "?sps.recordSeries=" + series + "%20" + str(i) + "&sps.catalogueLevels=Level3" # for eg gets us ADM 1, ADM 2
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers)
        response_json = response.json()
        if response_json["records"] != []:
            found_children.append({
                "series": series + " " + str(i),
                "id": response_json["records"][0]["id"],
                "description": response_json["records"][0]["description"],
                "children": find_children([{"id": response_json["records"][0]["id"]}], max_depth, 1)
            })
        else:
            break
    return found_children

def find_children(series, max_depth, current_depth):
    return_dict = {}
    current_depth += 1
    print("Current ID: " + str(series))
    for individual in series:
        time.sleep(1)
        url = baseurl + children_endpoint + individual["id"]
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers)
        response_json = response.json()
        if response.status_code == 200:
            if len(response_json["assets"]) > 0:
                assets = []
                for asset in response_json["assets"]:
                    if current_depth >= max_depth:
                        children = ["Max depth reached"]
                    else:
                        children = find_children([{"id": asset["id"]}], max_depth, current_depth)
                    assets.append({
                        "id": asset["id"],
                        "description": asset["scopeContent"]["description"],
                        "children": children
                    })
                return_dict = assets
            else:
                return_dict = "No children"
                break
    return return_dict

def count_records(data):
    count = 0
    if data["children"] == "No children":
        return 1
    for child in data["children"]:
        count += count_records(child)
    return count

def get_series_description(series):
    data = {}
    max_depth = 99
    data["top_level"] = series
    data["children"] = find_first_level_children(series, max_depth)
    data["total_records_count"] = count_records(data)
    return data


def filter_children(data):
    ignore_key = "children"
    filterd_data = {}
    for key, value in data.items():
        if key != ignore_key:
            filterd_data[key] = value
        else:
            filterd_data[key] = "Children not printed"
    return filterd_data