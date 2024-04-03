## ***
## Helper functions for the Named Entity Recognition module
## ***

import re
import requests

url = "https://discovery.nationalarchives.gov.uk/API/records/v1/details/"

def getNE(ner_results):
    named_entities = []
    seq = ""
    ent = ""
    ent_last = ""
    named_entities = []
    for i, j in enumerate(ner_results):
      if j["entity"][0] == 'B':
        if ent == "":
          ent = j["entity"]
        if seq != "":
          if j["word"][0:2] == '##':
            seq = seq + j["word"][2:]
          else:
            named_entities.append((seq, ent[2:]))
            seq = j["word"]
            ent_last = ent
            ent = ""
        else:
          seq = j["word"]
      if j["entity"][0] == 'I':
        if j["word"][0:2] == '##':
          seq = seq + j["word"][2:]
        else:
          seq = seq + " " + j["word"]
    named_entities.append((seq, ent_last[2:]))
    return named_entities

def get_pad(sentence, named_entities):
    sentence_pad = sentence
    for ne in named_entities:
      pad = ""
      name = ne[0].split(" ")
      text = sentence.split(" ")
      for i in name:
        for j in text:
          j = re.sub('[^A-Za-z0-9]+', '', j)
          match = re.search(i+'.+',j)
          if match:
            i = j
        if pad == "":
          pad += i
        else:
          pad += " " + i
      print(pad)
      if ne[1] == "B-PER":
        sentence_pad = sentence_pad.replace(pad,"[START]"+pad+"[END]")
    return sentence_pad

def populate_texts(textID):
    response = requests.request("GET", url+textID)
    description = response.json()['scopeContent']['description']
    description = re.sub('<scopecontent>', '', description)
    description = re.sub('</scopecontent>', '', description)
    description = re.sub('<p>', '', description)
    description = re.sub('</p>', '', description)
    return description