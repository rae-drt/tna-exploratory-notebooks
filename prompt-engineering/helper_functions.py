## ***
## Helper functions for the prompt engineering module
## ***

import re
import requests

url = "https://discovery.nationalarchives.gov.uk/API/records/v1/details/"

def append_IDs(ID_list, listString):
    for i in listString.split(','):
        ID_list.append(re.sub('[^A-Za-z0-9]+', '', i))
    return ID_list


def populate_documents(documentIDs):
    documents = {}
    for i in documentIDs:
        response = requests.request("GET", url+i)
        title = response.json()['title']
        description = response.json()['scopeContent']['description']
        title = re.sub('<unittitle type="Title">', '', title)
        title = re.sub('</unittitle>', '', title)
        description = re.sub('<scopecontent><head>Scope and Content</head>', '', description)
        description = re.sub('</scopecontent>', '', description)
        description = re.sub('<p>', '', description)
        description = re.sub('</p>', '', description)
        documents[title] = description
    return documents

def populate_texts(textIDs):
    texts = []
    for i in textIDs:
        response = requests.request("GET", url+i)
        description = response.json()['scopeContent']['description']
        description = re.sub('<scopecontent>', '', description)
        description = re.sub('</scopecontent>', '', description)
        description = re.sub('<p>', '', description)
        description = re.sub('</p>', '', description)
        texts.append(description)
    return texts
