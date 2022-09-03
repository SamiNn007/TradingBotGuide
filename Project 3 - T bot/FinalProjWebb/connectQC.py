##import base64
#import hashlib
#import time
#import requests
#import pandas as pd

#User ID: 209544
#Token: 11d6db38bdf62b4a06374e4c18937208fd1a13b82d22fa8da8b8ca889947ebda

# Get timestamp
timestamp = str(int(time.time()))
time_stamped_token = "11d6db38bdf62b4a06374e4c18937208fd1a13b82d22fa8da8b8ca889947ebda" + ':' + timestamp

# Get hased API token
hashed_token = hashlib.sha256(time_stamped_token.encode('utf-8')).hexdigest()
authentication = "{}:{}".format(209544, hashed_token)
api_token = base64.b64encode(authentication.encode('utf-8')).decode('ascii')

# Create headers dictionary.
headers = {
   # 'Authorization': 'Basic %s' % api_token,
    #'Timestamp': timestamp
}

# Create POST Request with headers (optional: Json Content as data argument).
response = requests.post("https://www.quantconnect.com/api/v2/projects/read", 
                         data = {}, 
                         headers = headers)
#content = response.json()
#reponse = api.ReadProject({"projectId": 12693213, 'project_name':'main.py'} )
#print(content)
#reponse = content.ReadProject({"projectId": 12693213, 'project_name':'main.py'} )
#print(response)
#print(pd.json_normalize(content))


