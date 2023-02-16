import requests
import json

# test purposes
stop_count = 20
testing = True

# code
next_page_token_text = "next_page_token"
api_key = "AIzaSyCnRkXos1XsHViYmnhAX0p35QOZhvb6cyo"
query = "restaurants%20in%20toronto"

url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

file = open('data\data1.txt', 'w', encoding="utf-8")
file.write(response.text)
file.close()

# get next_page_token
data = json.loads(response.text)
next_page_token = data[next_page_token_text]

count = 2 # second data file

while next_page_token_text in data.keys(): #check if there is a next page token
  payload={}
  headers = {}

  url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={api_key}"


  file = open(f'data\data{count}.txt', 'w', encoding="utf-8")
  file.write(response.text)
  file.close()

  # get next_page_token
  data = json.loads(response.text)
  next_page_token = data[next_page_token_text]

  count += 1 # continue to next data file
  # print(response.text)
  # print("Number of results {}".format(len(data["results"])))

  if count == stop_count and testing: # early breaking for testing
    break




# import requests


# location = "43.6532%2C79.3832"
# type = "restaurant"
# radius = 1500

# url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={type}&type={radius}&key=AIzaSyCnRkXos1XsHViYmnhAX0p35QOZhvb6cyo"

# url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522%2C79.1957362&radius=1500&type=restaurant&keyword=cruise&key=AIzaSyCnRkXos1XsHViYmnhAX0p35QOZhvb6cyo"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)


# from __future__ import print_function

# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# CLIENT_FILE = 'client_secret_389410694282-8k2dvd6240t1f6hp2os79sfir1ajb716.apps.googleusercontent.com'

# # The ID of a sample document.
# DOCUMENT_ID = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'

# API_KEY = 'AIzaSyCnRkXos1XsHViYmnhAX0p35QOZhvb6cyo'

# def main():
#     """Shows basic usage of the Docs API.
#     Prints the title of a sample document.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     try:
#         service = build('docs', 'v1', credentials=creds)

#         # Retrieve the documents contents from the Docs service.
#         document = service.documents().get(documentId=DOCUMENT_ID).execute()

#         print('The title of the document is: {}'.format(document.get('title')))
#     except HttpError as err:
#         print(err)


# if __name__ == '__main__':
#     main()