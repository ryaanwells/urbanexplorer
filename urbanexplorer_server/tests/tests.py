import httplib, json

conn = httplib.HTTPConnection("127.0.0.1", 8000)


# Check API is live
conn.request("GET", "/api/v1/userprofile/?format=json")
response = conn.getresponse()
print response.status, response.reason
data = json.dumps(json.loads(response.read()), sort_keys=True,
                  indent=4, separators=(',', ': '))
print data


# Check for specific user
conn.request("GET", "/api/v1/userprofile/Ryan/?format=json")
response = conn.getresponse()
print response.status, response.reason
data = json.dumps(json.loads(response.read()), sort_keys=True,
                  indent=4, separators=(',', ': '))
print data


# Create a new session
body = {"routeID":1, "deviceID":"Ryan", "lon": 1, "lat": 1, "timestamp":0}
headers = {"Content-Type": "application/json"}
conn.request("POST", "/startSession/", body=json.dumps(body), headers=headers)
response = conn.getresponse()
print response.status, response.reason 
resp = response.read()
try:
    print json.dumps(json.loads(resp), sort_keys=True,
                     indent=4, separators=(',', ': '))
except ValueError:
    print resp

body = {"sessionID": 5, "lon": 15, "lat": 15, "timestamp": 10001}
conn.request("PATCH", "/updateSession/", body=json.dumps(body), headers=headers)
response = conn.getresponse()

data = response.read()
print response.status, response.reason
print data

"""
data = json.dumps({'deviceID': 1})
headers = {"Content-Type": "application/json"}
conn.request("POST", "/api/v1/userprofile/?format=json", data, headers)
response = conn.getresponse()
print response.status, response.reason
data = json.dumps(json.loads(response.read()), sort_keys=True,
                  indent=4, separators=(',', ': '))
print data
conn.close()
"""
