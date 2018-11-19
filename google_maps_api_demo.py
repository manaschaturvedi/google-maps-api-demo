import json
import requests


source_address = 'borivali station west'
destination_address = 'malad station west'
key = ''  # enter your API key here
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins='+source_address+'&destinations='+destination_address+'&mode=driving&sensor=false&format=json&key=' + key
ans = requests.get(url)
j_ans = json.loads(ans.text)
total_distance = j_ans['rows'][0]['elements'][0]['distance']['text']
print('Distance between the source and destination address is:',total_distance)
