import requests
import json
import math
import numpy as np

# test purposes
stop_count = 20
testing = True

# code
next_page_token_text = "next_page_token"
api_key = ""
query = "restaurants%20in%20toronto"
location = "43.6532%2C79.3832"

top_left_latitude = 43.749808
top_left_longitude = -79.639074
bottom_left_latitude = 43.34529
bottom_left_longitude = 79.32376

top_right_latitude = 43.855205
top_right_longitude = -79.171079
bottom_right_latitude = 43.794346
bottom_right_longitude = -79.117834

top_left = "{top_left_latitue}%2C{top_left_longitude}"
bottom_left = "{bottom_left_latitude}%2C{bottom_left_longitude}"
top_right = "{top_right_latitude}%2C{top_right_longitude}"
bottom_right = "{bottom_right_latitude}%2C{bottom_right_longitude}"

linspace = math.floor(abs(top_left_longitude - top_right_longitude)/0.05)
longitudes = np.linspace(top_left_longitude, top_right_longitude, linspace) 

linspace = math.floor(abs(top_left_latitude - bottom_left_latitude)/0.05)
latitudes = np.linspace(bottom_left_latitude, top_left_latitude, linspace) 
print(longitudes)
count = 1
for longitude in longitudes:
  for latitude in latitudes:

    print(longitude)
    location = "{latitude}%2C{longitude}"

    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?location={location}&radius=.5&query={query}&key={api_key}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    file = open(f'data\data{count}.txt', 'w', encoding="utf-8")
    file.write(response.text)
    file.close()
    count += 1



# # get next_page_token
# data = json.loads(response.text)
# next_page_token = data[next_page_token_text]



# count = 2 # second data file

# while next_page_token_text in data.keys(): #check if there is a next page token
#   payload={}
#   headers = {}

#   url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={api_key}"


#   file = open(f'data\data{count}.txt', 'w', encoding="utf-8")
#   file.write(response.text)
#   file.close()

#   # get next_page_token
#   data = json.loads(response.text)
#   next_page_token = data[next_page_token_text]

#   count += 1 # continue to next data file
#   # print(response.text)
#   # print("Number of results {}".format(len(data["results"])))

#   if count == stop_count and testing: # early breaking for testing
#     break
