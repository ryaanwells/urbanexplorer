import httplib, json

conn = httplib.HTTPConnection("127.0.0.1", 8000)

conn.request("GET", "/api/v1/userprofile/?format=json")
response = conn.getresponse()
print response.status, response.reason
data = json.dumps(json.loads(response.read()), sort_keys=True,
                  indent=4, separators=(',', ': '))
print data

conn.request("GET", "/api/v1/userprofile/1/?format=json")
response = conn.getresponse()
print response.status, response.reason
data = json.dumps(json.loads(response.read()), sort_keys=True,
                  indent=4, separators=(',', ': '))
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
